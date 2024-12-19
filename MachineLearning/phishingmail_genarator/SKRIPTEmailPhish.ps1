# SMTP-Server-Informationen
$smtpServer = "smtp.gmail.com"  # Ersetze dies, falls du einen anderen Provider nutzt
# Prompt the user for their email address
$userEmail = Read-Host -Prompt "Enter your email address"

# Prompt the user for the recipient's email address
$recipientEmail = Read-Host -Prompt "Enter the recipient's email address"

# Prompt the user for their Gmail password securely
$password = Read-Host -Prompt "Enter your Gmail password" -AsSecureString

# Convert the secure string to plain text (if necessary, but be cautious with this)
# $plainPassword = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))

# Now you can use $userEmail, $recipientEmail, and $password in your email sending logic
# Inhalt der Phishing-Mail aus der Python-Datei lesen
$messageBody = Get-Content -Path "C:\Users\xnurs\OneDrive\Desktop\IMS\BBB\Lernatelier\3.Jahr\Projekt2\ILA3-Proj2\phishing_email.txt" | Out-String

# E-Mail Nachricht erstellen
$message = New-Object system.net.mail.mailmessage
$message.from = $smtpFrom
$message.To.Add($smtpTo)
$message.Subject = "Wichtige Mitteilung von der Deutschen Post"
$message.Body = $messageBody

# SMTP-Client konfigurieren
$smtp = New-Object Net.Mail.SmtpClient($smtpServer, 587)
$smtp.EnableSsl = $true  # SSL für sichere Verbindung aktivieren
$smtp.Credentials = New-Object System.Net.NetworkCredential($smtpUsername, $smtpPassword)

# E-Mail senden und Fehler abfangen
try {
    $smtp.Send($message)
    Write-Output "Die Phishing-Mail wurde erfolgreich gesendet."
} catch {
    Write-Output "Fehler beim Senden der E-Mail: $_"
}
# SMTP-Server-Informationen
$smtpServer = "smtp.gmail.com"  # Ersetze dies, falls du einen anderen Provider nutzt

# Prompt the user for their email address
$userEmail = Read-Host -Prompt "Enter your email address"

# Prompt the user for the recipient's email address
$recipientEmail = Read-Host -Prompt "Enter the recipient's email address"

# Prompt the user for their Gmail password securely
$password = Read-Host -Prompt "Enter your Gmail password" -AsSecureString

# Inhalt der Phishing-Mail aus der Python-Datei lesen
$messageBody = Get-Content -Path "C:\Users\xnurs\OneDrive\Desktop\IMS\BBB\Lernatelier\3.Jahr\Projekt2\ILA3-Proj2\phishing_email.txt" | Out-String

# E-Mail Nachricht erstellen
$message = New-Object system.net.mail.mailmessage
$message.From = $userEmail
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