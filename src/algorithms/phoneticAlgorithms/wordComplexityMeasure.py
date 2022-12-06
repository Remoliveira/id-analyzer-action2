from wcm import wcm

import nltk
import pandas as pd
import csv
import re

nltk.download('cmudict')

identificadoresCsv = pd.read_csv('Identifiers.csv')


def camelSplit(identifier):
    matches = re.finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$|_)', identifier)
    return [m.group(0).replace("_", "") for m in matches]


arpabet = nltk.corpus.cmudict.dict()


fieldnames = ['nome_projeto', 'nome_identificador',
              'nome_classe', 'posicao_identificador', 'score']

with open('wcmSeparetedMean.csv', 'w') as file:

    writer = csv.writer(file)
    writer.writerows([fieldnames])

    # TIRAR NOMES EM MAIUSCULO
    # tabelas dos resultados
    for row in identificadoresCsv.iterrows():

        csvEntries = row[1]

        nomeId = csvEntries.nome
        tipoId = csvEntries.tipo
        posicao = csvEntries.posicao
        projeto = 'projeto'
        posicaoId = csvEntries.posicao
        nomeClasse = csvEntries.nomeClasse

        nomesSeparados = camelSplit(nomeId)

        arpaCan = True
        score = 0
        addLine = [projeto, nomeId, nomeClasse, posicaoId]

        for nomeSingle in nomesSeparados:

            nomeSingle = nomeSingle.replace(" ", '').lower()

            try:
                arpabetResult = arpabet[nomeSingle]
                # print(arpabetResult)
            except:
                arpaCan = False
                score += 1
                # print("execption")
                # print(nomeSingle)

            if(arpaCan):
                try:
                    score += wcm(arpabetResult[0])
                except:
                    score += 1

        scoreMedia = score/len(nomesSeparados)
        formatted_string = "{:.2f}".format(scoreMedia)
        scoreMedia = float(formatted_string)
        addLine.append(scoreMedia)
        writer.writerows([addLine])

        # print(scoreMedia)
