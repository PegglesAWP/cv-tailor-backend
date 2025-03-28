# CV Tailor Backend

FastAPI backend for the CV Tailor application, which helps students and graduates create tailored CVs and cover letters for Australian graduate employers.

## Features

- User authentication with JWT
- Experience and education data management
- AI-powered CV and cover letter generation using Claude API
- Employer data scraping and storage
- Document generation with python-docx
- Stripe payment integration

## Setup Instructions

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file based on `.env.example`
6. Run the application: `uvicorn app.main:app --reload`

## API Documentation

When running locally, access the API documentation at:
- <http://localhost:8000/docs>
