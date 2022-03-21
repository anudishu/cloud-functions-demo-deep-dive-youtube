# Deployment Steps

- `cd Demo-3`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

- `gcloud config set project test-cloud-func-1`

## Deploy to GCP

- `gcloud functions deploy demo3 --entry-point hello --runtime python39 --source . --region us-east1 --trigger-http --allow-unauthenticated`
