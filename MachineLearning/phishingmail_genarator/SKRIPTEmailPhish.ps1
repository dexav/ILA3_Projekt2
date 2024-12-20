
$smtpServer = "smtp.gmail.com"  # Für den gmail

# Relativer Pfad zur Datei
$messageFilePath = Join-Path -Path $PSScriptRoot -ChildPath "phishing_email.txt"
Write-Host "Die des Absender muss den Provider Gmail haben."

while ($true) {
    $userEmail = Read-Host -Prompt "Enter your email address"

    $recipientEmail = Read-Host -Prompt "Enter the recipient's email address"

    $password = Read-Host -Prompt "Enter your Gmail password" -AsSecureString

    if (Test-Path $messageFilePath) {
        $messageBody = Get-Content -Path $messageFilePath | Out-String
    } else {
        Write-Output "Die Datei $messageFilePath wurde nicht gefunden."
        break
    }

    # E-Mail Nachricht erstellen
    $message = New-Object system.net.mail.mailmessage
    $message.from = $userEmail
    $message.To.Add($recipientEmail)
    $message.Subject = "Wichtige Mitteilung von der Deutschen Post"
    $message.Body = $messageBody

    # SMTP-Client konfigurieren
    $smtp = New-Object Net.Mail.SmtpClient($smtpServer, 587)
    $smtp.EnableSsl = $true  # SSL für sichere Verbindung aktivieren
    $smtp.Credentials = New-Object System.Net.NetworkCredential($userEmail, $password)

    # E-Mail senden und Fehler abfangen
    try {
        $smtp.Send($message)
        Write-Output "Die Phishing-Mail wurde erfolgreich gesendet."
    } catch {
        Write-Output "Fehler beim Senden der E-Mail: $_"
    }

    # Benutzer fragen, ob er das Programm beenden möchte
    $continue = Read-Host -Prompt "Möchten Sie eine weitere E-Mail senden? (j/n)"
    if ($continue -ne 'j') {
        break  # Schleife beenden
    }
}