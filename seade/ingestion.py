import requests
import boto3
import json

class Ingestor:
    def __init__(self, loc, var, year, url, stop_year):
        self.url = url
        self.params = {
            "loc": loc, #cidade
            "var": var, #variável
            "year": year,
        }
        self.stop_year = stop_year

    def get_response(self, **params):
        return requests.get(self.url, params=params)

    def get_data(self, **params):
        return self.get_response(**params).json()

def generate_json_file(start, end, year, file_name):
    data_list = []

    for loc in range(start, end):
        for var in range(start, end):
            url = f"https://api-imp.seade.gov.br/v1/dados/{loc}/{var}/{year}"
            meuingestor = Ingestor(loc, var, year, url, year)
            data = meuingestor.get_data(**meuingestor.params)
            data_list.append(data)
    
    with open(file_name, 'w') as file:
        json.dump(data_list, file)

# Define the values for loc, var, and year
start = 1  # Starting value for loc
end = 500  # Ending value for loc
year = 2010
file_name = 'data.json'

# Generate the JSON file
generate_json_file(loc_start, loc_end, year, file_name)