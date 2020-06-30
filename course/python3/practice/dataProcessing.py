from json import load as json_load
from os import listdir
from os.path import isfile, join
from pandas import DataFrame, concat


data_ip = []
data_ul = []
path_to_local_json_files = '/work/git/pyEdu/course/python3/practice/set_one'
file_list = [f for f in listdir(path_to_local_json_files) if isfile(join(path_to_local_json_files, f))]

for file in file_list:
    with open('{}/{}'.format(path_to_local_json_files, file), 'r') as json_file:
        json_object = json_load(json_file)
        line = json_object['items'][0]
        if 'ЮЛ' in line:
            data_ul.append(line['ЮЛ'])
        elif 'ИП' in line:
            data_ip.append(line['ИП'])
        else:
            assert False, 'Unreachable line'

fields = """
Наименование перевозчика
ФИО управляющего
Основной ОК ВЭД
Url сайта
Телефон
Адрес электронной почты
"""

# print(data_ip)
# print(data_ul)

ip_map = {}
ul_map = {}

some_set = set()

for item in data_ip:
    assert '{}'.format(item['ИННФЛ']) not in ip_map
    ip_map['{}'.format(item['ИННФЛ'])] = {
        'Наименование перевозчика': '{} {}'.format('ИП', item['ФИОПолн']),
        'ФИО управляющего': item['ФИОПолн'],
        'Основной ОК ВЭД': f"{item['ОснВидДеят']['Код']} {item['ОснВидДеят']['Текст']}",
        'Url сайта': item['Url'] if 'Url' in item else "Url сайта отсутствует",
        'Телефон': item['НомТел'] if 'НомТел' in item else "Телефон отсутствует",
        'Адрес электронной почты': item['E-mail'] if 'E-mail' in item else "E-mail отсутствует"
    }


for item in data_ul:
    assert '{}'.format(item['ИНН']) not in ul_map
    if 'Руководитель' in item:
        manager = item['Руководитель']['ФИОПолн']
    elif 'УправлОрг' in item:
        # TODO: Уточнить requirements, What we have to do in case when много управляющих
        # assert len(item['УправлОрг']) == 1, item['УправлОрг']
        manager = item['УправлОрг'][0]['НаимСокрЮЛ']
    else:
        manager = "Руководитель отсутствует"
    ul_map['{}'.format(item['ИНН'])] = {
    'Наименование перевозчика': '{}'.format(item['НаимПолнЮЛ']),
    'ФИО управляющего': manager,
    'Основной ОК ВЭД': f"{item['ОснВидДеят']['Код']} {item['ОснВидДеят']['Текст']}",
    'Url сайта': item['Url'] if 'Url' in item else "Url сайта отсутствует",
    'Телефон': item['НомТел'] if 'НомТел' in item else "Телефон отсутствует",
    'Адрес электронной почты': item['E-mail'] if 'E-mail' in item else "E-mail отсутствует"
}

# print(ip_map)
# print(ul_map)

df_ip = DataFrame(ip_map).T
df_ul = DataFrame(ul_map).T

# df_ip.to_excel('df_ip.xlsx')
# df_ul.to_excel('df_ul.xlsx')

df_common = concat([df_ip, df_ul])
df_common.to_excel('df_common.xlsx')