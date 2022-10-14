import requests 
import pandas as pd 

def consumption_api_bcentral(link) -> pd.DataFrame:
    req = requests.get(link)
    info = req.json()
    data = pd.DataFrame(info['value'])
    return data 


def consumption_api_bcentral_from_indice(percorrer_indice) -> pd.DataFrame:
    data = pd.DataFrame()
    while True:
        link=f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top={percorrer_indice}&$skip=0&$orderby=Data%20desc&$format=json'
        req = requests.get(link)
        info = req.json()
        dataframe = pd.DataFrame(info['value'])
        if len(info['value']) < 1:
            break
        data = pd.concat([data,dataframe])
        percorrer_indice += 10000

    return data