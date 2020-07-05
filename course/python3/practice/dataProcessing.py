from json import load as json_load
from os import listdir
from os.path import isfile, isdir, join, dirname, realpath
from pandas import DataFrame, concat
from configparser import ConfigParser

file_dir = dirname(realpath(__file__))
data_dir = f'{file_dir}/data'
assert isdir(data_dir), 'Data directory is absent'


config = ConfigParser()
config.read('config.ini')
token = config['CREDENTIALS']['token']

data_ip = []
data_ul = []
file_list = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

yandex_api_url = 'https://search-maps.yandex.ru/v1/?' \
                 'type=biz&lang=ru_RU&results=1'

def get_yandex_request_str(url, key, text):
    return "{}&apikey={}&text={}".format(url, key, text)

for file in file_list:
    with open('{}/{}'.format(data_dir, file), 'r') as json_file:
        json_object = json_load(json_file)
        line = json_object['items'][0]
        if 'ЮЛ' in line:
            data_ul.append(line['ЮЛ'])
        elif 'ИП' in line:
            data_ip.append(line['ИП'])
        else:
            assert False, 'Unreachable line'

fields = """
Адрес
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
    innfl = item['ИННФЛ']
    name = item['ФИОПолн']

    if 'Адрес' in item:
        adress = item['Адрес']['АдресПолн']
        region = item['Адрес']['КодРегион']
    else:
        adress = ' '
        region = ' '

    text = 'ИНН {} ИП {} {}'.format(
        innfl,
        name,
        adress
    )

    request_str = get_yandex_request_str(yandex_api_url, token, text)
    print(f'Sending request: {request_str}')

    # response = requests.get(request_str)
    #
    # print(response.content)
    # with open(f'yandex_{innfl}.json', 'wb') as json_file:
    #     json_file.write(response.content)
    phone_list = []
    address_from_yandex = ' '
    site_url = ' '
    with open(f'yandex_{innfl}.json', 'r') as json_file:
        json_object = json_load(json_file)
        if json_object['properties']['ResponseMetaData']['SearchResponse']['found'] != 0:
            print(json_object['features'][0]['properties'])
            print(json_object['features'][0]['properties']['name'])
            print(json_object['features'][0]['properties']['CompanyMetaData']['address'])
            # print(json_object['features'][0]['properties']['CompanyMetaData']['url'])
            # print(json_object['features'][0]['properties']['CompanyMetaData']['Phones'])
            if 'Phones' in json_object['features'][0]['properties']['CompanyMetaData']:
                for phone in json_object['features'][0]['properties']['CompanyMetaData']['Phones']:
                    phone_list.append(phone['formatted'])
            address_from_yandex = json_object['features'][0]['properties']['CompanyMetaData']['address']
            if 'url' in json_object['features'][0]['properties']['CompanyMetaData']:
                site_url = json_object['features'][0]['properties']['CompanyMetaData']['url']


    ip_map['{}'.format(item['ИННФЛ'])] = {
        'Регион': region,
        'Адрес': address_from_yandex,
        'Наименование перевозчика': '{} {}'.format('ИП', item['ФИОПолн']),
        'ФИО управляющего': item['ФИОПолн'],
        'Основной ОК ВЭД': f"{item['ОснВидДеят']['Код']} {item['ОснВидДеят']['Текст']}",
        'Url сайта': site_url,
        'Телефон': ', '.join(phone_list),
        'Адрес электронной почты': item['E-mail'] if 'E-mail' in item else "E-mail отсутствует"
    }


for item in data_ul:
    inn = item['ИНН']
    name = item['НаимПолнЮЛ']
    shot_name = item['НаимСокрЮЛ']

    assert '{}'.format(item['ИНН']) not in ul_map
    if 'Руководитель' in item:
        manager = item['Руководитель']['ФИОПолн']
    elif 'УправлОрг' in item:
        # TODO: Уточнить requirements, What we have to do in case when много управляющих
        # assert len(item['УправлОрг']) == 1, item['УправлОрг']
        manager = item['УправлОрг'][0]['НаимСокрЮЛ']
    else:
        manager = " "
    if 'Адрес' in item:
        adress = item['Адрес']['АдресПолн']
        region = item['Адрес']['КодРегион']
    else:
        adress = ' '
        region = ' '

    text = f'ИНН {inn} {shot_name} {adress}'

    request_str = get_yandex_request_str(yandex_api_url, token, text)
    print(f'Sending request: {request_str}')

    # response = requests.get(request_str)
    #
    # print(response.content)
    # with open(f'yandex_{inn}.json', 'wb') as json_file:
    #     json_file.write(response.content)

    phone_list = []
    address_from_yandex = ' '
    site_url = ' '
    with open(f'yandex_{inn}.json', 'r') as json_file:
        json_object = json_load(json_file)
        if json_object['properties']['ResponseMetaData']['SearchResponse']['found'] != 0:
            print(json_object['features'][0]['properties'])
            print(json_object['features'][0]['properties']['name'])
            print(json_object['features'][0]['properties']['CompanyMetaData']['address'])
            # print(json_object['features'][0]['properties']['CompanyMetaData']['url'])
            # print(json_object['features'][0]['properties']['CompanyMetaData']['Phones'])
            if 'Phones' in json_object['features'][0]['properties']['CompanyMetaData']:
                for phone in json_object['features'][0]['properties']['CompanyMetaData']['Phones']:
                    phone_list.append(phone['formatted'])
            address_from_yandex = json_object['features'][0]['properties']['CompanyMetaData']['address']
            if 'url' in json_object['features'][0]['properties']['CompanyMetaData']:
                site_url = json_object['features'][0]['properties']['CompanyMetaData']['url']

    ul_map['{}'.format(item['ИНН'])] = {
    'Регион': region,
    'Адрес': address_from_yandex,
    'Наименование перевозчика': '{}'.format(shot_name),
    'ФИО управляющего': manager,
    'Основной ОК ВЭД': f"{item['ОснВидДеят']['Код']} {item['ОснВидДеят']['Текст']}",
    'Url сайта': site_url,
    'Телефон': ', '.join(phone_list),
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