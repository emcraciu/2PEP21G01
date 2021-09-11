import imaplib

username = 'pinkiwinkiwinki555'
password = '1234pinki'
imap_url = 'imap.gmail.com'
pop_url = 'pop.gmail.com'


def get_mail_imap(username: str, password: str):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(username, password)
    con.select('Inbox')
    result, data = con.search(None, 'UNSEEN')
    for email_number in data[0].split():
        status, message_data = con.fetch(email_number, '(RFC822)')
        yield str(message_data[1], 'utf-8')
    con.logout()


if __name__ == '__main__':
    mails = get_mail_imap(username, password)
    for mail in mails:
        print(mail)
