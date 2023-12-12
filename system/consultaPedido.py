import json, sys
from system.consultaAPIOmie import ConsultaAPI
from system.utilities import *

class ConsultaPedido:
    def __init__(self, app_key, app_secret, numeroPedido) -> None:
        self.consulta = ConsultaAPI(app_key=app_key, app_secret=app_secret)
        self.uriAddress = "produtos/pedido/"
        self.listarPedidos = self.consulta.consulta(self.uriAddress, call="ListarPedidos", param={"registros_por_pagina": 1000, "apenas_importado_api": "N"})
        self.numeroPedido = numeroPedido
        self.pedido = self.__dadosPedido()

    def __dadosPedido(self) -> json:
        self.codigoPedido = self.__buscaPedido(self.numeroPedido)
        self.pedido = self.consulta.consulta(self.uriAddress, call="ConsultarPedido", param={'codigo_pedido': self.codigoPedido if self.codigoPedido else sys.exit()})
        saveJson("pedidoDeVenda", self.pedido)
        return json.loads(self.pedido.content)["pedido_venda_produto"]
    
    def __buscaPedido(self, numeroPedido) -> any:
        self.listaDePedidos = json.loads(self.listarPedidos.content)['pedido_venda_produto']
        for pedido in self.listaDePedidos:
            if pedido['cabecalho']['numero_pedido'] == str(numeroPedido):
                return pedido['cabecalho']['codigo_pedido']
        else:
            return False
