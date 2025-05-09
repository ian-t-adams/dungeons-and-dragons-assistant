# Backend (FastAPI)

## Structure
- `main.py` — FastAPI entry point
- `agents/` — Multi-agent logic
- `services/` — Azure and external service integrations
- `utils/` — Utility functions (logging, helpers, etc.)
- `config/` — Configuration and settings
- `routers/` — API route definitions
- `tests/` — Automated tests

## Local Development: Running Backend & Frontend

### 1. Run the Backend (FastAPI)
1. Open a new Command Prompt window.
2. Navigate to the backend folder:
   ```cmd
   cd c:\Code\dungeons-and-dragons-assistant\backend
   ```
3. (Optional) Create and activate a virtual environment:
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
5. (Optional) Copy the example environment file and set your secrets:
   ```cmd
   copy .env.example .env
   ```
   Edit `.env` to add your Azure keys if needed.
6. Start the FastAPI server:
   ```cmd
   uvicorn main:app --reload
   ```
   By default, this runs at http://127.0.0.1:8000

### 2. Run the Frontend (React)
1. Open a second Command Prompt window.
2. Navigate to the frontend folder:
   ```cmd
   cd c:\Code\dungeons-and-dragons-assistant\frontend
   ```
3. Install dependencies (only needed once):
   ```cmd
   npm install
   ```
4. Start the React development server:
   ```cmd
   npm start
   ```
   This will open http://localhost:3000 in your browser.

### 3. Connect Frontend to Backend
- By default, the React app will try to call the backend at the same host/port.
- For local development, you may need to set up a proxy in `frontend/package.json`:
  ```json
  "proxy": "http://localhost:8000",
  ```
  Add this line (if not present) just before the last curly brace.

### 4. Test the Setup
- Open http://localhost:3000 in your browser.
- Use the Agent Chat component to send a message.
- You should see a response from the FastAPI backend.

### 5. Run Tests (Backend)
```cmd
pytest
```
