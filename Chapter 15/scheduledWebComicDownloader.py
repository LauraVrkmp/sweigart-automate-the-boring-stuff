import datetime, os, bs4, requests, sys, threading

path = 'C:\\Users\\Laura\\OneDrive\\Bureaublad\\Comics\\'
last_checked_file = 'last_checked.txt'

def checkLeftHandToons(lastSrc):
    url = 'https://lefthandedtoons.com'
    selector = '.comicimage'
    new_src_url, soup, i = SourceCollector(url, selector, 0)
    comicSrc = new_src_url
    while comicSrc != lastSrc:
        print('Downloading image %s...' % (comicSrc))
        res = requests.get(comicSrc)
        res.raise_for_status()
        imageFile = open(os.path.join(path, os.path.basename(comicSrc)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prev_button = soup.select('.prev a')
        prev_button = prev_button[0].get('href')
        prev_page = requests.get(url + prev_button)
        prev_page.raise_for_status()
        comicSrc, soup, i = SourceCollector(url + prev_button, selector, 0)

    print('Done.')
    return new_src_url


def checkSavageChickens(lastSrc):
    url = 'https://www.savagechickens.com'
    selector = '.entry_content img'
    i = 0
    new_src_url, soup, j = SourceCollector(url, selector, i)
    comicSrc = new_src_url
    while comicSrc != lastSrc and i < j:
        print('Downloading image %s...' % (comicSrc))
        res = requests.get(comicSrc)
        res.raise_for_status()
        comicSrc, soup, j = SourceCollector(url, selector, i)
        imageFile = open(os.path.join(path, os.path.basename(comicSrc)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        i += 1
        if i == j:
            prev_button = soup.select('.previous-entries')
            prev_button = prev_button[0].find('a')
            prev_button = prev_button['href']
            prev_page = requests.get(prev_button)
            prev_page.raise_for_status()
            url = prev_button
            i = 0

    print('Done.')
    return new_src_url


def SourceCollector(url, selector, i):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='lxml')
    comicElem = soup.select(selector)
    if comicElem == []:
        print('Could not find comic image.')
        sys.exit()
    else:
        return comicElem[i].get('src'), soup, len(comicElem)


if not os.path.exists(path + last_checked_file):
    with open(path + last_checked_file, 'w') as file:
        date = datetime.datetime.now()
        left_handed_toons_src = \
        'http://www.lefthandedtoons.com/toons/drew_months.gif'
        savage_chickens_src = \
        'https://www.savagechickens.com/wp-content/uploads/chickengodzillavskong.jpg'
        file.write(str(date) + '\n' + left_handed_toons_src + '\n' + 
                   savage_chickens_src + '\n')
else:
    with open(path + last_checked_file, 'r') as file:
        lines = file.readlines()
        date = lines[0][:-1]
        left_handed_toons_src = lines[1][:-1]
        savage_chickens_src = lines[2][:-1]


def run_checkLeftHandToons():
    global new_left_handed_toons_src
    new_left_handed_toons_src = checkLeftHandToons(left_handed_toons_src)

def run_checkSavageChickens():
    global new_savage_chickens_src
    new_savage_chickens_src = checkSavageChickens(savage_chickens_src)


thread1 = threading.Thread(target=run_checkLeftHandToons)
thread2 = threading.Thread(target=run_checkSavageChickens)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

with open(path + last_checked_file, 'w') as file:
    date = datetime.datetime.now()
    left_handed_toons_src = new_left_handed_toons_src
    savage_chickens_src = new_savage_chickens_src
    file.write(str(date) + '\n' + left_handed_toons_src + '\n' + 
               savage_chickens_src + '\n')
