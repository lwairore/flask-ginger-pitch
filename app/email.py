from flask_mail import Message
from flask import render_template
from . import mail
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def mail_message(subject, to, **kwargs):
    sender_email = os.environ.get("SENDGRID_MAIL_USERNAME")
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

    subject = subject
    message = "Hi there,\nThanks for signing up to keep in touch with Ginger-Pitch family.From now on, you'll get regular updates on the best pitch practices. \nIn the meantime, check out communities best to offer pitches. Here's to the start of a healthy digital relationship.\nCheers,\nGinger Pitch"
    message = Mail(
        from_email=sender_email,
        to_emails=to,
        subject=subject,
        html_content=message
    )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    return response