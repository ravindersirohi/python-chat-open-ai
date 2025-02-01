# python-chat-open-ai
Python Open AI

## About
Python Fast API running on [Google Cloud Run ](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service) container app, and integrated with Chat GPT 4 via the [Open AI](https://platform.openai.com/docs/overview) API.

## How to setup and debug locally?

Please refer below steps to setup the Python Fast API.

1. First clone [gh repo clone ravindersirohi/python-fast-api] the python-fast-api repository.
2. Go to the python-chat-open-ai folder.
3. Run - [pip install -r requirements.txt] from command prompt.
4. Now create the virtual environment [python -m venv env] and activate (Windows [.\env\Scripts\activate], macOS/Linux [source env/bin/activate]) the virtual environment.
5. [uvicorn main:app --reload] to start the app, once api is up should see http://127.0.0.1:8000
6. http://127.0.0.1:8000/docs to see the Open API/Swagger documentation.

## Deployment

Source and infrastructre deployed via the Github workflow, please refer [.github/workflow/deploy](https://github.com/ravindersirohi/python-chat-open-ai/blob/main/.github/workflows/deploy.yml) yaml file.

## Chat GPT API Config
1. Register yourself on [Open AI platform](https://platform.openai.com/) and generate [Open AI](https://platform.openai.com/settings/organization/api-keys) key, required to make a call from any client, in this case [Fast API](https://fastapi.tiangolo.com/).
2. Add OPENAI_API_KEY environment variable in Github Environment variable (Repository settings->Secrets and Variables) and set this Open AI key.
3. Populate GCP_PROJECT_ID and GCP_CREDENTIALS in GitHub secrets (Repository settings->Secrets and Variables).

## Infrastrue setup
API infrastructe is setup on Google Cloud Platform via Terraform, please refer [gcp-terraform-infra](https://github.com/ravindersirohi/gcp-terraform-infra) and extend for below resources.

```
Service Account:

resource "google_service_account" "service_account" {
  account_id   = "service-account-id"
  display_name = "Service Account"
}

Artifact Registry:

resource "google_artifact_registry_repository" "my-repo" {
  location      = "europ-west2"
  repository_id = "my-repository"
  description   = "example docker repository"
  format        = "DOCKER"
}

```

## How to access API once hosted on Google Cloud ?

Once the source code gets deployed via the Github trigger, should be able to see container access point (for example - https://gcp-chat-gpt-fast-api-xxxxx.europe-west2.run.app).
Please follow below to access Chat GPT API.

1. .../docs - Swagger UI endpoint.
2. .../chat - To interact with chat by sending the below payload.
```
Post request /chat

{
    "prompt": "Who is 007?"
}

If, everything configured correctly should get below response.

{
    "prompt": "Who is 007?",
    "response": "007 is a fictional character in a series of spy novels written by British author Ian Fleming. The character, also known by his code name, James Bond, is a Secret Service agent working for the British government. He is known for his sophistication, skill in espionage and combat, and his iconic status as a symbol of mid-20th century Cold War intrigue. The character has been adapted and continued in films, television, and other media."
}

```

## Additional references

- [Fast API](https://fastapi.tiangolo.com/)
