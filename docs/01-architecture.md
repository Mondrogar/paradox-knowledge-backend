# Architecture

## Project Shape

The project is designed as a backend-first knowledge system.

The core should not depend on ChatGPT, MCP, REST, or any specific LLM runtime. LLM-facing integrations are adapters over the same core functions.

## High-Level Flow

```text
Paradox game files
    ↓
parser / extractor
    ↓
normalised entities
    ↓
SQLite catalog
    ↓
core query layer
    ↓
REST API / MCP tools
    ↓
LLM client
```

## Core Principle

Business logic belongs in the core layer.

Transport layers such as REST endpoints and MCP tools should be thin wrappers over core functions.

```text
core function:
  get_mission(...)
  search_decisions(...)
  explain_trigger(...)

REST endpoint:
  calls core function

MCP tool:
  calls core function
```

## Initial Runtime Stack

- Python
- SQLite
- FastAPI
- Python MCP SDK
- Docker-ready project layout

## Storage

SQLite is the primary storage for MVP/v1.

The database should combine:

- relational catalog tables
- JSON columns for parsed structures
- raw source text for audit/debug
- FTS5 search tables where useful
- source file and hash tracking

Storage access should go through repository interfaces so another database can be introduced later if needed.

## Deployment Assumption

The parser/indexer may need access to local game files.

The hosted API/MCP runtime should not require direct access to the game installation. It should operate on a generated SQLite database artifact.