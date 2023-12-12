import consultaAPIOmie, openpyxl, time
from chavesDeAcesso import FTG

wb = openpyxl.load_workbook(r"C:\Users\asaph\Downloads\vendas_e_nf-e_390402700771845.xlsx", data_only=True)
print("Vai carregar")
ws = wb['vendas_e_nf-e_390402700771845']
print("Carregou")
consulta = consultaAPIOmie.ConsultaAPI(FTG.get_key(), FTG.get_secret())
for row in ws.iter_rows(min_col=3, max_col=3, min_row=2):
    while True:
        print("LOOP \O/")
        alteraProduto = consulta.consulta("geral/produtos/", "AlterarProduto", {"codigo": row[0].value, "codigo_produto_integracao": row[0].value})
        print(alteraProduto.status_code, alteraProduto.content)
        if alteraProduto.status_code == 425:
            print("Temos um problema, Watson")
            time.sleep(20)
        else:
            break
    with open("log.txt", "a") as file:
        file.write(f'Código: {row[0].value} - cIntegracao: {row[0].value} - Status {alteraProduto.status_code}: {alteraProduto.content}\n')
    del alteraProduto
