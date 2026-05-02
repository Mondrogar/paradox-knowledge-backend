# Paradox Knowledge Backend

Paradox Knowledge Backend is a tool-oriented backend for parsing, indexing and explaining mechanics defined in Paradox game files.

The first supported game is Europa Universalis IV. The first MVP vertical slice focuses on explaining EU4 missions and decisions from local game files.

This MVP is a validation slice, not the product boundary.

The long-term goal is a reusable knowledge backend for Paradox games, exposed through API/tool interfaces usable by LLM clients such as Custom GPTs, LibreChat agents, MCP clients or other assistant runtimes.

## Initial MVP

The initial MVP validates the end-to-end flow:

1. Read local EU4 game files.
2. Parse mission and decision definitions.
3. Resolve localisation where possible.
4. Store extracted entities in SQLite.
5. Track source files, hashes and game version.
6. Expose indexed data through REST/OpenAPI and MCP tools.
7. Return grounded explanations with source references.

## Out of Scope for MVP

The first MVP does not include:

- savegame parsing
- Reddit or wiki ingestion
- full multi-game support
- a UI
- universal Paradox framework abstractions
- campaign strategy coaching based on live save state

## Planned Direction

After the EU4 missions/decisions slice works, the project may expand to:

- EU4 ideas, events, modifiers and government reforms
- savegame-aware checks
- Victoria 3 as the second supported game
- richer MCP tools
- hosted API deployment

## Project Status

This is a personal, non-commercial community project for experimenting with game-file parsing, knowledge backends, API/tool design and LLM integrations.

The repository contains the source code and documentation for the tool. The project may also operate a public hosted instance populated from supported game files so the community can search, inspect and explain game-defined mechanics.

The public repository does not include a full generated game-data database or copied vanilla game file dumps by default.

## Legal Notice

This is an unofficial community project and is not affiliated with, endorsed by, sponsored by, or approved by Paradox Interactive.

Paradox Interactive, Europa Universalis IV, Victoria 3 and related names, logos and trademarks are the property of their respective owners.

The project is intended for interoperability, analysis, search and explanation of game-defined mechanics. It does not distribute game binaries, complete game installations, or artwork.

If you are a rights holder and believe that hosted data or project content should be removed or changed, please open an issue or contact the maintainer.

## License

The source code and project documentation in this repository are licensed under the MIT License.

This license applies only to this project's own code and documentation. It does not grant rights to Paradox Interactive game files, localisation text, artwork, trademarks, or other third-party content.