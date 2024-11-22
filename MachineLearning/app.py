from flask import Flask, render_template, request
import pandas as pd
import joblib
import re
import os

app = Flask(__name__)

# Funktion zur Merkmalsextraktion für URLs
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

# Funktion zur Analyse von E-Mails
def analyze_email(email_content):
    phishing_keywords = ["login", "update", "secure", "password", "verification"]
    suspicious_links = re.findall(r'https?://\S+', email_content)
    keyword_hits = [word for word in phishing_keywords if word in email_content.lower()]

    is_phishing = len(keyword_hits) > 0 or len(suspicious_links) > 0
    return {
        "phishing_keywords": keyword_hits,
        "suspicious_links": suspicious_links,
        "is_phishing": is_phishing
    }

# Modell laden
model_path = 'phishing_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Das Modell '{model_path}' wurde nicht gefunden.")
model = joblib.load(model_path)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    analysis_type = None

    if request.method == "POST":
        analysis_type = request.form["analysis_type"]
        input_text = request.form["input_text"]

        if analysis_type == "url":
            # URL analysieren
            features = pd.DataFrame([extract_features(input_text)])
            prediction = model.predict(features)[0]
            result = "Phishing" if prediction == 1 else "Sicher"
        elif analysis_type == "email":
            # E-Mail analysieren
            email_analysis = analyze_email(input_text)
            result = {
                "is_phishing": "Phishing" if email_analysis["is_phishing"] else "Sicher",
                "details": email_analysis
            }

    return render_template("index.html", result=result, analysis_type=analysis_type)

if __name__ == "__main__":
    app.run(debug=True)
