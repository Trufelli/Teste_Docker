# Bibliotecas importadas (Csv - Manusear CSVs, Sys - Tratar argumentos)
import csv
import sys

# Dicionario contendo a Sigla do Estado, Lista com nome da cidade e nome dos clientes
clientes_por_estado = {'AL': [[],[]],'AP': [[],[]],'AM': [[],[]],'BA': [[],[]],'CE': [[],[]],'DF': [[],[]],'ES': [[],[]],'GO': [[],[]],'MA': [[],[]],'MA': [[],[]],'MT': [[],[]],'MS': [[],[]],'MG': [[],[]],'PA': [[],[]],'PB': [[],[]],'PR': [[],[]],'PE': [[],[]],'PI': [[],[]],
           'RJ': [[],[]],'RN': [[],[]],'RS': [[],[]],'RO': [[],[]],'RR': [[],[]],'SC': [[],[]],'SP': [[],[]],'SE': [[],[]],'TO': [[],[]]} 


# Funcao para ler o arquivo CSV e gravar as informacoes no dicionario
def ler_arquivo_csv(arquivo_csv):
    with open(arquivo_csv) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if row[0] in clientes_por_estado:
                clientes_por_estado[row[0]][0].append(row[1])
                clientes_por_estado[row[0]][1].append(row[2])


# Imprimi os resultados
def imprimi_clientes_por_estado():
    for estado in clientes_por_estado:
        if (len(clientes_por_estado[estado][1])>0):
            print("\nEstado: {} - Quantidade de clientes: {}\n".format(estado,len(clientes_por_estado[estado][1])))

            for cidade_do_cliente in clientes_por_estado[estado][0]:
                print("- Cidade: {} - Cliente: {} ".format(cidade_do_cliente,clientes_por_estado[estado][1][clientes_por_estado[estado][0].index(cidade_do_cliente)]))


if __name__ == '__main__':
    
    try:
        ler_arquivo_csv(sys.argv[1])
        imprimi_clientes_por_estado()

    except:
        print("Nao foi possivel ler o CSV!!!")
