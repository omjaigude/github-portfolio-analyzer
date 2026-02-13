# 🔎 GitHub Developer Analyzer

A web application that evaluates a developer’s GitHub profile and generates a hiring recommendation based on repository activity and contribution statistics.

Built for Hackathon Submission 🏆

---

## 📌 Objective

Recruiters often rely on resumes which may not accurately represent real coding ability.

This project analyzes a developer’s actual GitHub activity and automatically provides a skill evaluation and hiring suggestion.

---

## 🧠 How It Works

1. User enters a GitHub username
2. Backend fetches public GitHub data
3. Important metrics are extracted
4. A scoring algorithm evaluates the profile
5. Website shows developer level and recommendation

---

## 📊 Features Analyzed

* Number of repositories
* Followers count
* Following count
* Stars received
* Fork count
* Activity level
* Programming languages used

Each feature contributes to a total developer score.

---

## 🧮 Evaluation Logic

The system calculates a score based on developer activity:

Higher activity → Higher score → Better recommendation

The score is categorized into:

| Score Range | Level        |
| ----------- | ------------ |
| Low         | Beginner     |
| Medium      | Intermediate |
| High        | Advanced     |
| Very High   | Expert       |

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask
* Requests

### Data Source

* GitHub Public API

---

## 📁 Project Structure

```
project/
│
├── backend/
│   ├── app.py
│   ├── github_fetcher.py
│   ├── predictor.py
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone repository

```
git clone <repo link>
cd project
```

### 2. Create virtual environment

```
python -m venv .venv
```

Activate (Windows):

```
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add GitHub Token

Create:

```
backend/.env
```

Add:

```
GITHUB_TOKEN=your_token_here
```

### 5. Run backend

```
cd backend
python app.py
```

### 6. Open frontend

Open in browser:

```
frontend/index.html
```

---

## 📌 Example Output

Input:

```
torvalds
```

Output:

* Developer Level: Advanced
* Activity Score: High
* Hiring Suggestion: Strong Hire

---

## 🎯 Use Cases

* Quick developer screening
* Internship filtering
* Hackathon team selection
* Open-source contributor evaluation

---

## 🔐 Privacy

Only public GitHub data is accessed. No private information is collected.

---

## 🚀 Future Improvements

* Add Machine Learning prediction
* Resume upload analysis
* Recruiter dashboard
* Candidate comparison tool

---

## 👨‍💻 Developed For

Hackathon Project Submission
