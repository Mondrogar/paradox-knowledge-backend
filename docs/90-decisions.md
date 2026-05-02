# Decision Log

## D001: Start with EU4 as the first supported game

Status: Accepted

Europa Universalis IV is the first supported game because it is stable, well understood, locally available, and provides a good test domain for Paradox game-file parsing.

The project should not be designed as EU4-only. EU4 is the first adapter and validation target.

Victoria 3 is a likely second supported game.

## D002: MVP is a vertical slice, not the final product boundary

Status: Accepted

The MVP target is to explain EU4 missions and decisions from game files.

This does not define the final scope of the project. It exists to validate the parser, storage, API, MCP and explanation flow end to end.

## D003: Use SQLite for MVP/v1

Status: Accepted

SQLite is the primary storage for MVP/v1.

Reasons:

- generated read-heavy catalog
- one portable database file
- low operational overhead
- suitable for local development and rebuilds
- supports relational tables, JSON columns and FTS5
- avoids premature DB server complexity

The storage layer should use repository interfaces so the database can be replaced later if needed.

## D004: Do not use MongoDB for MVP

Status: Accepted

MongoDB is not selected for MVP.

Parsed data may be stored as JSON, but the project still needs catalog-style querying, source tracking, versioning, localisation lookup and entity relationships.

SQLite with JSON columns gives enough flexibility without adding a separate database server.

## D005: Docker-ready from the beginning

Status: Accepted

The project should be Docker-ready from the beginning.

Docker should support reproducible runtime and future deployment to VPS/cloud.

The SQLite database should be mounted as a volume or bind mount.

Local game files should be mounted read-only when indexing.

Docker must not block early parser development.

## D006: Use MIT License for project code and documentation

Status: Accepted

The project source code and project-owned documentation are licensed under the MIT License.

The MIT License applies only to this project's own code and documentation. It does not grant rights to third-party game files, localisation text, artwork, trademarks or other content owned by their respective rights holders.

## D007: Keep the public repository unpopulated by default

Status: Accepted

The public repository should contain the tool source code, documentation, schemas, configuration, synthetic fixtures and empty/example databases.

The repository should not include full copied vanilla game files, complete generated game-data databases, bulk localisation dumps, game binaries, artwork or complete game installations by default.

## D008: Allow a public hosted populated service as a project direction

Status: Accepted

The project may operate a public hosted instance populated from supported game files.

The hosted instance is intended for non-commercial community use, including search, analysis and explanation of game-defined mechanics for players, modders and other community users.

The hosted service should be clearly marked as unofficial and should not imply affiliation, endorsement, sponsorship or approval by Paradox Interactive.

## D009: Do not provide bulk generated database downloads in the initial hosted version

Status: Accepted

The initial hosted service should focus on targeted search, lookup and explanation.

It should not initially provide bulk downloads of the complete generated game-data database.

This keeps the first public version focused on interoperability, analysis and explanation rather than redistribution of a complete extracted dataset.