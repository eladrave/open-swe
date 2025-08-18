# Open SWE CLI How-To

This guide shows how to run the Open SWE CLI and includes examples for common tasks.

## Setup

1. Generate a `.env` file:
   ```bash
   python scripts/setup_env.py
   ```
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
   The planner proposes a plan:
   ```text
   planner Plan
   1. Initialize project
   2. Add React entry point
   ```
   Use ←/→ to approve or deny.
4. After approving, the developer view streams actions:
   ```text
   developer created package.json
   developer added src/App.tsx
   developer updated index.html
   ```

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
   You'll see a planner summary similar to:
   ```text
   planner Plan
   1. Scaffold Express API
   2. Create SQLite schema
   3. Build React UI
   ```
4. Approve each step and monitor the developer log as files and commands execute.

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

