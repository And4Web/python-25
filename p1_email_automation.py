import smtplib

to = input("Enter the receiver's email address: \n")
message = input("Enter your message: \n")

def send_mail(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("andpmedia1", "password2457")
    server.sendmail("andpmedia1", to, message)
    server.close()

send_mail(to, message)