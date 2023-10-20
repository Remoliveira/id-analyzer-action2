/* eslint-disable no-console */
/* eslint-disable filenames/match-regex */
import {PythonShell} from 'python-shell'
import csv2json from 'csvtojson'

class AlgorithmsService {
  async downloadDependencies(): Promise<void> {
    var package_name = 'pandas'
    let options = {
      args: [package_name]
    }

    return new Promise(async response => {
      setTimeout(() => {
        try {
          PythonShell.run(
            'src/algorithms/install_package.py',
            options,
            function (error) {
              if (error) console.log(error)
            }
          )
        } catch (err) {}

        response()
      }, 2000)
    })
  }

  async applyCategoryAlgorithm(): Promise<void> {
    return new Promise(async response => {
      setTimeout(() => {
        try {
          PythonShell.run(
            'src/algorithms/categoriesAlgorithm/CategoryCatch.py',
            undefined,
            function (error) {
              if (error) console.log(error)
            }
          )
        } catch (err) {}

        response()
      }, 2000)
    })
  }

  async applyWordEmbeddingAlgorithm(): Promise<void> {
    return new Promise(async response => {
      setTimeout(() => {
        try {
          PythonShell.run(
            'src/algorithms/wordEmbeddingAlgorithms/fasttext2vec.py',
            undefined,
            function (error) {
              if (error) console.log(error)
            }
          )
        } catch (error) {}
        response()
      }, 2000)
    })
  }

  async applyPhoneticAlgorithm(): Promise<void> {
    return new Promise(async response => {
      setTimeout(() => {
        try {
          PythonShell.run(
            'src/algorithms/phoneticAlgorithms/wordComplexityMeasure.py',
            undefined,
            function (error) {
              if (error) console.log(error)
            }
          )
        } catch (error) {
          console.log(error)
        }
        response()
      }, 2000)
    })
  }

  async setCategoryJson() {
    const categoryCsv = 'IdentificadoresPosProcessamentoDeCategorira.csv'
    const jsonArray = await csv2json().fromFile(categoryCsv)

    return jsonArray
  }

  async setPhoneticJson() {
    const phoneticCsv = 'wcmSeparetedMean.csv'
    const jsonArray = await csv2json().fromFile(phoneticCsv)

    return jsonArray
  }
}

export {AlgorithmsService}
