from app.tasks.send_email_task import send_email_task
from app.repository.user_repository import UserRepository

class EmailService:
    def __init__(self):
        self.user_repo = UserRepository()

    def send_email_task(self, email_data):
        users = self.user_repo.get_all_users()
        emails = [user.email for user in users if user.id in email_data.users]
        send_email_task.delay(emails, email_data.message)
