# Backend Folder Structure and Usage Guide

This document explains the purpose and usage of each main folder in the backend, and how they interact to support development.

---

## .devcontainer/

**Purpose:** Provides configuration for Visual Studio Code Dev Containers, enabling a consistent, containerized development environment for all contributors.

**Usage:**

- Contains `devcontainer.json`, which defines the base image, features (Azure CLI, azd, Node.js), forwarded ports, and recommended VS Code extensions (Python, Jupyter, Azure, etc.).
- When you open the project in VS Code and select "Reopen in Container," the environment is built and configured automatically.
- Ensures all developers have the same tools and extensions for Python, Jupyter, Azure, and frontend development.

---

## main.py

**Purpose:** Entry point for the FastAPI application.

**Usage:** Initializes the FastAPI app, includes routers, and starts the server. All API requests are routed through this file.

---

## agents/

**Purpose:** Contains logic for your multi-agent system (e.g., D&D agents).

**Usage:**

- Define classes and functions for each agent (e.g., `DnDAgent`).
- Agents encapsulate behaviors, decision-making, and interactions.
- Called by API endpoints or services to process user input and generate responses.

---

## services/

**Purpose:** Integrations with Azure and other external services.

**Usage:**

- Implement clients or wrappers for Azure APIs (e.g., Content Understanding, Agent API).
- Services handle authentication, API calls, and data transformation.
- Agents or routers use these services to access external capabilities.

---

## config/

**Purpose:** Centralized configuration and environment management.

**Usage:**

- Store settings, secrets, and environment variable logic (e.g., `settings.py`).
- Import configuration in other modules to access API keys, endpoints, or feature flags.
- Keeps sensitive and environment-specific data out of the codebase.

---

## routers/

**Purpose:** API route definitions for FastAPI.

**Usage:**

- Organize endpoints by feature or resource (e.g., `agent_router.py` for agent actions).
- Each router handles HTTP requests, validates input, and calls agents/services as needed.
- Routers are included in `main.py` to expose them as part of the API.

---

## How They Interact

- **Routers** receive HTTP requests and act as the interface between the frontend and backend logic.
- Routers call **agents** to process user input, make decisions, or generate responses.
- Agents may use **services** to access Azure or other external APIs for advanced capabilities.
- All modules use **config** to securely access settings and secrets.
- The application is started and managed via **main.py**, which ties everything together.

This modular structure keeps your backend organized, maintainable, and scalable as your application grows.
