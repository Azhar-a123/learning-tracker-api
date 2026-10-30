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

## Installation

1. Clone or download the repository.

2. Open a terminal in the project folder and install the required dependencies using `python -m pip install -r requirements.txt`.

3. Start the application by running `python -m uvicorn main:app --reload`.

4. Open `http://localhost:8000/docs` to access the API documentation.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /goals | Create a new learning goal |
| GET | /goals | View all learning goals |
| GET | /goals/{goal_id} | View a specific goal |
| PATCH | /goals/{goal_id} | Update an existing goal |
| DELETE | /goals/{goal_id} | Delete a goal |

## status Handling

There are only 3 statuses the API accepts, `not_started`- the goal has not been started, `in_progress`- the user is currently working on the goal and `completed`- the goal has been achieved.

Example- 

{

"title": "learn Python"
"status": "in_progress"

}

## Testing

Automated tests have been created using pytest to check the API functionality, including creating, viewing, updating and deleting goals. The tests also check how the API handles invalid requests.

To run the tests, open a terminal in the project folder and enter `python -m pytest`.

## RUNNING WITH Docker

To run this application through Docker, you need Docker Desktop installed and running.

Build the Docker image in the VS Code terminal: 

`docker build -t learning-tracker-api .` 

Create a Docker volume:

`docker volume create learning-tracker-data`

Start the application with the Docker volume

 `docker run --rm -p 127.0.0.1:8000:8000 -e DATABASE_PATH=/app/data/learning_tracker.db -v learning-tracker-data:/app/data learning-tracker-api`

Open the API documentation in your browser after the application is running: 

http://localhost:8000/docs

The Docker volume stores the SQLite database so that saved goals are not lost when the container is stopped and removed.
