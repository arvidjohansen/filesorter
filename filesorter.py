
import os

from pprint import pprint as p 

p(dir(os))

extensions = [
    'csv',
    'doc',
    'docx',
    'exe',
    'html',
    'jpeg',
    'jpg',
    'mkv',
    'mp3',
    'mp4',
    'msi',
    'png',
    'pdf',
    'pptx',
    'svg',
    'torrent',
    'txt',
    'webm',
    'wotreplay',
    'xls',
    'xlsx',
    'zip',

]

p(os.listdir())

files = os.listdir()

for ext in extensions:
    try:
        os.mkdir(ext)
        print("Created directory for %s" % ext)
    except FileExistsError:
        print("Directory %s already exists, skipping" % ext)


for f in files:
    for e in extensions:
        #print("File %s ends with %s" % ((f,e)))
        if f.endswith('.'+e):
            os.rename(f,e+'/'+f)
            print("Successfully moved file %s to directory %s" % ((f,e)))