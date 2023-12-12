from system.consultaAPIOmie import ConsultaAPI
from datetime import datetime, date


class CriacaoPedido:
    def __init__(self, app_key, app_secret, pedidoOriginal) -> None:
        self.pedidoOriginal = pedidoOriginal
        self.consulta = ConsultaAPI(app_key=app_key, app_secret=app_secret)
        self.__criarListaItens()
        self.__conferirItens()
        self.consulta.consulta(uriAddress="produtos/pedido/", call="IncluirPedido", param=
            {
                "cabecalho": {
                    "codigo_cliente": 3489132908,
                    "codigo_pedido_integracao": f"{pedidoOriginal["cabecalho"]["numero_pedido"]:0>9}",
                    "data_previsao": f"{date.strftime(datetime.today(), "%d/%m/%Y")}"
                },
                "det": self.itens,
                "frete": {
                    "modalidade": "3"
                },
                "informacoes_adicionais": {
                    "codigo_categoria": pedidoOriginal["informacoes_adicionais"]["codigo_categoria"],
                    "codigo_conta_corrente": 3489125920,
                    "consumidor_final": "N",
                    "enviar_email": "N"
                }
            }
        )
    
    def __conferirItens(self):
        for item in self.itens:
            if item["ide"]["codigo_item_integracao"] == "":
                item["ide"]["codigo_item_integracao"] = item["produto"]["codigo"]

    def __criarListaItens(self):
        self.itens = []
        itemAux = {"ide": {}, "produto": {}}
        for item in self.pedidoOriginal["det"]:
            itemAux["ide"]["codigo_item_integracao"] = item["ide"]["codigo_item_integracao"]
            itemAux["produto"]["cfop"] = item["produto"]["cfop"]
            itemAux["produto"]["codigo_produto_integracao"] = item["produto"]["codigo_produto_integracao"]
            itemAux["produto"]["quantidade"] = item["produto"]["quantidade"]
            itemAux["produto"]["valor_unitario"] = item["produto"]["valor_unitario"]
            self.itens.append(itemAux)
