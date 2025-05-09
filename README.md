# Dungeons & Dragons Assistant

This project uses FastAPI (Python) for the backend and React for the frontend. It is designed to support multi-agent collaboration for D&D players and dungeon masters, with Azure integration for content understanding, agent APIs, and multimodal capabilities.

## Structure
- `backend/` — FastAPI backend (Python)
- `frontend/` — React frontend (JavaScript/TypeScript)

## Getting Started

### Backend
1. Navigate to the backend folder:
   ```cmd
   cd backend
   ```
2. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```cmd
   uvicorn main:app --reload
   ```

### Frontend
1. Navigate to the frontend folder:
   ```cmd
   cd frontend
   ```
2. (Instructions for React setup will be added after initialization)

---

## Azure Best Practices
- Use Managed Identity for authentication
- Never hardcode credentials; use Azure Key Vault
- Implement error handling and logging
- Prepare for deployment as an Azure Web App or Container App
