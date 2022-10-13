# Deployment Steps

## Test on Local

- `cd Demo-5`

- > Main Terminal:
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `functions-framework --target=hello --signature-type=event --debug --port=8080 --host 0.0.0.0`

- > Terminal 2:
- `export PUBSUB_PROJECT_ID=my-project`
- `gcloud beta emulators pubsub start --project=$PUBSUB_PROJECT_ID --host-port=localhost:8085`

- > Termanal 3:
- `export PUBSUB_PROJECT_ID=my-project`
- `export TOPIC_ID=my-topic`
- `export PUSH_SUBSCRIPTION_ID=my-subscription`
- `$(gcloud beta emulators pubsub env-init)`
- `git clone https://github.com/googleapis/python-pubsub.git`
- `cd python-pubsub/samples/snippets/`
- `pip install -r requirements.txt`
- `python publisher.py $PUBSUB_PROJECT_ID create $TOPIC_ID`
- `python subscriber.py $PUBSUB_PROJECT_ID create-push $TOPIC_ID $PUSH_SUBSCRIPTION_ID http://localhost:8080`
- `python publisher.py $PUBSUB_PROJECT_ID publish $TOPIC_ID`

## Pre-Deployment Steps (One Time)

- `gcloud auth login`

- `gcloud projects list`

- `gcloud config set project PROJECT_ID`

  - `gcloud config set project gcp-cloud-functions-demo-1`

- Create Service Account
  - `gcloud iam service-accounts create cloud-functions-demo-sa --display-name="Cloud Functions Demo Service Account"`

## Deploy to GCP

- Create topic my-awesome-topic

- Create bucket my-awesome-bucket-123456

- `gcloud functions deploy demo5-pubsub --entry-point hello --runtime python39 --source . --region us-east1 --trigger-topic my-awesome-topic --service-account cloud-functions-demo-sa@my-project-asksumit.iam.gserviceaccount.com`

- `gcloud functions deploy demo5-cloud-storage --entry-point hello --runtime python39 --source . --region us-east1 --trigger-bucket my-awesome-bucket-123456 --service-account cloud-functions-demo-sa@my-project-asksumit.iam.gserviceaccount.com`
