import re
import tldextract

def check_phishing(url):
    """
    Prüft, ob eine URL Merkmale eines Phishing-Links aufweist.
    """
    # Extrahiere Domain-Informationen (Subdomain, Domain, TLD)
    domain_info = tldextract.extract(url)
    subdomain = domain_info.subdomain
    domain = domain_info.domain
    suffix = domain_info.suffix

    # Liste bekannter sicherer TLDs (Top Level Domains)
    safe_tlds = ["com", "org", "net", "gov", "edu", "ch", "de", "at", "uk", "fr", "es", "it", "nl", "us"]

    # Prüfkriterien
    warnings = []

    # Regel 1: Überprüfe auf ungewöhnliche Zeichen wie '@', '-', Zahlen in der Domain
    if "@" in url:
        warnings.append("Ungewöhnliches '@'-Zeichen in der URL")
    if "-" in domain:
        warnings.append("Bindestrich im Domain-Namen gefunden, was oft auf Phishing hinweist")
    if re.search(r"\d+", domain):
        warnings.append("Zahlen im Domain-Namen gefunden, was ungewöhnlich ist")

    # Regel 2: Überprüfe, ob die TLD ungewöhnlich ist
    if suffix not in safe_tlds:
        warnings.append(f"Ungewöhnliche TLD (Domain-Endung) '.{suffix}'")

    # Regel 3: Überprüfe, ob die Subdomain lang oder kompliziert aussieht
    if len(subdomain) > 10:
        warnings.append("Lange oder komplizierte Subdomain")

    # Regel 4: Überprüfe auf häufige Phishing-Schlüsselwörter in der URL
    phishing_keywords = ["login", "secure", "account", "update", "verify"]
    for keyword in phishing_keywords:
        if keyword in url.lower():
            warnings.append(f"Verdächtiges Schlüsselwort '{keyword}' in der URL")

    # Rückgabe der Ergebnisse
    if warnings:
        return f"Verdächtige URL: {url}\nWarnungen:\n" + "\n".join(warnings)
    else:
        return f"URL scheint sicher zu sein: {url}"

# Benutzer-Eingabe
while True:
    url = input("Bitte geben Sie eine URL zur Überprüfung ein (oder 'exit' zum Beenden): ")
    if url.lower() == "exit":
        print("Programm beendet.")
        break
    result = check_phishing(url)
    print(result)
    print("-" * 50)
