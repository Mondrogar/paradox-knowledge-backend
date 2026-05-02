# Agent Instructions

These instructions apply to all AI coding agents working in this repository.

This project is a Python-first Paradox game-file knowledge backend. The first supported game is Europa Universalis IV, and the MVP focuses on explaining EU4 missions and decisions from game files.

Read the project documentation before making architectural changes:

- `README.md`
- `docs/01-architecture.md`
- `docs/02-mvp-scope.md`
- `docs/03-legal-and-data-policy.md`
- `docs/90-decisions.md`
- `docs/91-open-questions.md`

## Working Guidelines

### Communication style

Lead with the answer, not the reasoning.

Be clear and appropriately detailed for the complexity of the topic. If one sentence is enough, do not use three. This applies to messages, not to the thoroughness of code changes.

Include code snippets in messages when they provide useful context.

### Implementation philosophy

Choose the approach that correctly and completely solves the problem.

Do the work a careful senior developer would do, including relevant edge cases. Be thorough, but do not gold-plate.

### Implementation quality

Do not optimize for the fastest-looking implementation.

Avoid two common failure modes:

1. Quick-and-dirty code that only works for the happy path.
2. Overengineered code that adds unnecessary layers, abstractions, configuration, frameworks or speculative future-proofing.

Implement the smallest clean solution that fully satisfies the requested scope.

Code should be:

- correct for the requested behavior
- readable
- testable where practical
- maintainable without unnecessary abstraction
- explicit about real failure boundaries

Do not add generic engines, plugin systems, factory layers, broad configuration systems, or multi-game abstractions before the first concrete EU4 vertical slice works.

If a simple direct implementation is enough, use it.

If a more structured implementation is needed, keep the structure proportional to the problem being solved.

### Code readability

Code should be easy to follow for a beginner-to-intermediate Python developer.

Prefer explicit names, straightforward control flow and small focused modules.

Avoid clever one-liners, unnecessary indirection, deep inheritance, factory-heavy designs and function-over-function layering unless they solve a real problem.

Readable and boring code is preferred over clever code.

### Scope

Match the scope of changes to what was requested.

Address closely related issues when fixing them is clearly the right thing to do. If adjacent code is broken or directly contributes to the problem being solved, fix it.

Do not add unrelated features, refactor unrelated code, or “improve” things that were not asked for.

### Error handling

Add error handling at real boundaries where failures can occur:

- file I/O
- filesystem path handling
- user input
- configuration
- database access
- network calls
- cross-service communication

Do not add defensive checks for scenarios that cannot happen given the current architecture.

### Abstraction

Use judgment when extracting repeated code.

Extract code when duplication creates real maintenance risk or hides intent.

Do not create abstractions just because two or three simple lines look similar. Prefer clear local code over premature generalization.

### Security and dependency hygiene

Follow secure coding practices.

Do not commit secrets, API keys, tokens, credentials, local environment files or private paths.

Do not add new dependencies casually. Prefer standard library solutions where they are clear and sufficient. When adding a dependency, choose maintained packages with reasonable adoption and security posture.

### Subagent / explore tasks

These guidelines apply equally to subagent and explore workflows.

Do the complete job. Do not gold-plate, but do not leave work half-done.

## Project Architecture Rules

### Core first

Business logic belongs in the core layer.

REST endpoints and MCP tools must be thin adapters over core functions.

```text
core function:
  search_missions(...)
  get_mission(...)
  explain_trigger(...)

REST endpoint:
  calls core function

MCP tool:
  calls core function
```

### Python-first stack

The MVP stack is:

- Python
- SQLite
- FastAPI
- Python MCP SDK
- Docker-ready runtime

Do not rewrite the project to TypeScript, MongoDB, MSSQL or another primary stack unless a project decision explicitly changes this.

### Storage

SQLite is the primary storage for MVP/v1.

Use SQLite as a generated, read-heavy catalog with:

- relational tables
- JSON columns for parsed structures
- raw source text where useful for audit/debug
- source file and hash tracking
- FTS5 where useful

Keep storage access behind repository/query interfaces so the database can be replaced later if needed.

### Docker

The project should be Docker-ready from the beginning.

Docker must support reproducible runtime and future deployment, but it should not block early parser development.

SQLite databases should be mounted as volumes or bind mounts.

Local game files should be mounted read-only when indexing.

## Data and Legal Rules

Follow `docs/03-legal-and-data-policy.md`.

The public repository should contain source code, documentation, schemas, configuration, synthetic fixtures and empty/example databases.

Do not commit by default:

- full copied vanilla game files
- complete generated game-data databases
- bulk localisation dumps
- game binaries
- artwork
- complete game installations
- secrets or private local paths

Synthetic test fixtures are preferred.

The project may later operate a public hosted instance populated from supported game files, but that does not mean bulk extracted game data belongs in the repository.

## MVP Scope

The MVP is a vertical slice, not the final product boundary.

Initial MVP target:

```text
Explain EU4 missions and decisions from game files.
```

In scope for MVP:

- EU4 missions
- EU4 decisions
- parser/indexer flow
- localisation resolution where practical
- SQLite catalog
- source file and game version tracking
- REST/OpenAPI adapter
- MCP adapter

Out of scope for MVP unless explicitly requested:

- savegame parsing
- Reddit/wiki ingestion
- full multi-game implementation
- frontend/UI
- universal Paradox framework abstractions
- hosted multi-user product features

## Documentation Updates

Update documentation when implementation changes project behavior, scope, architecture or accepted decisions.

Use:

- `docs/90-decisions.md` for accepted decisions
- `docs/91-open-questions.md` for unresolved questions
- relevant topic docs for durable design details

Do not use `AGENTS.md` as the main project specification. Keep detailed project knowledge in `docs/`.