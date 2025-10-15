import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


LOG = Path("mail.txt")

SMTP_SERVER = os.environ.get("SMTP_SERVER", "localhost")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "1025"))  # debug SMTP
SENDER = os.environ.get("SENDER_EMAIL", "test@example.local")
RECEIVER = os.environ.get("RECEIVER_EMAIL", "test@example.local")

subject = "Test notification"
body = "Test."

msg = MIMEMultipart()
msg["From"] = SENDER
msg["To"] = RECEIVER
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
    server.sendmail(SENDER, [RECEIVER], msg.as_string())
    server.quit()
    LOG.write_text("OK: message sent\n", encoding="utf-8")
    print("Sent (or delivered to local debug SMTP).")
except Exception as e:
    LOG.write_text(f"ERROR: {e}\n", encoding="utf-8")
    print("Error (see mail.txt):", e)
