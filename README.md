# Sentiora AI

AI-powered crisis intelligence and situational awareness platform.

## Overview

Sentiora AI ingests trusted public crisis and disaster data, normalizes heterogeneous records, clusters related events using semantic embeddings, calculates interpretable risk scores, and visualizes crisis intelligence through a modern dashboard.

The system is designed as a maintainable engineering-focused academic project rather than a throwaway prototype.

## Core Features

- NOAA/NWS alert ingestion
- GDACS disaster ingestion
- ReliefWeb humanitarian ingestion
- Normalized event schema
- PostgreSQL persistence
- Semantic clustering
- Transparent risk scoring
- FastAPI backend
- React dashboard
- Docker Compose infrastructure

## Tech Stack

### Backend

- FastAPI
- SQLAlchemy 2.x
- PostgreSQL
- Alembic
- AsyncPG

### NLP / ML

- sentence-transformers
- scikit-learn
- LightGBM (planned)

### Frontend

- React
- TypeScript
- Tailwind CSS
- Leaflet

### Infrastructure

- Docker Compose
- Ruff
- Pytest

# Local Development Setup

## Requirements

- WSL2 + Ubuntu
- Docker Desktop
- Python 3.12
- uv
- Node.js LTS

---

# Backend Setup

```bash
cd backend

uv venv
source .venv/bin/activate

uv pip install -r requirements.txt
```

---

# Run Backend Locally

```bash
uvicorn app.main:app --reload
```

---

# Docker Compose

From repository root:

```bash
docker compose up --build
```

---

# API Docs

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Testing

```bash
make check
```

---

# Current Status

Week 1 foundation complete:

- FastAPI backend
- PostgreSQL integration
- Docker infrastructure
- Alembic migrations
- Ruff + pytest workflow

Upcoming:

- NOAA/NWS ingestion
- normalized event storage
- semantic clustering
- risk scoring
- frontend dashboard

---

# License

Academic project for engineering and learning purposes.
