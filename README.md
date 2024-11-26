# Todoist-GPT-Demo
The purpose of this project is to create automation that enables a user to create Todoist tasks fluidly and easily while using AI. For instance, you may find yourself in a chat with SLMs or LLMs with a plethora of information that you want to track as tasks. Instead of switching applications to create the tasks in Todoist, AI does a very good job of taking specified information and formatting it so it is easily digestible for programmatic sources. And thus, a user can simply ask AI to break down the information, format it, and create tasks. 

The specific implementation of this is curently a small Flask API as an AWS Lambda, built and deployed with AWS SAM and CloudFormation, along with Secrets Manager to store API keys.

Due to a limitation with ChatGPT-4o that inhibits it from making HTTP requests, there is no way to link it with the application. Therefore, it's a WIP. However, ChatGPT can still format data and provide JSON blocks or CURL statements.
