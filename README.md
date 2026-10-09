# Learning Tracker API

## Description

The Learning Tracker API allows users to create, view, update and delete their learning goals. This application was developed using Python and FastAPI. Learning goals are stored and managed with SQLite.

## Technologies Used

- Python
- FastAPI
- SQLite
- pytest
- HTTPX
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /goals | Create a new learning goal |
| GET | /goals | View all learning goals |
| GET | /goals/{goal_id} | View a specific goal |
| PATCH | /goals/{goal_id} | Update an existing goal |
| DELETE | /goals/{goal_id} | Delete a goal |

## Installation

1. Clone or download the repository.

2. Open a terminal in the project folder and install the required dependencies using `python -m pip install -r requirements.txt`.

3. Start the application by running `python -m uvicorn main:app --reload`.

4. Open `http://127.0.0.1:8000/docs` to access the API documentation.

## Testing

Automated tests have been created using pytest to check the API functionality, including creating, viewing, updating and deleting goals. The tests also check how the API handles invalid requests.

To run the tests, open a terminal in the project folder and enter `python -m pytest`.


