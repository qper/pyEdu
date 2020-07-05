from configparser import ConfigParser
from dadata import Dadata
from os import path
from time import strftime as format_time
from tqdm import tqdm
from json import dump, dumps, load, loads

data = {}
current_date_and_time = format_time('%Y-%m-%d-%H-%M-%S')
data_file = f'{current_date_and_time}.json'


file_dir = path.dirname(path.realpath(__file__))
data_dir = f'{file_dir}/data'
assert path.isdir(data_dir), 'Data directory is absent'

config = ConfigParser()
config.read('config.ini')
token = config['CREDENTIALS']['token']
search = Dadata(token)

with open('tax_numbers.txt', 'r') as file:
    tax_numbers_list = file.read().split('\n')

for item in tqdm(tax_numbers_list):
    # find_by_id returns a list
    response = search.find_by_id("party", str(item))
    print(response)
    data.update({f'{item}': response})

print(data)

with open(f'{data_dir}/{data_file}', 'w') as json_file:
    dump(data, json_file)
