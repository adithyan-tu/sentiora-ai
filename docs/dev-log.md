# Sentiora AI — Week 1 Development Log

## Project

Sentiora AI — AI-Powered Crisis Intelligence and Situational Awareness Platform

## Week

Week 1 — Engineering Foundation and Environment

---

# Day 1 — Environment Setup and Repository Initialization

## Learning Completed

- WSL2 development workflow
- Docker Desktop with WSL2 backend
- Python virtual environments using uv
- Node.js and npm setup
- Git and GitHub workflow
- Environment variable basics
- Importance of reproducible engineering environments

## Features Built

- WSL2 Ubuntu environment
- Docker Desktop integration
- Python 3.12 installation
- uv package manager setup
- Node.js LTS setup
- GitHub repository initialization
- Initial project folder structure

## Repository Structure Created

```text
sentiora-ai/
├── backend/
├── frontend/
├── data/
│   ├── raw/
│   ├── processed/
│   └── labels/
├── docs/
├── models/
├── notebooks/
├── docker-compose.yml
├── README.md
├── .env.example
└── .gitignore
```

## Commands Run

```bash
wsl --install
docker version
uv --version
node --version

git init
git add .
git commit -m "chore: initialize Sentiora AI project structure"
```

## Verification

- WSL2 functioning correctly
- Docker working inside Ubuntu
- Repository pushed to GitHub
- Initial project structure established

## Bug or Blocker

None

## Next Action

Begin FastAPI backend skeleton implementation.

---

# Day 2 — FastAPI Backend Skeleton

## Learning Completed

- REST API fundamentals
- FastAPI architecture
- OpenAPI/Swagger documentation
- API routing concepts
- Pydantic and type hints

## Features Built

- FastAPI application factory
- `/health` endpoint
- `/version` endpoint
- centralized API router
- CORS middleware setup
- initial test suite

## Backend Structure

```text
backend/app/
├── api/
│   ├── routes/
│   │   ├── health.py
│   │   └── version.py
│   └── router.py
├── core/
└── main.py
```

## Commands Run

```bash
uv venv
source .venv/bin/activate

uv pip install fastapi uvicorn[standard] pydantic-settings pytest httpx

uvicorn app.main:app --reload
pytest
```

## Verification

- Backend server starts successfully
- Swagger UI accessible
- `/health` returns OK
- `/version` endpoint operational
- Initial pytest suite passes

## Bug or Blocker

Minor Python import path issues fixed by running commands inside backend directory.

## Next Action

Implement centralized configuration and logging.

---

# Day 3 — Configuration and Structured Logging

## Learning Completed

- Environment-based configuration
- Secret hygiene
- Pydantic settings management
- Structured logging concepts
- Application metadata separation

## Features Built

- centralized settings module
- `.env` configuration loading
- structured JSON logging
- metadata configuration module
- improved backend startup lifecycle

## New Modules Added

```text
backend/app/core/
├── config.py
├── logging.py
└── metadata.py
```

## Commands Run

```bash
uv pip install python-json-logger

uvicorn app.main:app --reload
pytest
```

## Verification

- `.env` values load correctly
- structured logs visible in console
- metadata appears in Swagger docs
- all tests passing

## Example Log Output

```json
{
  "levelname": "INFO",
  "message": "Application initialized successfully"
}
```

## Bug or Blocker

None

## Next Action

Add PostgreSQL integration and Alembic migrations.

---

# Day 4 — PostgreSQL and Alembic

## Learning Completed

- PostgreSQL fundamentals
- relational schema design
- SQLAlchemy ORM concepts
- Alembic migration workflow
- async database architecture

## Features Built

- PostgreSQL database integration
- SQLAlchemy 2.x async engine
- async session management
- Alembic migration setup
- Source model
- Event model
- DB-aware health endpoint

## Database Models

```text
backend/app/db/
├── base.py
├── session.py
└── models/
    ├── source.py
    └── event.py
```

## Commands Run

```bash
sudo apt install postgresql postgresql-contrib -y

alembic init alembic

alembic revision --autogenerate -m "create sources and events tables"

alembic upgrade head
```

