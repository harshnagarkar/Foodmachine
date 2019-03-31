# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("admin@foodmachine.ml")
to_email = Email("hknagark@go.olemiss.edu")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
