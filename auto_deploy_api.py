from fastapi import FastAPI
import httpx
import os

app = FastAPI()

# Environment Variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = "KAP-ment"

# Repo names
REPO_FRONTEND = "KAP"                    # Main Next.js frontend repo
REPO_DASHBOARD = "nextjs-boilerplate"    # Dashboard repo

@app.get("/")
def home():
    return {"status": "Auto Deploy API Running ✔"}

@app.post("/update")
async def update():
    if not GITHUB_TOKEN:
        return {"error": "GitHub Token Missing in Render Environment!"}

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    async with httpx.AsyncClient() as client:

        # Trigger Frontend Deploy (KAP repo)
        await client.post(
            f"https://api.github.com/repos/{OWNER}/{REPO_FRONTEND}/dispatches",
            headers=headers,
            json={"event_type": "auto-deploy"}
        )

        # Trigger Dashboard Deploy (nextjs-boilerplate repo)
        await client.post(
            f"https://api.github.com/repos/{OWNER}/{REPO_DASHBOARD}/dispatches",
            headers=headers,
            json={"event_type": "auto-deploy"}
        )

    return {"message": "Deploy triggered for KAP + Dashboard 🚀"}
