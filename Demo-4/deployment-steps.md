# Deployment Steps

## Test on Local

- `cd Demo-4`

- `functions-framework --target hello --debug`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

- `gcloud config set project test-cloud-func-1`

## Deploy to GCP

- `gcloud functions deploy demo4 --entry-point hello --runtime python39 --source . --region us-east1 --trigger-http --allow-unauthenticated`
