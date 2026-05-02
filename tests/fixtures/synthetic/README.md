# Synthetic Fixtures

This directory contains synthetic Paradox-like game file fixtures for testing.

## Purpose

Synthetic fixtures are manually created examples that test specific parsing scenarios without requiring actual game files.

## Guidelines

- Keep fixtures small and focused on specific parsing scenarios
- Use Paradox script syntax patterns (blocks, key-value pairs, etc.)
- Include comments explaining what each fixture tests
- Do not copy full game files or localisation dumps
- Avoid real game content that may be copyrighted

## Example Fixture Structure

```
fixtures/
  synthetic/
    eu4/
      missions/
        test_mission_01.txt
      decisions/
        test_decision_01.txt
```

## Future Expansion

As parsing logic develops, fixtures should be added to cover:
- Basic block parsing
- Nested blocks
- Key-value pairs
- Lists and arrays
- Localisation references
- Edge cases and error conditions
