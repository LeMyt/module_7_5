import os

#directory = os.getcwd()
directory = '.'
print(os.getcwd())
for root, dirs, files in os.walk(directory):
    for file in files:
        #print(file)
        filetime = os.stat(file).st_mtime
        filesize = os.stat(file).st_size
        print(filetime)