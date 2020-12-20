
import os
from collections import defaultdict

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



def create_directories():

    count_dict = defaultdict(int)

    for f in files:
        for e in extensions:
            if f.endswith('.' + e):
                count_dict[e] += 1
    for ext, count in count_dict.items():
        if count > 0:
            try:
                os.mkdir(ext)
                print('Directory %s created' % ext)
            except FileExistsError:
                print('Directory %s already exists, skipping' % ext)


def move_files():
    for f in files:
        for e in extensions:
            if f.endswith('.' + e):
                os.rename(f, e + '/' + f)
                print('Successfully moved file %s to directory %s' % ((f,e)))

files = os.listdir()
print('Found %s files' % len(files))

ans = input('Create directories? (y/n)\n')
if ans.lower() == 'y': create_directories() 

ans = input('Move files into directories? (y/n)\n')
if ans.lower() == 'y': move_files()
