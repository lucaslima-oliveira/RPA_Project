import pandas as pd

from pdf_create import cria_certificado

input_excel = r'arquives/input certificado.xlsx'

df_excel = pd.read_excel(input_excel)

for index, row in df_excel.iterrows():

    cria_certificado(row['nome'], row['cpf'],row['curso'],'Universidade Federal do Amazonas')