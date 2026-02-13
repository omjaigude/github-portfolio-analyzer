def score_profile(user, repos):

    score = 0
    report = {}

    # Activity
    if user.get("public_repos", 0) > 15:
        score += 20
        report["activity"] = "Very Active"
    elif user.get("public_repos", 0) > 5:
        score += 10
        report["activity"] = "Moderate"
    else:
        report["activity"] = "Low Activity"

    # Documentation
    documented = sum(1 for r in repos if r.get("description"))
    ratio = documented / len(repos) if repos else 0

    if ratio > 0.7:
        score += 20
        report["documentation"] = "Well Documented"
    else:
        report["documentation"] = "Poor Documentation"

    # Impact
    stars = sum(r.get("stargazers_count",0) for r in repos)
    if stars > 50:
        score += 20
        report["impact"] = "Used by others"
    else:
        report["impact"] = "Low visibility"

    # Skills
    langs = set(r.get("language") for r in repos if r.get("language"))
    skill_score = min(len(langs)*5,20)
    score += skill_score
    report["skills"] = list(langs)

    # Final grade
    if score >= 70:
        grade = "HIRE"
    elif score >= 40:
        grade = "CONSIDER"
    else:
        grade = "REJECT"

    return {"score":score,"grade":grade,"report":report}
