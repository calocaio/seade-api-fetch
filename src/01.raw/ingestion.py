import requests
import boto3
import json
class Ingestor:
    def __init__(self, loc, var, year, url, stop_year):
        self.url = url
        self.params = {
            "loc": loc,
            "var": var,
            "year": year,
        }
        self.stop_year = stop_year

    def get_response(self, **params):
        return requests.get(self.url, params=params)

    def get_data(self, **params):
        return self.get_response(**params).json()

def generate_json_file(loc_start, loc_end, year, file_name):
    data_list = []

    for loc in range(loc_start, loc_end):
            url = f"https://api-imp.seade.gov.br/v1/dados/{loc}/0/{year}"
            meuingestor = Ingestor(loc, var, year, url, year)
            data = meuingestor.get_data(**meuingestor.params)
            data_list.append(data)
    
    with open(file_name, 'w') as file:
        json.dump(data_list, file)

# variáveis de loc(id da cidade), var(id da variável), e ano
loc_start = 1 
loc_end = 645
var= 0
year = 2020
file_name = 'dados_sp2020.json'


generate_json_file(loc_start, loc_end, year, file_name)