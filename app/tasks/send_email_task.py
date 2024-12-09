from celery import Celery
from smtplib import SMTP
from email.mime.text import MIMEText

celery_app = Celery("tasks", broker="redis://redis:6379/0")

@celery_app.task
def send_email_task(emails: list[str], message: str):
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your-email@example.com"
    smtp_password = "your-password"

    with SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_user, smtp_password)
        for email in emails:
            msg = MIMEText(message, "html")
            msg["Subject"] = "Notification"
            msg["From"] = smtp_user
            msg["To"] = email
            smtp.send_message(msg)
