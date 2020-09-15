from bs4 import BeautifulSoup as soup
import re
# Pega o arquivo excel(tabela html na verdade) baixado do SGTI e transforma em uma list de dictionaries


def file_to_list(file_name):
    # tst = re.search('Delegatarios', file_name)

    f = open(f'C:\\Users\\sandr\\Downloads\\{file_name}', 'r')
    raw_file = f.readline()

    file = soup(raw_file, 'html.parser').table

    h, [_, *d] = [i.text for i in file.tr.find_all(
        'th')], [[i.text for i in b.find_all('td')] for b in file.find_all('tr')]

    result = [dict(zip(h, i)) for i in d]

    print('ftl', result[0])
    return result


# file_to_list('C:\\Users\\sandr\\Downloads\\Delegatarios.xls')
