# ci-cd-project
created simple pipeline: test -> build -> delivery to Docker Hub 
pipeline ingnores unimportant files that aren't in src/ path, classifed as dummy files
## Services i used:
* Github actions - to setup pipeline configuration file
* Docker - used in build and delivery phase of pipeline
* Python - programming language for app and pytest test
* Github Branch protection - to deny merging unless github actions checkmarks are up
## files
[.github/workflows](.github/workflows) - github actions config files 
