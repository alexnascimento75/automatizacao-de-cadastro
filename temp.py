import pandas

tabela = pandas.read_csv('alunos.csv')


for linha in tabela.index:
    nome = tabela.loc[linha, 'Nome']
    email = tabela.loc[linha, 'Email']
    endereco = tabela.loc[linha, 'Endereco']
    telefone = tabela.loc[linha, 'Telefone']
   

    