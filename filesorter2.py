
import os
from collections import defaultdict

extensions = [
    'csv',
    'doc',
    'docx',
    'exe',
	'gif',
    'html',
	'jfif',
    'jpeg',
    'jpg',
    'mkv',
    'mp3',
    'mp4',
    'msi',
	'nef',
	'pgn',
    'png',
    'pdf',
	'psd',
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
    num_files_moved = 0
    for f in files:
        for e in extensions:
            if f.lower().endswith('.' + e):
                os.rename(f, e + '/' + f)
                num_files_moved += 1
                print('Successfully moved file %s to directory %s' % ((f,e)))
    return num_files_moved

files = os.listdir()
print('Found %s files' % len(files))

ans = input('Create directories? (y/n)\n')
if ans.lower() == 'y': create_directories() 

ans = input('Move files into directories? (y/n)\n')
if ans.lower() == 'y':
    total_files_moved = move_files()

input('Finished moving %s files!' % total_files_moved)