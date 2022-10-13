# Deployment Steps

- `cd Demo-6`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

  - `gcloud config set project gcp-cloud-functions-demo-1`

- Create Service Account
  - `gcloud iam service-accounts create cloud-functions-demo-sql-1-sa --display-name="Cloud Functions Demo Service Account"`

## Enable APIs

- Enable Cloud SQL Admin API

## Modify IAM Role

- Add Cloud SQL Client Role to Service Account
  - `gcloud projects add-iam-policy-binding 	my-project-asksumit --member serviceAccount:cloud-functions-demo-sa@	my-project-asksumit.iam.gserviceaccount.com --role 'roles/cloudsql.client'`

## Create MySQL Database

- Create cloud SQL database

## Deploy to GCP

- `gcloud functions deploy demo6 --entry-point hello --runtime python39 --source . --region us-east1 --trigger-http --allow-unauthenticated --set-env-vars ENVIRONMENT=cloudfunction --service-account cloud-functions-demo-sa@	my-project-asksumit.iam.gserviceaccount.com`
