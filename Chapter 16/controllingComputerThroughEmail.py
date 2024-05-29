import subprocess, imapclient, pyzmail, time, datetime

def check_link(email, password, sender, passkey):
    time_now = datetime.datetime.now()
    time_formatted = time_now.strftime('%d-%b-%Y')

    imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
    imapObj.login(email, password)
    imapObj.select_folder('INBOX')
    UIDs = imapObj.search('FROM %s SINCE %s' % (sender, time_formatted))

    links = []

    for mail in UIDs:
        rawMessage = imapObj.fetch([mail], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessage[mail][b'BODY[]'])
        text = message.text_part.get_payload().decode(message.text_part.charset)
        if passkey in text:
            links.append(text[len(passkey) + 2:])
            imapObj.delete_messages(mail)

    imapObj.logout()
    return links


email = input('Enter your email: ')
password = input('Enter your password: ')
sender = 'laura.veerkamp11@gmail.com'
passkey = 'This is your go.'
path_to_qBittorrent = 'C:\\Program Files\\qBittorrent\\qbittorrent.exe'

while True:
    links = check_link(email, password, sender, passkey)
    for link in links:
        subprocess.Popen([path_to_qBittorrent, link])
    time.sleep(60 * 15)
