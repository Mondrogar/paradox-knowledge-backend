# MVP Scope

## MVP Target

Explain EU4 missions and decisions from game files.

This is the first vertical slice, not the endgame of the project.

## Project Vision

Build a Paradox knowledge backend that can parse, index and explain game-defined mechanics from Paradox game files.

Europa Universalis IV is the first supported game because it provides a practical and useful first domain.

Victoria 3 is a likely second supported game.

The long-term goal is not an EU4-only mission explainer. The long-term goal is a reusable backend for Paradox game knowledge, exposed through API and tool interfaces.

## Purpose

The MVP should prove that the system can:

- parse Paradox script-like files
- extract meaningful entities
- resolve localisation
- store parsed data in a searchable catalog
- expose data through REST and MCP
- produce grounded explanations for LLM use

## In Scope

- Europa Universalis IV as the first game
- missions
- decisions
- raw trigger extraction
- raw effect extraction
- human-readable summaries of requirements
- human-readable summaries of rewards
- source file tracking
- source hash tracking
- game version tracking
- SQLite storage
- REST/OpenAPI adapter
- MCP adapter

## Out of Scope

- savegame parsing
- automatic campaign-state evaluation
- Reddit ingestion
- wiki ingestion
- multi-game implementation
- universal Paradox abstraction layer
- frontend/UI
- hosted multi-user product features

## Example Questions

The MVP should eventually support questions like:

- Why is this EU4 mission unavailable?
- What are the requirements for this mission?
- What rewards does this mission give?
- Which decisions are available for forming a country?
- What does this decision require?
- Which source file defines this mission or decision?