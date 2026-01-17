# CI/CD-pipeline-project
created simple pipeline: test -> build -> delivery to Docker Hub 
pipeline ingnores unimportant files that aren't in src/ path, classifed as dummy files
## How it Works
pipeline is configurated using github actions YAML files, each file contains event trigger, jobs, steps, actions:
#### [githubactions.yaml](.github/workflows/githubactions.yaml) - default pipeline setup for important src/ files, include jobs:
1. tests - responsible for early unit tests in local environment, using pytest
2. build - responsible for building docker image, and checking running capabilities
3. delivery - responsible for builds and pushes of docker image to docker hub
#### [github-dummy-action.yaml](.github/workflows/github-dummy-action.yaml) - dummy pipeline setup for common files
## Services i used:
* Github actions - to setup pipeline configuration file
* Docker - used in build and delivery phase of pipeline
* Python - programming language for app and pytest test
* Github Branch protection - to deny merging unless github actions checkmarks are up
## files
[.github/workflows](.github/workflows) - github actions config files 
