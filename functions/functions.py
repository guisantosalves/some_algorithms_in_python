# def mensagem(M, default="nenhuma mensagem passada", *args):
#     print(f"gayzao {M}")
#     print(default)
#     print(args)

# print(mensagem("eae gayyy", "eae nene", "iaiaiaiaaiaiiai", "iaiadosfogf"))

## kwargs -> aluno="aloo" -> se transforma em dictionary (chave : valor) -> sendo aluno chave e aloo valor

#args vira uma tupla e já o kwargs vira um dictionary; obrigatoriamente o *args deve estar antes do parâmetro default

def mensagem2(M, *args, default="nenhuma mensagem passada", **kwargs):
    print(f"exemplo: {M}")
    print(default)
    print(args)
    print(kwargs)

print(mensagem2("gui", "guizaodozap", "dalskda", "lucas", "lalalal", default="homem", lilo="amo", mamo="mamim"))