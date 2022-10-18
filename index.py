from downloader import download
import static_ffmpeg
import sys

static_ffmpeg.add_paths()

if len(sys.argv) < 2:
    print('url is need')
    exit()

download(sys.argv[1])


