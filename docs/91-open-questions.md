# Open Questions

## Game File Access

- How will the indexer locate the local EU4 installation?
- Should the game path be configured by environment variable, config file, or CLI argument?
- Should source files be copied into an indexing workspace or read directly?

## Game Version Detection

- How should the game version be detected?
- Should the indexer require manual version input?
- Should source root hashing be enough for reproducibility?

## Parser Scope

- How much of Paradox script syntax should be parsed in v0?
- Should unknown blocks be preserved as raw structures?
- Should the parser aim for correctness first or broad tolerance first?

## Localisation

- Which languages should be indexed initially?
- Should English localisation be required?
- Should unresolved localisation keys be allowed in API responses?

## API and MCP

- Should REST and MCP be implemented at the same time?
- Which functions should exist first?
- Should REST be considered a compatibility adapter for Custom GPT Actions?

## Future Expansion

- Which EU4 domain follows missions and decisions?
- Should Victoria 3 be added after EU4 missions/decisions are stable?
- What abstractions are safe to move into core after the first game adapter works?

## Legal and Hosted Data

- What contact path should be used for rights-holder takedown or modification requests?
- Which targeted query endpoints and response fields should the initial hosted service expose?
- Should complete generated database downloads remain permanently out of scope, or only out of scope for the initial hosted version?
- What attribution text should be shown in API responses or documentation?
- Should hosted data include localisation text, script fragments, or only normalized explanations?
