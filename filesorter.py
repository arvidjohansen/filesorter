
import os
from collections import defaultdict 
from pprint import pprint as p

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

count_dict = defaultdict(int)
def create_directories():
    files = os.listdir()
    for f in files:
        for e in extensions:
            if f.endswith('.' + e):
                count_dict[e] += 1
    for ext, count in count_dict.items():
        if count > 0:
            try:
                os.mkdir(ext)
                print("Created directory for %s" % ext)
            except FileExistsError:
                print("Directory %s already exists, skipping" % ext)
create_directories()



p(count_dict)


files = os.listdir()


def move_files():
    for f in files:
        for e in extensions:
            if f.endswith('.'+e):
                os.rename(f,e+'/'+f)
                print("Successfully moved file %s to directory %s" % ((f,e)))

ans = input("Moving files into directories. Continue? (y/n)\n")
if ans.lower() == 'y':
    move_files()
else:
    print("Exiting...")