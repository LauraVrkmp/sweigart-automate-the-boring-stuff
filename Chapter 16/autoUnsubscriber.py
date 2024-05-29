import imapclient, pyzmail, bs4, webbrowser

def unsubscribe(email, password):
    imapObj = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
    imapObj.login(email, password)
    imapObj.select_folder('INBOX', readonly=True)
    UIDs = imapObj.search('ALL')

    print(UIDs)

    unsub_links = []

    for mail in UIDs:
        rawMessages = imapObj.fetch([mail], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessages[mail][b'BODY[]'])
        try:
            html = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(html, 'html.parser')
            link_elems = soup.select('a')
            for link_elem in link_elems:
                if 'unsubscribe' in str(link_elem).lower():
                    unsub_links.append(link_elem.get('href'))
        except AttributeError:
            print('Couldn\'t retrieve information for %s' % (mail))
            continue

    imapObj.logout()
    return unsub_links

email = input('Enter your email address: ')
password = input('Enter your password: ')
links = unsubscribe(email, password)

for link in links:
    webbrowser.open(link)

print('Continue in browser to unsubscribe for mails')