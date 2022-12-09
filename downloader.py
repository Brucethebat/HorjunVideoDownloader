import requests
from bs4 import BeautifulSoup as bs
import subprocess
import platform


class download:
    def __init__(self, url):
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')
        res = soup.find('video', id='example_video_1')
        namefile = soup.find('h5', class_='font-size-21 font-weight-medium text-white').text
        print('name is : ',namefile)
        print('please select quality :')
        count = 1
        qualityes = []
        resolution = []
        for i in res.find_all('source'):
            if i['title'] == 'auto':
                continue
            print(count, '->',i['title'])
            qualityes.append(i)
            resolution.append(i['title'])
            count+=1
        selected = int(input('saylamaly : '))
        if selected > count or selected < 1:
            print('Yalnys sayladynoooooooooow')
            selected = 1
        p = qualityes[selected-1]['src']
        if platform.system() == "Windows":
            cmd = 'ffpb.exe' + ' -i ' + p + ' "' + namefile + '(' + resolution[selected-1] + ')' + '.mp4"'
        else:
            cmd = 'ffpb' + ' -i ' + p + ' "' + namefile + '(' + resolution[selected-1] + ')' + '.mp4"'
        subprocess.run(cmd)