# ERG ETL
## Overview

The ERG ETL (Extract, Transform, Load) module is a Python-based tool designed to facilitate data processing pipelines. Its primary functions include loading data from Azure Blob Storage, cleaning and validating the data according to predefined rules specified in a config.json file, and finally writing the results into a PostGIS database. This document outlines the prerequisites and steps needed to set up and run the ERG ETL module.

## Prerequisites

To set up and use the ERG ETL module, the following tools and environments are required:

1. **Minikube**: A local Kubernetes environment focused on simplifying learning and development for Kubernetes.
1. **kubectl**: A command-line tool for interacting with Kubernetes clusters.
1. **Argo CLI**: Used for submitting and managing workflows in Argo.
1. **PostGIS**: A PostgreSQL database extension that adds support for geographic objects.
1. **Docker**: Required for building and pushing the ERG ETL module's Docker image.

## Installation Steps
### Install Minikube

Minikube is a tool that runs a single-node Kubernetes cluster locally for development purposes.
- Installation on macOS:
```zsh
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube
minikube start
```
[Minikube Official Documentation](https://minikube.sigs.k8s.io/docs/start/)
### Install kubectl
kubectl is a command-line interface for running commands against Kubernetes clusters.
- Installation on macOS:
```zsh
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
sudo chown root: /usr/local/bin/kubectl
kubectl version --client
```

[Kubernetes Documentation Install Tools](https://kubernetes.io/docs/tasks/tools/)

### Install Argo CLI
Argo CLI is used for managing Argo Workflows.
- Installation:
```zsh
curl -sLO https://github.com/argoproj/argo-workflows/releases/download/v3.5.2/argo-darwin-amd64.gz
gunzip argo-darwin-amd64.gz
chmod +x argo-darwin-amd64
mv ./argo-darwin-amd64 /usr/local/bin/argo
argo version
```
[Argo CLI Installation](https://github.com/argoproj/argo-workflows/releases/)

### Set Up PostGIS
Deploy PostGIS within a Kubernetes cluster.
- Deployment:
```zsh
# Update postgres-postgis-deployment.yaml with the desired PostgreSQL user and password
    kubectl apply -f postgres-postgis-deployment.yaml
```

### Build and Push ERG ETL Docker Image
Build the ERG ETL Docker image and push it to your repository.
-  Build and Push:
```zsh
cd etl  # Move to the ERG ETL project directory
docker build -t <repo_name>/ergetl:0.0.1 .
docker image push <repo_name>/ergetl:0.0.7
```
- Replace `<repo_name>` with your repository name in your Docker Hub configuration.

- Update the version image in the `argo-worfkflow-template.yaml` file in line 58:
```yaml
- name: python-script
  container:
    image: <repo_name>/ergetl:0.0.1
```

### Update Configuration
Modify the `params.yaml` file with appropriate values for your setup. 

### Submit Argo Workflows
Submit a job to Argo Workflows, passing the JSON payload as a base64-encoded string.
- Submit Workflow:
```zsh
argo submit argo.yaml -p jsonContent=$(base64 -i config.json) -f params.yaml -n argo
```
## Usage

After installation, you can use the ERG ETL module to automate data extraction, transformation, and loading processes. Ensure that the **Azure Blob Storage**, **PostGIS** database, and other configurations are correctly set up in the `params.yaml` and config.json files. The module will handle data processing according to these configurations.