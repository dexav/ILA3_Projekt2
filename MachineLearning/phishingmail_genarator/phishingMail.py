import random

# Dummy-Link (dies ist nur eine Übung, keine echte URL)
dummy_link = "http://example.com/fake-payment"

# Nachricht für die Phishing-Mail
message = f"""
Guten Tag,

hier ist die Deutsche Post. Wir möchten Sie darauf hinweisen, dass Sie Ihr Paket, das gestern zugestellt wurde, noch nicht abgeholt haben. 

Um Ihr Paket zu erhalten, müssen Sie innerhalb der nächsten 24 Stunden eine Gebühr von 100.- Euro bezahlen. Klicken Sie dazu auf den folgenden Link, um die Zahlung abzuschließen:

{dummy_link}    

Bitte ignorieren Sie diese Nachricht nicht, da Ihr Paket sonst zurückgesendet wird.

Mit freundlichen Grüßen,
Deutsche Post
"""

# E-Mail-Nachricht speichern
with open("phishing_email.txt", "w") as file:
    file.write(message)

print("Phishing-Nachricht wurde gespeichert.")
