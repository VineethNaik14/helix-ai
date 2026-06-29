# Helix AI

> AI-powered codebase understanding platform built with FastAPI, PostgreSQL, Qdrant, and Sentence Transformers.

Helix AI indexes software repositories, extracts code metadata using Abstract Syntax Trees (AST), generates semantic embeddings, and enables natural language search across source code using vector search.

---

# Features

* Repository indexing
* Recursive project scanning
* Python AST parsing
* Function extraction
* Class extraction
* Import extraction
* PostgreSQL metadata storage
* Sentence Transformer embeddings
* Qdrant vector database integration
* Semantic code search API
* Dependency graph generation

---

# Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic

### AI

* Sentence Transformers
* all-MiniLM-L6-v2
* Qdrant

### DevOps

* Docker
* Docker Compose

---

# Project Structure

```
helix-ai/

├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── embeddings/
│   ├── graphs/
│   ├── indexing/
│   ├── parsers/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── vectorstore/
│   ├── app.py
│   └── main.py
│
├── scripts/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/VineethNaik14/helix-ai.git
cd helix-ai
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Start PostgreSQL

Create a PostgreSQL database.

Create and update your `.env` file with the database credentials.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/helix
```

Create the database tables.

```bash
python -m scripts.create_tables
```

---

# Start Qdrant

Run Docker.

Start Qdrant.

```bash
docker compose up -d
```

Dashboard:

```
http://localhost:6333/dashboard
```

---

# Run the API

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Index Repository

```
POST /api/v1/repositories
```

Request

```json
{
    "path": "your path"
}
```

---

## List Indexed Repositories

```
GET /api/v1/repositories
```

---

## Search Functions

```
GET /api/v1/search/functions
```

Example

```
/api/v1/search/functions?name=scan
```

---

## Semantic Search

```
POST /api/v1/search/semantic
```

Request

```json
{
    "query": "Where is the repository scanned?"
}
```

Example Response

```json
[
    {
        "score": 0.44,
        "name": "scan",
        "file": "app/indexing/scanner.py",
        "line": 19
    }
]
```

---

# How It Works

1. The repository is scanned recursively.
2. Programming languages are detected.
3. Python files are parsed using the AST module.
4. Metadata for functions, classes, and imports is extracted.
5. Metadata is stored in PostgreSQL.
6. Semantic embeddings are generated using Sentence Transformers.
7. Embeddings are indexed into Qdrant.
8. Natural language queries are converted into embeddings.
9. Qdrant returns the most semantically similar code.
10. Results are returned through the REST API.

---

# Current Capabilities

* Python repository indexing
* Function extraction
* Class extraction
* Import extraction
* Semantic search
* Dependency graph generation

---

# Author

### **`Vineeth Naik`**
