/* eslint-disable no-console */
import * as core from '@actions/core'
import {AlgorithmsService} from './service/AlgorithmService'
import {ProjectsService} from './service/ProjectService'

const algorithmsService = new AlgorithmsService()
const projectService = new ProjectsService(algorithmsService)

async function run(): Promise<void> {
  try {
    console.log('herew')

    let repo = core.getInput('repoName')
    let owner = core.getInput('owner')
    let branch = core.getInput('branch')
    repo = 'Calculator'
    owner = 'HouariZegai'
    branch = 'master'
    await projectService.storeProject({repo, owner, branch})
  } catch (error) {
    if (error instanceof Error) core.setFailed(error.message)
  }
}

run()
