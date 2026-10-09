from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class Goal(BaseModel):
    title: str
    status: str


class GoalUpdate(BaseModel):
    title: str | None = None
    status: str | None = None


DATABASE = "learning_tracker.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL,
        status TEXT NOT NULL) """)
    finally:
        connection.close()


create_table()


@app.get("/goals/{goal_id}")
def get_goal(goal_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM goals WHERE id = ?", (goal_id,))
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="goal not found")
        goal = {"id": row[0], "title": row[1], "status": row[2]}
        return goal

    finally:
        connection.close()


@app.post("/goals")
def create_goal(goal: Goal):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO goals (title, status) VALUES (?, ?)", (goal.title, goal.status)
        )
        connection.commit()
        goal_id = cursor.lastrowid
        new_goal = {"id": goal_id, "title": goal.title, "status": goal.status}
        return new_goal
    finally:
        connection.close()


@app.get("/goals")
def get_goals():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM goals")
        rows = cursor.fetchall()
        results = []
        for row in rows:
            goal = {"id": row[0], "title": row[1], "status": row[2]}
            results.append(goal)

        return results
    finally:
        connection.close()


@app.patch("/goals/{goal_id}")
def update_goal(goal_id: int, update: GoalUpdate):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM goals WHERE id = ?", (goal_id,))
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="goal not found")
        new_title = row[1]
        new_status = row[2]

        if update.title is not None:
            new_title = update.title

        if update.status is not None:
            new_status = update.status

        cursor.execute(
            "UPDATE goals SET title = ?, status = ? WHERE id = ?",
            (new_title, new_status, goal_id),
        )
        connection.commit()
        updated_goal = {"id": goal_id, "title": new_title, "status": new_status}
        return updated_goal
    finally:
        connection.close()


@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM goals WHERE id = ?", (goal_id,))
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="goal not found")

        cursor.execute("Delete FROM goals WHERE id= ?", (goal_id,))

        connection.commit()

        deleted_goal = {"id": row[0], "title": row[1], "status": row[2]}
        return deleted_goal
    finally:
        connection.close()
