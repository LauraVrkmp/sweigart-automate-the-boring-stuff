from PIL import Image
import os, logging, traceback

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotofiles = 0
    numNonPhotoFiles = 0

    for filename in filenames:
        lower_filename = filename.lower()
        if not (lower_filename.endswith('.png') or lower_filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue
        
        try:
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size
            if (width > 500 and height > 500):
                numPhotofiles += 1
            else:
                numNonPhotoFiles += 1
        except Exception as e:
            logging.error(traceback.format_exc())
    
    if numPhotofiles > numNonPhotoFiles:
        print('Photos: ' + str(numPhotofiles))
        print('Non-photos: ' + str(numNonPhotoFiles))
        print(foldername)