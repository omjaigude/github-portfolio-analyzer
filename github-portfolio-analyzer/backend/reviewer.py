def generate_review(score, report):

    strengths = []
    weaknesses = []
    advice = []

    # Activity
    if report["activity"] == "Very Active":
        strengths.append("Shows consistent coding habit")
    else:
        weaknesses.append("Low contribution consistency")
        advice.append("Push code regularly every week")

    # Documentation
    if report["documentation"] == "Well Documented":
        strengths.append("Explains projects clearly")
    else:
        weaknesses.append("Missing proper README files")
        advice.append("Add README with features, setup, screenshots")

    # Impact
    if report["impact"] == "Used by others":
        strengths.append("Projects have real-world usefulness")
    else:
        weaknesses.append("Projects look like practice projects")
        advice.append("Build and deploy one real-world project")

    # Skills
    if len(report["skills"]) < 3:
        weaknesses.append("Limited tech stack")
        advice.append("Learn backend + database + API integration")

    # Hiring decision
    if score >= 70:
        decision = "Ready for internships"
    elif score >= 40:
        decision = "Needs improvement before applying"
    else:
        decision = "Not ready for hiring yet"

    return {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "advice": advice,
        "decision": decision
    }
