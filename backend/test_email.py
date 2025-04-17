import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "thedesignerfemi@gmail.com"
EMAIL_PASSWORD = "cuwu dmni kqgs wlob"
TO_EMAIL = "thedesignerfemi@gmail.com"

def send_test_email():
    print("Sending test email...")

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL
    msg["Subject"] = "🚨 TEST — Email System Working!"

    body = "✅ This is a test email from your scraper system.\nEverything is connected correctly."
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("📬 Email sent successfully!")

if __name__ == "__main__":
    send_test_email()