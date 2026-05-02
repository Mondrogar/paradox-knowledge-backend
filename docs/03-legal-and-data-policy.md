# Legal and Data Policy

## Purpose

This document defines how the project treats source code, documentation, generated data, hosted data and third-party game content.

The goal is to support a public, non-commercial community tool while keeping a clear boundary between this project's own code and data derived from supported games.

## Repository Policy

The public repository may contain:

- source code
- documentation
- configuration
- schemas
- API definitions
- MCP tool definitions
- synthetic test fixtures
- empty or example databases

The public repository should not contain by default:

- full copied vanilla game files
- complete generated game-data databases
- bulk localisation dumps
- game binaries
- artwork
- complete game installations
- other large redistributed game assets

## Hosted Data

A public hosted instance may be populated from supported game files to provide search, analysis and explanation features for the community.

Hosted data should be used to answer targeted queries and explain game-defined mechanics.

The hosted service should not initially provide bulk downloads of the complete generated database.

## Generated Data

Generated indexes and SQLite databases are build artifacts.

Local generated databases may contain data derived from a user's own local game installation.

Generated databases should not be committed to the public repository by default.

## Test Fixtures

Automated tests should prefer synthetic Paradox-like fixtures created specifically for this project.

Small excerpts may be used only where necessary for documentation, debugging or compatibility investigation, and should be kept minimal.

## Attribution and Unofficial Status

The project should clearly identify supported games and source versions where relevant.

The project must not imply affiliation, endorsement, sponsorship or approval by Paradox Interactive.

Paradox Interactive, Europa Universalis IV, Victoria 3 and related names, logos and trademarks are the property of their respective owners.

## Takedown Requests

The project should provide a clear contact or issue path for rights-holder concerns.

If a rights holder requests removal or modification of hosted data, the maintainer should review and respond promptly.

## License Boundary

The MIT License applies to this project's own source code and documentation.

It does not apply to third-party game files, localisation text, artwork, trademarks or other content owned by their respective rights holders.