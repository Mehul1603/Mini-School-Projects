import smtplib
address='ghostrider16me@gmail.com'
password='mehul1995'
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(address,password)

    subject = 'Happy Birthday!'
    body = 'many happy return to you!'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(address,'mehulkasliwal16@gmail.com',msg)