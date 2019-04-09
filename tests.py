# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *


def emails(Emailuser):
	sg = sendgrid.SendGridAPIClient(apikey='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')
	from_email = Email("admin@foodmachine.ml")
	to_email = Email(Emailuser)
	subject = "Account registration at food machine"
	content = Content("text/plain", "Hi, \n Thanks for join  food machine")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	print(response.body)
	print(response.headers)
