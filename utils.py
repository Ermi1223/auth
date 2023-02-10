from django.core.mail import send_mail
import uuid

def send_activation_email(email, activation_token):
    activation_url = 'http://localhost:8000/api/activate/' + activation_token
    message = f'Please click the following link to activate your account: {activation_url}'
    send_mail('Account activation', message, 'from@example.com', [email], fail_silently=False)


def generate_token():
    return str(uuid.uuid4())
