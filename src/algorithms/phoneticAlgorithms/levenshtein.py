import jellyfish
import re
import csv
import pandas as pd

identificadoresCsv = pd.read_csv('../../../Identifiers.csv')

difficultWords = ['Accede',
                  'Alias',
                  'Anathema',
                  'Anemone',
                  'Apocryphal',
                  'Camaraderie',
                  'Colloquialism',
                  'Debauch',
                  'Demagogue',
                  'Emollient',
                  'Epitome',
                  'Espouse',
                  'Espresso',
                  'Fatuous',
                  'Forte',
                  'Grandiloquent',
                  'Hegemony',
                  'Inchoate',
                  'Knell',
                  'Maelstrom',
                  'Mauve',
                  'Mischievous',
                  'Nadir',
                  'Neophyte',
                  'Noisome',
                  'Panacea',
                  'Phlegmatic',
                  'Protean',
                  'Puerile',
                  'Pulchritude',
                  'Quinoa',
                  'Quixotic',
                  'Sanguine',
                  'Sherbet',
                  'Staid',
                  'Surfeit',
                  'Timbre',
                  'Truculent',
                  'Vicissitude',
                  'Zephyr']


def camelSplit(identifier):
    matches = re.finditer(
        '.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$|_)', identifier)
    return [m.group(0).replace("_", "") for m in matches]


fieldnames = difficultWords.copy()
fieldnames.insert(0, 'Identificador')
fieldnames.insert(1, 'Classe')
fieldnames.insert(2, 'Projeto')
fieldnames.insert(3, 'Tipo')
fieldnames.insert(4, 'Posicao')

# palavras juntas
# with open('palavrasDificeisCompletas.csv','w') as file:

#     writer = csv.writer(file)
#     writer.writerows([fieldnames])

#     for identificador in identificadores:

#         projeto = identificador[0]
#         nomeId = identificador[1].replace('_','')
#         tipoId = identificador[2]
#         posicaoId = identificador[3]

#         distancia = [nomeId,projeto,tipoId,posicaoId]

#         for unWord in unWords:

#             dLevestein = jellyfish.levenshtein_distance(nomeId.strip(), unWord.strip())
#             distancia.append(dLevestein)
#         # print(distancia)
#         writer.writerows([distancia])


#         # for nomeSingle in nomeId:
#         #     distancia = [nomeSingle,projeto,tipoId,posicaoId]
#         #     for unWord in unWords:

#         #         dLevestein = jellyfish.levenshtein_distance(nomeSingle.strip(), unWord.strip())
#         #         distancia.append(dLevestein)
#         #     # print(distancia)
#         #     writer.writerows([distancia])


# palavras dificeis separadas
with open('palavrasDificeisSeparadasVEM21.csv', 'w') as file:

    writer = csv.writer(file)
    writer.writerows([fieldnames])

    for row in identificadoresCsv.iterrows():

        csvEntries = row[1]

        projeto = 'projeto'
        nomeId = csvEntries.nome
        nomesSeparados = camelSplit(nomeId)
        tipoId = csvEntries.tipo
        posicaoId = csvEntries.posicao
        nomeClasse = csvEntries.nomeClasse

        distancia = [nomeId, projeto, tipoId, posicaoId]

        # for nomeSingle in nomeId:

        #     mediaScore = 0

        #     # distancia = [nomeId,projeto,tipoId,posicaoId]
        #     for unWord in unWords:

        #         dLevestein = jellyfish.levenshtein_distance(nomeSingle.strip(), unWord.strip())
        #         distancia.append(dLevestein)

        #     writer.writerows([distancia])

        mediaScore = 0
        for unWord in difficultWords:

            # distancia = [nomeId,projeto,tipoId,posicaoId]
            mediaScore = 0

            for nomeSingle in nomesSeparados:

                dLevestein = jellyfish.levenshtein_distance(
                    nomeSingle.strip(), unWord.strip())
                mediaScore += dLevestein

            mediaScore = mediaScore/len(nomesSeparados)
            formatted_string = "{:.2f}".format(mediaScore)
            mediaScore = float(formatted_string)
            distancia.append(mediaScore)

        writer.writerows([distancia])


# print(jellyfish.metaphone('Antidisestablishmentarianism'))
# print(jellyfish.soundex('Anathema'))

# print(jellyfish.levenshtein_distance('response','answer'))
