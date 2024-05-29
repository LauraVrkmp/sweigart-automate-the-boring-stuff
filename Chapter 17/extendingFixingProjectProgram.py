# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open('images\\%s' % (LOGO_FILENAME))
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('images\\.'):
    lower_filename = filename.lower()
    if not (lower_filename.endswith('.png') or lower_filename.endswith('.jpg') \
            or lower_filename.endswith('.gif') or lower_filename.endswith('.bmp')) \
    or filename == LOGO_FILENAME:
        continue        # skip non-image files and the logo file itself

    im = Image.open('images\\%s' % (filename))
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
    
    # Add the logo.
    if width >= 2 * logoWidth and height >= 2 * logoHeight:
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        # Save changes.
        im.save(os.path.join('withLogo', filename))
    else:
        print('This image is not large enough for the logo.')