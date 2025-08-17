# Open SWE CLI How-To

This guide shows how to run the Open SWE CLI and includes examples for common tasks.

## Setup

1. Copy `.env.example` to `.env` and add your API keys.
2. Install dependencies and build the workspace:
   ```bash
   yarn install
   yarn build
   ```
3. Point the CLI at a project by setting `OPEN_SWE_LOCAL_PROJECT_PATH`:
   ```bash
   OPEN_SWE_LOCAL_PROJECT_PATH=/path/to/project yarn cli
   ```

## Create a web app

1. Make a new directory and initialize git (optional):
   ```bash
   mkdir hello-web && cd hello-web && git init
   ```
2. Start the CLI:
   ```bash
   OPEN_SWE_LOCAL_PROJECT_PATH=$(pwd) yarn cli
   ```
3. At the prompt, ask:
   ```
   Create a simple React app that shows "Hello, world" on the homepage.
   ```
4. Approve the plan and watch the agent generate the project files.

## Create a full stack app

1. Prepare a directory:
   ```bash
   mkdir todo-app && cd todo-app && git init
   ```
2. Launch the CLI as above.
3. Prompt the agent:
   ```
   Build a full stack TODO app with an Express API, a SQLite database, and a React front end. Include scripts to run the server and client.
   ```
4. Approve each plan step. The agent will create API routes, database schema, and UI components.

## Work in an existing repository

1. Clone or use an existing git repository:
   ```bash
   git clone https://github.com/user/repo.git
   cd repo
   ```
2. Run the CLI pointing at the repo:
   ```bash
   OPEN_SWE_LOCAL_PROJECT_PATH=$(pwd) yarn cli
   ```
3. Give the agent tasks, for example:
   ```
   Add unit tests for the auth middleware and refactor the handler to use async/await.
   ```
4. The agent applies patches, commits them, and you can push the changes to GitHub.

