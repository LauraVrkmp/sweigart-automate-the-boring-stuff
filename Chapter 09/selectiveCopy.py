import shutil, os

def selectiveCopy(folder):
    folder = os.path.abspath(folder)

    for folderName, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                if filename.endswith('.pdf'):
                    print('Copying file in ' + folderName + ': ' + filename)
                    shutil.copy(folderName + '\\' + filename, "C:\\Users\\Laura\\OneDrive\\Bureaublad\\programmeren\\sweigart-automate-the-boring-stuff\\Chapter 09\\selectiveCopy")

selectiveCopy("C:\\Users\\Laura\\Downloads")