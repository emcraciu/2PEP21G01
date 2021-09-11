import smtplib

message_ = 'Test email message'
username_ = 'pinkiwinkiwinki555'
password_ = '1234pinki'
destination_ = 'example@example.com'
smtp_url = 'imap.gmail.com'


def send_mail_smtp(username, password, message, destination):
    con = smtplib.SMTP_SSL(smtp_url, 465)
    con.ehlo()
    con.login(username, password)
    con.sendmail(username, destination, message)
    con.quit()


if __name__ == '__main__':
    send_mail_smtp(username_, password_, message_, destination_)
