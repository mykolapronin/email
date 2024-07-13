from utils import email_sender


def main():
    list_of_recipients = [
        'mykola.pronin@ukr.net',
    ]
    # cars = ['Audi', 'BMW']

    for res in list_of_recipients:
        params = {
            'recipient_name': 'Sasha',
            'letter_title': 'Welcome',
            'body_content': 'Awesome email',
            'sender_signature': 'Mr',
            'sender_name': res,
            'footer_text': 'Thank you',
            'age': 14,
            # 'cars': cars
        }
        body = email_sender.create_welcome_letter(params)
        email_sender.send_email(
            recipients=list_of_recipients, mail_subject='Head', mail_body=body
        )


main()
#
# if __name__ == '__main__':
#     main()
