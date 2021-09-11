import poplib

username_ = 'pinkiwinkiwinki555'
password_ = '1234pinki'
pop_url = 'pop.googlemail.com'


def get_mail_pop(username: str, password: str):
    con = poplib.POP3_SSL(pop_url)
    con.user(username)
    con.pass_(password)
    for email_number in range(1, len(con.list()[1]) + 1):
        for msg in con.retr(email_number)[1]:
            yield msg
    con.quit()


if __name__ == '__main__':
    mails = get_mail_pop(username_, password_)
    for mail in mails:
        print(mail)
