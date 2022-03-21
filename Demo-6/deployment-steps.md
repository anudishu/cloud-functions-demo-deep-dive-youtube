# Deployment Steps

- `cd Demo-6`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

- `gcloud config set project test-cloud-func-1`

## Enable APIs

- Enable Cloud SQL Admin API

## Modify IAM Role

- Add Cloud SQL Client Role to IAM Role

## Create MySQL Database

- Create cloud SQL database

## Deploy to GCP

- `gcloud functions deploy demo6 --entry-point hello --runtime python39 --source . --region us-east1 --trigger-http --allow-unauthenticated --set-env-vars ENVIRONMENT=cloudfunction`
