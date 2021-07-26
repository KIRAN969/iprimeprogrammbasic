import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("969kiran969@gmail.com","Kiran@969")
message="hello good morning"
connection.sendmail("969kiran969@gmail.com","rachapallikirankumar969@gmail.com",message)
print("message sent")
connection.quit()