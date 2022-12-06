
import jellyfish
import re
import pandas as pd
import csv
pd.options.display.max_rows = 9999

identificadoresCsv = pd.read_csv('../../../Identifiers.csv')


def camelSplit(identifier):
    matches = re.finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$|_)', identifier)
    return [m.group(0).replace("_", "") for m in matches]


fieldnames = ['nome_projeto', 'nome_identificador', 'posicao',
              'american_soundex', 'metaphone', 'NYSIIS', 'match_rating_approach']

with open('algoritmosFoneticos.csv', 'w') as file:

    writer = csv.writer(file)
    writer.writerows([fieldnames])

    for row in identificadoresCsv.iterrows():

        csvEntries = row[1]

        nomeIdentificador = csvEntries.nome

        tipo = csvEntries.tipo
        posicao = csvEntries.posicao

        addLine = ['projeto', nomeIdentificador, posicao]

        nameSoundex = jellyfish.soundex(nomeIdentificador)
        addLine.append(nameSoundex)

        nameMetaphone = jellyfish.metaphone(nomeIdentificador)
        addLine.append(nameMetaphone)

        nameNysiis = jellyfish.nysiis(nomeIdentificador)
        addLine.append(nameNysiis)

        nameCodex = jellyfish.match_rating_codex(nomeIdentificador)
        addLine.append(nameCodex)

        writer.writerows([addLine])
