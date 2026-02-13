# 🔎 GitHub Developer Analyzer

A web application that evaluates a developer’s GitHub profile and generates a hiring recommendation based on repository activity and contribution statistics.

---

## 📌 Objective

This project analyzes a developer’s actual GitHub activity and automatically provides a skill evaluation and hiring suggestion.

---

## 📌 Optional Way
Add GitHub token in backend/.env to increase API request limit.
Project works without token as well.

## 🧠 How It Works

1. User enters a GitHub username
2. Backend fetches public GitHub data
3. Important metrics are extracted
4. A scoring algorithm evaluates the profile
5. Website shows developer level and recommendation

---

## 📷 Demo

### Home Page
<img width="1702" height="823" alt="Screenshot 2026-02-13 193614" src="https://github.com/user-attachments/assets/9a6db3f5-a94f-4a6c-a0c4-a78fc92ed3f7" />


### Enter Username
<img width="1699" height="793" alt="Screenshot 2026-02-13 193653" src="https://github.com/user-attachments/assets/c9a86eb1-53a4-478d-b37a-0b9420ba3217" />


### Prediction Result
<img width="1456" height="883" alt="Screenshot 2026-02-13 193738" src="https://github.com/user-attachments/assets/58285565-0718-46ad-8b60-534fd5284c89" />


## 📊 Features Analyzed

* Number of repositories
* Followers count
* Stars received
* Fork count
* Activity level
* Programming languages used

Each feature contributes to a total developer score.

---

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
│   ├── github_api.py
│   ├── scorer.py
│   ├── reviewer.py
│   ├──requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
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


## 🔐 Privacy

Only public GitHub data is accessed. No private information is collected.


## 👨‍💻 Author: Om Jaigude

