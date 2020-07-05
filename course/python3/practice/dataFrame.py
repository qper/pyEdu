from os import listdir
from os.path import isfile, isdir, join, dirname, realpath
from json import load as json_load
from pandas import DataFrame


file_dir = dirname(realpath(__file__))
data_dir = f'{file_dir}/data'
assert isdir(data_dir), 'Data directory is absent'

data_ul = []
data_ip = []

file_list = [f for f in listdir(data_dir) if isfile(join(data_dir, f))]

for file in file_list:
    with open('{}/{}'.format(data_dir, file), 'r') as json_file:
        json_object = json_load(json_file)
        if 'ЮЛ' in json_object['items'][0]:
            data_ul.append(json_object['items'][0]['ЮЛ'])
        elif 'ИП' in json_object['items'][0]:
            data_ip.append(json_object['items'][0]['ИП'])
        else:
            raise KeyError

df_ul = DataFrame(data_ul)
df_ip = DataFrame(data_ip)
