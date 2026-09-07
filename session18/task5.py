#Use ChatGPT to generate Python code for a base Notification class and two subclasses: EmailNotification and SMSNotification. Each subclass should have a send() method that prints a message indicating the type of notification sent. Paste the code you received and run it to demonstrate inheritance.
class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")


class SMSNotification(Notification):
    def send(self):
        print("SMS notification sent")


email = EmailNotification()
sms = SMSNotification()

email.send()
sms.send()