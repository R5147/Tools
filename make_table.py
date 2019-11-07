from bs4 import BeautifulSoup
import pyperclip

html = pyperclip.paste()

def filter_td(string):
    new_string = string.split('\n')
    new_line = '									'
    next_line = '								'
    new_content = ''

    if len(new_string) != 1:
        for index, i in enumerate(new_string):
            if i != '':
                if index == 0:
                    new_content += '\n' + new_line + i + '<br>\n'
                elif index != len(new_string) - 1:
                    new_content += new_line + i + '<br>\n'
                else:
                    new_content += new_line + i + '\n' + next_line
    else:
        new_content = string
    return new_content

soup = BeautifulSoup(html, 'html.parser')
tables = soup.find_all('table')

new_table_content = ''
base_line = 5
table_line = '\t'*base_line
thead_tbody_line = '\t'*(base_line+1)
tr_line = '\t'*(base_line+1+1)
th_td_line = '\t'*(base_line+1+1+1)



for table in tables:
    print(table_line+'<table class="data_table">')
    new_table_content += table_line+'<table class="data_table">\n'

    trs = table.find_all('tr')

    for tr_index, tr in enumerate(trs):
        ths = tr.find_all('th')
        tds = tr.find_all('td')
        if tr_index == 0:
            if ths:
                print(thead_tbody_line+'<thead>')
                new_table_content += thead_tbody_line+'<thead>\n'
                print(tr_line+'<tr>')
                new_table_content += tr_line + '<tr>\n'
            for th in ths:
                th_text = th.text.strip()
                print(th_td_line+'<th>'+th_text+'</th>')
                new_table_content += th_td_line+'<th>'+th_text+'</th>\n'
            if ths:
                print(tr_line+'</tr>')
                new_table_content += tr_line+'</tr>\n'
                print(thead_tbody_line+'</thead>')
                new_table_content += thead_tbody_line+'</thead>\n'
            print(thead_tbody_line+'<tbody>')
            new_table_content += thead_tbody_line+'<tbody>\n'

        if tds:
            print(tr_line+'<tr>')
            new_table_content += tr_line+'<tr>\n'
            for td in tds:
                td_text = td.text.strip()
                print(th_td_line+'<td>'+filter_td(td_text)+'</td>')
                new_table_content += th_td_line+'<td>'+filter_td(td_text)+'</td>\n'
            print(tr_line+'</tr>')
            new_table_content += tr_line+'</tr>\n'

    print(thead_tbody_line+'</tbody>')
    new_table_content += thead_tbody_line+'</tbody>\n'
    print(table_line+'</table>')
    new_table_content += table_line+'</table>\n\n'

    print('=======================================')

pyperclip.copy(new_table_content)
