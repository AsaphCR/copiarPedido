import requests


class ConsultaAPI:
    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
    
    # def __str__(self):
    #     return f'{json.loads(self.response.content)}'

    def consulta(self, uriAddress, call, param):
        self.uriAddress = uriAddress
        self.headers = {
            'Content-type': 'application/json',
        }
        self.json_data = {
            'call': call,
            'app_key': self.app_key,
            'app_secret': self.app_secret,
            'param': [param],
        }
        self.response = requests.post(f'https://app.omie.com.br/api/v1/{self.uriAddress}', headers=self.headers, json=self.json_data)
        return self.response


# consulta = ConsultaAPI(FTG.get_key(), FTG.get_secret())
# consulta.consulta(
#                 "geral/produtos",
#                 call="ConsultarProduto",
#                 param={
#                     "codigo": "000016238"
#                 }
#             )
# print(consulta)


# 403 - A chave de acesso está inválida ou o aplicativo está suspenso
# 500 - Não existem registros para a página / error Method x not exists / Esta requisição já foi processada ou está sendo processada e você pode tentar novamente às xh