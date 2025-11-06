from fastapi import FastAPI
import requests, os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "KAPment automation backend running ✅"}

@app.post("/update")
def update_repo():
    token = os.getenv("GITHUB_TOKEN")
    repo = "KAP-ment/nextjs-boilerplate"
    api_url = f"https://api.github.com/repos/{repo}/dispatches"

    headers = {
        "Accept": "application/vnd.github.everest-preview+json",
        "Authorization": f"token {token}",
    }
    data = {"event_type": "auto_deploy"}
    requests.post(api_url, headers=headers, json=data)
    return {"status": "Triggered GitHub workflow 🚀"}
