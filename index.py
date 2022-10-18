from downloader import download

import sys

if len(sys.argv) < 2:
    print('url is need')
    exit()

download(sys.argv[1])


