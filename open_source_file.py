import os
import pyperclip
import urllib.parse

def open_source_file(content):
    # open source code [start] reference: https://datatofish.com/command-prompt-python/

    lang_sequence = [0, 0, 0, 0, 0]

    lang_type = [
        ['en', 'tc', 'sc'],
        ['english', 'tc_chi', 'sc_chi'],
        ['eng', 'chi', 'sc'],
        ['english', 'chinese', 'sc']
    ]

    for iindex, i in enumerate(lang_type):
        for jindex, j in enumerate(i):
            k = '/' + j + '/'
            if content.find(k) != -1:
                lang_sequence[0] = jindex
                lang_sequence[2] = jindex
                if jindex == 0:
                    lang_sequence[1] = 1
                    lang_sequence[3] = 2
                elif jindex == 1:
                    lang_sequence[1] = 2
                    lang_sequence[3] = 0
                elif jindex == 2:
                    lang_sequence[1] = 1
                    lang_sequence[3] = 0
                lang_sequence[4] = iindex
                break

    url_head = {
        'https://uat1.netsoft.net': '\\\\192.168.1.4\\common_website',
        'https://srpa.netsoft.net': '\\\\192.168.1.4\\common_website\\srpa',
        'file:///C:/Users/Raymond/Desktop': 'C:\\Users\\Raymond\\Desktop',
        'http://localhost': 'E:\\common_website'
    }

    for head in url_head:
        if content.startswith(head):
            string = content
            string = string.replace(head, url_head[head])
            string = string.replace('/', '\\')

            for i in string.split('\n'):
                i = urllib.parse.unquote(i)
                print(i)
                os.system('cmd /c "{} & {} & {}"'.format(i, i.replace(
                    lang_type[lang_sequence[4]][lang_sequence[0]],
                    lang_type[lang_sequence[4]][lang_sequence[1]]), i.replace(
                    lang_type[lang_sequence[4]][lang_sequence[2]],
                    lang_type[lang_sequence[4]][lang_sequence[3]])))
            break
    # open source code [end]

open_source_file(pyperclip.paste())
