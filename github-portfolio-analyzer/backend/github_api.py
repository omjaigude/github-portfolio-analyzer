import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"token {TOKEN}"
}

BASE = "https://api.github.com"

def get_user(username):
    return requests.get(f"{BASE}/users/{username}", headers=HEADERS).json()

def get_repos(username):
    return requests.get(f"{BASE}/users/{username}/repos?per_page=100", headers=HEADERS).json()
