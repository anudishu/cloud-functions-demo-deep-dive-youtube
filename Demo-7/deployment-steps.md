# Deployment Steps

- `cd Demo-7`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

  - `gcloud config set project gcp-cloud-functions-demo-1`

- Create Service Account
  - `gcloud iam service-accounts create cloud-functions-demo-service-account --display-name="Cloud Functions Demo Service Account"`

## Enable APIs

- Enable Cloud SQL Admin API

## Modify IAM Role

- Add Cloud SQL Client Role to Service Account
  - `gcloud projects add-iam-policy-binding gcp-cloud-functions-demo-1 --member serviceAccount:cloud-functions-demo-sa@gcp-cloud-functions-demo-1.iam.gserviceaccount.com --role 'roles/cloudsql.client'`
- Add Secret Manager Secret Accessor Role to IAM Role
 - `gcloud projects add-iam-policy-binding my-project-asksumit --member serviceAccount:cloud-functions-demo-sa@	my-project-asksumit.iam.gserviceaccount.com --role 'roles/secretmanager.secretAccessor'`

## Create MySQL Database

- Create cloud SQL database

## Create Secret in Secrets Manager

- Create secret db-password in Secrets Manager - Bwpj8ez0oCBvzmGr

## Create Schema & Tables in MySQL DB

- Open Cloud Shell after SQL instance is created and execute following commands

  - `gcloud sql connect test-sql-1 --user root`

  - `SHOW DATABASES;`

  - `SHOW SCHEMAS;`

  - `CREATE DATABASE mydb;`

  - `SHOW DATABASES;`

  - `USE mydb;`

  - `SHOW TABLES;`

  - `CREATE TABLE students (studentid INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(25), CONSTRAINT students_pk PRIMARY KEY (studentid));`

  - `SHOW TABLES;`

  - `INSERT INTO students (name) VALUES("student1");`
  - `INSERT INTO students (name) VALUES("student2");`

  - `SELECT * FROM students;`

## Deploy to GCP

- `gcloud functions deploy demo7 --entry-point hello --runtime python39 --source . --region us-east1 --trigger-http --allow-unauthenticated --set-env-vars ENVIRONMENT=cloudfunction --set-secrets DATABASE_PASSWORD=db-password:latest --service-account cloud-functions-demo-sa@	my-project-asksumit.iam.gserviceaccount.com`
