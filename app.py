import awsgi
import boto3
import json
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_todoist_api_key():
    secret_name = "todoist-secret"  
    region_name = "us-east-1"   

    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        # Retrieve the secret value
        response = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])
        return secret["TODOIST_API_KEY"]
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        return None


@app.route("/create_task", methods=["POST"])
def create_task():
    todoist_api_key = get_todoist_api_key()
    if not todoist_api_key:
        return jsonify({"success": False, "error": "Failed to retrieve API key"}), 500

    # Extract data from the request
    data = request.json
    task_content = data.get("content")
    due_date = data.get("due_date", "today")
    priority = data.get("priority", 1)

    # Todoist API endpoint and headers
    todoist_url = "https://api.todoist.com/rest/v2/tasks"
    headers = {
        "Authorization": f"Bearer {todoist_api_key}",
        "Content-Type": "application/json"
    }

    # Payload for creating a task
    payload = {
        "content": task_content,
        "due_string": due_date,
        "priority": priority
    }

    # Send the request to Todoist API
    response = requests.post(todoist_url, json=payload, headers=headers)

    # Handle the response
    if response.status_code == 200 or response.status_code == 204:
        return jsonify({"success": True, "task": response.json()})
    else:
        return jsonify({"success": False, "error": response.text}), response.status_code


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
