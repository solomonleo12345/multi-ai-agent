# Multi-Agentic System

A modular Python application that integrates a backend service, a frontend UI, and AI agents powered by Groq language models.

## Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
  - [Start Backend Service](#start-backend-service)
  - [Start Frontend UI](#start-frontend-ui)
  - [Invoke AI Agent](#invoke-ai-agent)
- [Testing](#testing)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
```
c:\Users\solom\OneDrive\Documents\projects\2. MULTI AGENTIC SYSTEM
├─ requirements.txt
├─ setup.py
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ backend/
│  │  ├─ __init__.py
│  │  └─ api.py
│  ├─ config/
│  │  ├─ __init__.py
│  │  └─ settings.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ ai_agent.py
│  │  └─ frontend/
│  │     ├─ __init__.py
│  │     └─ ui.py
│  └─ logs/
├─ MULTI_AGENTIC_SYSTEM.egg-info/
│  ├─ dependency_links.txt
│  ├─ PKG-INFO
│  ├─ requires.txt
│  ├─ SOURCES.txt
│  └─ top_level.txt
```

## Prerequisites
- Python 3.11 or newer
- pip (Python package installer)
- Git (to clone the repository)

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/multi-agentic-system.git
   cd multi-agentic-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .   # Install the package in editable mode
   ```

## Configuration
Create a `.env` file in the project root (or set environment variables in your shell) with the required keys:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

> **Note:** The `GROQ_API_KEY` is used by `app.core.ai_agent` to authenticate with the Groq API. The `TAVILY_API_KEY` is used by the `TavilySearch` tool for web look‑ups.

## Running the Application
### Start Backend Service
```bash
python -m app.backend.api
```
The backend exposes REST endpoints and runs on `http://localhost:8000` by default.

### Start Frontend UI
```bash
streamlit run app/frontend/ui.py
```
The UI will be available at `http://localhost:8501`.

### Invoke AI Agent
You can call the helper function from `app.core.ai_agent` directly or via the backend:

```python
from app.core.ai_agent import get_response_from_ai_agents

response = get_response_from_ai_agents(
    llm_id="llama-3.3-70b-versatile",
    query="Explain multi-agent systems",
    allow_search=False,
    system_prompt="You are a helpful assistant."
)
print(response)
```

## Testing
Run the test suite with:
```bash
pytest
```
(Ensure any test files are added under a `tests/` directory.)

## Logging
The application uses `app.common.logger.get_logger`. Logs are written to the `logs/` directory. Example log files include `log_2026-07-14.log`.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes.
4. Push to the branch and open a pull request.

Please follow the existing code style and include unit tests for new functionality.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.