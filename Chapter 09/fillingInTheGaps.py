import os, re, shutil

prefixRegex = re.compile(r'spam(\d){3}.txt')

def fillTheGap(path):
    count = 1
    for filename in os.listdir(path):
        if prefixRegex.search(filename):
            if int(filename[4:7]) != count:
                if count > 99:
                    new_file_name = 'spam' + str(count) + '.txt'
                if count > 9:
                    new_file_name = 'spam0' + str(count) + '.txt'
                else:
                    new_file_name = 'spam00' + str(count) + '.txt'
                shutil.move(path + '\\' + filename, path + '\\' + new_file_name)
            count += 1

def insert(path, insert_value):
    files = os.listdir(path)
    for filename in reversed(files):
        if prefixRegex.search(filename):
            id_old = int(filename[4:7])
            id_new = int(insert_value[4:7])
            if id_old >= id_new:
                if id_old > 98:
                    new_file_name = 'spam' + str(id_old + 1) + '.txt'
                if id_old > 8:
                    new_file_name = 'spam0' + str(id_old + 1) + '.txt'
                else:
                    new_file_name = 'spam00' + str(id_old + 1) + '.txt'
                shutil.move(path + '\\' + filename, path + '\\' + new_file_name)
            else:
                temp = open(path + '\\' + insert_value, 'w')
                temp.close()                


path = "C:\\Users\\Laura\\Downloads\\test"
fillTheGap(path)

insert_value = 'spam005.txt'
insert(path, insert_value)