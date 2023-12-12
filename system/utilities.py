import os, json

def criarDiretorio(directoryName) -> None:
    try:
        os.mkdir(directoryName)
    except:
        pass


def saveJson(arquivo, objjson) -> None:
    criarDiretorio("json")
    with open(f"json/{arquivo}.json", "w") as file:
        json.dump(json.loads(objjson.content), file, indent=4)


# def tinput(msg) -> str:
#     string = input(msg)
#     try:
#         int(string.strip())
#     except:
#         tinput("Dados inválidos", msg)