import pandas as pd
import ezodf
import numpy as np

doc = ezodf.opendoc('Lista_Principal.ods')

# convert the first sheet to a pandas.DataFrame
sheet = doc.sheets[0]
df_dict = {}
for i, row in enumerate(sheet.rows()):
    # row is a list of cells
    # assume the header is on the first row
    if i == 0:
        # columns as lists in a dictionary
        df_dict = {cell.value:[] for cell in row}
        # create index for the column headers
        col_index = {j:cell.value for j, cell in enumerate(row)}
        continue
    for j, cell in enumerate(row):
        # use header instead of column index
        df_dict[col_index[j]].append(cell.value)
# and convert to a DataFrame
df = pd.DataFrame(df_dict)

#Filtro para Folha e Senhas
filtro = df[df['Folha']== '002']
senhas = df[df['Folha']== 'Senhas >>>']

if len(filtro.index)>0:
    print ('Senha ','Valor')
    for i in filtro.index:
        linha = df['Linha'][i]
        coluna = df['Coluna'][i]
        for j in list(senhas):
            if j!='Folha' and j!='Linha' and j!='Coluna' and j!=None:
                xsenha = linha + coluna + str(df[j][0]) #senha
                xvalor = df[j][i] #valor
                if xvalor == None:
                    xvalor = ''
                print(xsenha,xvalor)