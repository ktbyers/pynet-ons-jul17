#!/usr/bin/env python
from email_helper import send_mail

def main():
    sender = 'twb@twb-tech.com'
    recipient = 'ktbyersx@gmail.com'
    subject = 'This is a test message.'

    message = '''
Whatever

Whatever

'''

    if send_mail(recipient, subject, message, sender):
        print 'Email notification sent to {}'.format(recipient)
        return True

if __name__ == '__main__':
    main()
