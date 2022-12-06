import gensim.downloader as api
import re
import numpy
import time
import pandas as pd
import csv


pd.options.display.max_rows = 9999

identificadoresCsv = pd.read_csv('Identifiers.csv')
inicio = time.time()
w2v_model = api.load("fasttext-wiki-news-subwords-300")


def camelSplit(identifier):
    matches = re.finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$|_)', identifier)
    return [m.group(0).replace("_", "") for m in matches]


# calcula a distancia/similaridade entre todas as palavras de uma classe com todas as palavras de atributos que pertencem a ela
with open('Score-Media3WordEmbedding.csv', mode='w') as csv_file:

    fieldnames = ['nome_identificador', 'nome_da_classe',
                  'score_relacao', 'nome_arquivo', 'media_top3_atributo']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    listaValor = []

    for row in identificadoresCsv.iterrows():

        csvEntries = row[1]

        nomeClasse = csvEntries.nomeClasse
        nomeIdentificador = csvEntries.nome

        classeCamel = camelSplit(nomeClasse)

        for classeCamelIterator in classeCamel:

            classeCamelIterator = classeCamelIterator.lower()

            atributosCamel = camelSplit(nomeIdentificador)

            for atributosCamelIterator in atributosCamel:

                atributosCamelIterator = atributosCamelIterator.lower()

                try:
                    valorSimilaridade = w2v_model.similarity(
                        atributosCamelIterator, classeCamelIterator)

                except KeyError:
                    valorSimilaridade = -1

                try:
                    vetorAtributosSimilares = w2v_model.most_similar(
                        atributosCamelIterator, None, 3)
                    for palavrasSimilares in vetorAtributosSimilares:
                        listaValor.append(palavrasSimilares[1])
                        # print(palavrasSimilares[1])

                    mediaValor = numpy.mean(listaValor)
                    listaValor = []

                except KeyError:
                    mediaValor = -1

                writer.writerow({'nome_identificador': atributosCamelIterator, 'nome_da_classe': classeCamelIterator,
                                'score_relacao': valorSimilaridade, 'nome_arquivo': '', 'media_top3_atributo': mediaValor})


fim = time.time()
print(fim-inicio)
