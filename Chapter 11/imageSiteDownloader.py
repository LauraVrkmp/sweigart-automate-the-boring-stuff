"""Download jpg/png images from Imgur that match a user's search term(s)."""

import os, requests, bs4

def image_downloader(extension):
    """Search for and download all images of the argument type from Imgur."""
    url = 'https://www.flickr.com/search/?text=' + search
    os.makedirs('flickr', exist_ok=True)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    image_elem = soup.select('.photo-list-photo-container')

    for i, image in enumerate(image_elem):
        # Convert image URL from thumbnail size to fullsize version
        image_elem_string = str(image_elem[i])
        index_src = image_elem_string.find('src')
        index_jpg = image_elem_string.find('jpg')
        image_elem_string = image_elem_string[index_src+5:index_jpg+3]
   
        image_url = 'https:' + image_elem_string

        print('Downloading image {}'.format(image_url))
        res = requests.get(image_url)
        res.raise_for_status()
        image_file = open(os.path.join('flickr',
                                        os.path.basename(image_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    return len(image_elem)


search = input('Enter desired search term(s): ')
downloaded = image_downloader('jpg')

if downloaded == 0:
    print('No images found.')

else:
    print('All ' + str(downloaded) + ' files successfully downloaded.')