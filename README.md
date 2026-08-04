# Flask Demo

A simple Flask application built to learn and demonstrate the basics of Flask routing.

## What this project does

- Shows how to create basic routes in Flask (`/`, `/welcome`, `/index`)
- Demonstrates dynamic URL routes using parameters (`/success/<score>`, `/fail/<score>`)
- Includes a form-based route (`/calculate`) that takes marks in three subjects, calculates the average, and shows a pass/fail result
- Includes a simple JSON API endpoint (`/api`) that takes two numbers and returns their sum

## Tech Used

- Python
- Flask

## Project Structure

```
├── app.py # Main Flask application with all routes
├── templates/ # HTML templates (index, calculate, result pages)
├── requirements.txt # Python dependencies
├── test.json # Sample JSON data for testing the API
└── README.md
```

## Routes Overview

| Route | Method | What it does |
|---|---|---|
| `/` | GET | Shows a simple "Hello, World!" message |
| `/welcome` | GET | Shows a welcome message |
| `/index` | GET | Renders the index page |
| `/success/<score>` | GET | Shows a pass message with the given score |
| `/fail/<score>` | GET | Shows a fail message with the given score |
| `/calculate` | GET, POST | Shows a form to enter marks, then calculates and displays the average and result |
| `/api` | POST | Accepts JSON with two numbers (`a`, `b`) and returns their sum |

## How to Run Locally

1. Clone this repo

```bash
   git clone https://github.com/Sonalikasingh17/FlaskDemo.git
   cd FlaskDemo
```

2. Install the required packages

```bash
   pip install -r requirements.txt
```

3. Run the app

```bash
   python app.py
```

4. Open your browser and go to `http://localhost:5000`

## Testing the API

You can test the `/api` endpoint using a tool like Postman or `curl`:

```bash
curl -X POST http://localhost:5000/api -H "Content-Type: application/json" -d '{"a": 5, "b": 10}'
```

This should return:

```json
{"result": 15.0}
```

## Purpose

This project was built to practice and understand the basics of Flask — routing, handling forms, dynamic URLs, and building a simple API endpoint.
