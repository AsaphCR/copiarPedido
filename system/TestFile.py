from consultaAPIOmie import ConsultaAPI
from chavesDeAcesso import FTG
import utilities

class ConsultaProduto:
    def __init__(self, app_key, app_secret) -> None:
        self.consulta = ConsultaAPI(app_key=app_key, app_secret=app_secret)
        self.consulta.consulta(uriAddress="geral/produtos/", call="ConsultarProduto", param={"codigo": "000000027"})
        # self.consulta.consulta(uriAddress="geral/contacorrente/", call="ListarContasCorrentes", param={  "pagina": 1, "registros_por_pagina": 100,})
        utilities.saveJson("produto27Matriz", self.consulta.response)


ConsultaProduto(FTG.get_key(), FTG.get_secret())
