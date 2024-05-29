import os

def traverseFileSystem(path):
    path = os.path.abspath(path)
    
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if os.path.getsize(folderName + '\\' + filename) > 100_000_000:
                print('Path: ' + folderName + '\nFilename: ' + filename + \
                      '\nSize: ' + str(os.path.getsize(folderName + '\\' + filename)))

traverseFileSystem("C:\\Users\\Laura\\Downloads")