from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from github_api import get_user, get_repos
from scorer import score_profile
from reviewer import generate_review

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze/{username}")
def analyze(username: str):

    user = get_user(username)
    repos = get_repos(username)

    result = score_profile(user, repos)
    review = generate_review(result["score"], result["report"])

    return {
        "user": user.get("login"),
        "followers": user.get("followers"),
        "repos": len(repos),
        "analysis": result,
        "review": review
    }
