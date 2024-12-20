import pandas as pd
import re
import os
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Modellpfad definieren
model_path = 'phishing_model.pkl'

# Datensatz laden
data = pd.read_csv("feed.csv")
print(data.head())

# Funktion zur Merkmalsextraktion
def extract_features(url):
    url = url.lower().replace("http://", "").replace("https://", "").rstrip("/")
    return {
        "url_length": len(url),
        "special_char_count": len(re.findall(r"[@_-]", url)),
        "login_in_url": int("login" in url),
        "secure_in_url": int("secure" in url),
        "update_in_url": int("update" in url),
        "num_subdirectories": url.count('/'),
        "num_periods": url.count('.'),
        "num_digits": len(re.findall(r"\d", url)),
        "unusual_tld": int(url.endswith(('.xyz', '.top', '.biz', '.info')))
    }

# Merkmale aus den URLs im Datensatz extrahieren
features = data["url"].apply(lambda url: pd.Series(extract_features(url)))
X = features
y = data["is_phishing"]

# Trainings- und Testdaten splitten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Modell speichern und laden
if os.path.exists(model_path):
    # Modell laden, falls es bereits gespeichert ist
    model = joblib.load(model_path)
    # Überprüfen, ob die Merkmale übereinstimmen
    if set(X.columns) != set(model.feature_names_in_):
        print("Merkmalsnamen haben sich geändert. Trainiere das Modell neu.")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, model_path)
        print("Modell wurde neu trainiert und gespeichert.")
else:
    # Modell trainieren und speichern, falls es nicht existiert
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    print("Modell wurde neu trainiert und gespeichert.")

# Modell evaluieren mit Cross-Validation
cv_scores = cross_val_score(model, X_train, y_train, cv=10)
print("Durchschnittliche Cross-Validation-Genauigkeit:", cv_scores.mean())

# Finale Modellbewertung auf Testdaten
y_pred = model.predict(X_test)
print("Genauigkeit auf Testdaten:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))



def classify_url(url):
    features = pd.DataFrame([extract_features(url)])  # Konvertiere URL-Merkmale in ein DataFrame
    prediction = model.predict(features)[0]  # Vorhersage durch das Modell
    return "Phishing" if prediction == 1 else "Sicher"


for each in data["url"]:
    print(f"URL '{each}' ist: {classify_url(each)}")


while True:
    url = input("Bitte geben Sie eine URL zur Überprüfung ein (oder 'exit' zum Beenden): ")
    if url.lower() == "exit":
        print("Programm beendet.")
        break
    result = classify_url(url)
    print(result)
    print("-" * 50)