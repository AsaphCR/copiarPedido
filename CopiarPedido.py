from system.consultaPedido import ConsultaPedido
from system.chavesDeAcesso import FTG, ATAC
from system.criacaoPedido import CriacaoPedido

while True:
    Pedido = ConsultaPedido(FTG.get_key(), FTG.get_secret(), input("Insira o número do pedido: ").strip())
    Resposta = CriacaoPedido(ATAC.get_key(), ATAC.get_secret(), Pedido.pedido)
    print(Resposta.consulta.response.content)
