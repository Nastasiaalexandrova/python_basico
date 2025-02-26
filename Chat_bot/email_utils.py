import aiosmtplib
from email.mime.text import MIMEText

# Replace with your email settings
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # Usually 587 for TLS

async def send_email(recipient, subject, body):
    """ Sends an email confirmation to the client. """
    message = MIMEText(body, "plain", "utf-8")
    message["From"] = EMAIL_SENDER
    message["To"] = recipient
    message["Subject"] = subject

    try:
        await aiosmtplib.send(
            message,
            hostname=SMTP_SERVER,
            port=SMTP_PORT,
            username=EMAIL_SENDER,
            password=EMAIL_PASSWORD,
            use_tls=True,
            # use_tls=False,
            start_tls=True,
        )
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")