## Verification

- PostgreSQL database operational
- migrations applied successfully
- tables created:
  - sources
  - events
  - alembic_version

- backend connects successfully to DB

## Bug or Blocker

Initial migration confusion between local PostgreSQL and containerized PostgreSQL later resolved during Docker setup.

## Next Action

Containerize backend infrastructure using Docker Compose.

---

# Day 5 — Docker Compose Infrastructure

## Learning Completed

- Docker containerization
- Docker Compose orchestration
- container networking
- persistent Docker volumes
- backend-to-database networking

## Features Built

- backend Dockerfile
- Docker Compose stack
- PostgreSQL container
- persistent database volume
- containerized backend workflow

## Infrastructure

```text
Docker Compose
├── sentiora_backend
└── sentiora_postgres
```

## Commands Run

```bash
docker compose build
docker compose up

docker ps

docker exec -it sentiora_postgres psql -U sentiora -d sentiora_db
```

## Verification

- backend container operational
- PostgreSQL container operational
- backend connects using Docker service name
- health endpoint functional inside containerized environment

## Important Engineering Fix

Alembic migrations had to be rerun inside Dockerized PostgreSQL because local and containerized databases are isolated systems.

## Bug or Blocker

Docker PostgreSQL initially contained no tables because migrations had only been applied locally.

## Resolution

```bash
docker exec -it sentiora_backend bash
alembic upgrade head
```

## Next Action

Add engineering discipline tooling: Ruff, pytest automation, Makefile workflow.

---

# Day 6 — Testing, Ruff, and Workflow Automation

## Learning Completed

- Ruff linting
- Ruff formatting
- automated developer workflows
- Makefile automation
- engineering discipline practices

## Features Built

- Ruff configuration
- formatting workflow
- linting workflow
- Makefile automation
- shared pytest fixture structure
- improved backend testing workflow

## New Files Added

```text
backend/
├── Makefile
└── pyproject.toml
```

## Commands Run

```bash
uv pip install ruff

ruff check .
ruff check . --fix
ruff format .

make check
```

## Verification

- Ruff linting passes
- Ruff formatting passes
- pytest suite passes
- Makefile commands operational

## Bug or Blocker

`make` initially missing from Ubuntu environment.

## Resolution

```bash
sudo apt install make
```

Additional issue:

- Makefile missing or incorrectly formatted initially.

Resolved by:

- creating correct `Makefile`
- using TAB indentation instead of spaces.

## Next Action

Stabilize Week 1 infrastructure and improve repository documentation.

---

# Day 7 — Foundation Review and Stabilization

## Learning Completed

- README-driven development
- infrastructure stabilization
- reproducible engineering setup
- architecture review practices

## Features Stabilized

- FastAPI backend
- PostgreSQL integration
- Docker Compose workflow
- Alembic migrations
- Ruff + pytest workflow
- Makefile automation

## Improvements Made

- expanded README
- improved `.gitignore`
- added `.gitkeep` placeholders
- verified Docker workflow
- verified database workflow
- verified WSL path discipline

## Commands Run

```bash
docker compose down
docker compose up --build

make check

git tag week1-foundation
git push origin week1-foundation
```

## Verification

- Docker Compose stack reproducible
- health endpoint operational
- database connectivity verified
- migrations persistent
- automated checks passing
- README sufficient for fresh setup

## Week 1 Milestone Achieved

Completed engineering foundation including:

- FastAPI backend
- PostgreSQL persistence
- Docker infrastructure
- Alembic migrations
- async architecture
- testing workflow
- linting workflow
- reproducible development environment

## Current System Status

```text
Sentiora AI
│
├── FastAPI backend
├── Structured logging
├── PostgreSQL database
├── SQLAlchemy ORM
├── Alembic migrations
├── Docker Compose infrastructure
├── Async architecture
├── Ruff linting
├── pytest workflow
├── Makefile automation
└── Reproducible engineering environment
```

## Next Action

Begin Week 2:

- NOAA/NWS ingestion
- async HTTP clients
- ingestion adapters
- normalized event ingestion pipeline
- raw payload persistence
