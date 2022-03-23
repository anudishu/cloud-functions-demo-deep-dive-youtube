# Deployment Steps

- `cd Demo-3`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

  - `gcloud config set project gcp-cloud-functions-demo-1`

- Create Service Account
  - `gcloud iam service-accounts create cloud-functions-demo-sa --display-name="Cloud Functions Demo Service Account"`

## Deploy to GCP

- `gcloud functions deploy demo3 --entry-point hello --runtime python39 --source . --region us-east1 --trigger-http --allow-unauthenticated --service-account cloud-functions-demo-sa@gcp-cloud-functions-demo-1.iam.gserviceaccount.com`
