# Rule Engine Project

This project implements a rule-based engine where users can create custom rules and evaluate them against specific data sets. It features a **Flask** backend for handling rule creation and evaluation, **MongoDB** for storing the rules, and a **React** frontend for user interaction.

## Features

- **Create Rules**: Users can define rules using logical expressions (e.g., `age > 30 AND salary > 50000`).
- **Evaluate Rules**: Users can evaluate the created rules against provided data.
- **Storage**: Rules are stored in a **MongoDB** database for persistence.
- **Frontend-Backend Communication**: The frontend sends HTTP requests to the backend for rule creation and evaluation.
- **Error Handling**: Robust error handling on both frontend and backend to ensure smooth operations.

---

## Table of Contents

- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [How to Use](#how-to-use)
- [API Endpoints](#api-endpoints)
- [License](#license)

---

## Technologies Used

- **Backend**: Flask, Flask-CORS, pymongo
- **Database**: MongoDB
- **Frontend**: React, Axios
- **Other**: Python’s `ast` module for parsing rules into Abstract Syntax Tree (AST)

---

## Getting Started

### Prerequisites

- **Node.js** (for running the React frontend)
- **Python 3.x** (for running the Flask backend)
- **MongoDB** (ensure MongoDB is running locally or remotely)
  
### Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/rule-engine-project.git
cd rule-engine-project
```

## Backend Setup

- Navigate to the backend/ directory:

```bash
cd backend/
```

- Install Python dependencies using pip:

```bash
pip install -r requirements.txt
```

- Ensure MongoDB is running locally or update the connection string in app.py to your remote MongoDB instance:

```bash
client = MongoClient('mongodb://localhost:27017/')
```

- Start the Flask backend:

```bash
python app.py
```

The backend will run on `http://localhost:5000`.

## Frontend Setup

- Navigate to the frontend/ directory:

```bash
cd frontend/
```

- Install the frontend dependencies:

```bash
npm install
```

- Start the React frontend:

```bash
npm start
```

The frontend will be accessible at `http://localhost:3000`.

## How to Use

### 1. Creating a Rule

- Navigate to the "Create Rule" section on the homepage.
- Enter a rule string in the input field. Example:
```bash
age > 30 AND salary > 50000
```
- Click "Create Rule". If successful, you'll receive a message with the created rule ID.

### 2. Evaluating a Rule

- Navigate to the "Evaluate Rule" section on the homepage.
- Enter the rule ID you received when creating the rule.
- Enter a data set (in JSON format) to evaluate the rule. Example:
```bash
{
  "age": 35,
  "salary": 60000
}
```
- Click "Evaluate Rule". You will see the result of the evaluation (either true or false).

## API Endpoints

### 1. Create Rule

- URL: /api/create_rule
- Method: POST
- Request Body:
```bash
{
  "rule": "age > 30 AND salary > 50000"
}
```
- Response:
Success: 201 Created
```bash
{
  "message": "Rule created successfully",
  "rule_id": "6144f0e1f3b60f2f5b6a254e"
}
```
Error: 400 Bad Request
```bash
{
  "error": "Rule string is required"
}
```

### 2. Evaluate Rule

- URL: /api/evaluate_rule
- Method: POST
- Request Body:
```bash
{
  "rule_id": "6144f0e1f3b60f2f5b6a254e",
  "data": {
    "age": 35,
    "salary": 60000
  }
```
- Response:
Success: 200 OK
```bash
{
  "result": true
}
```
- Error: 404 Not Found
```bash
{
  "error": "Rule not found"
}
```



