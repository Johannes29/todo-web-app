import json

from flask import Flask, make_response, request
from tasks import Tasks

app = Flask(__name__)
tasks = Tasks()

@app.route("/api/new_task", methods=["GET", "POST"])
def create_new_task():
    task_name = request.get_json()["name"]
    task_id = tasks.add_task(task_name)
    task = tasks.get_task(task_id)
    return make_response(json.dumps(task), 201)
