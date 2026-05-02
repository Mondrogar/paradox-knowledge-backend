"""Command-line interface for Paradox Knowledge Backend."""

import argparse
import sys

from paradox_knowledge import __version__


def main() -> None:
    """Paradox Knowledge Backend - Parse, index and explain Paradox game files."""
    parser = argparse.ArgumentParser(
        prog="paradox-knowledge",
        description="Paradox Knowledge Backend - Parse, index and explain Paradox game files.",
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="help",
        help="Command to run (default: help)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"paradox-knowledge {__version__}",
    )

    args = parser.parse_args()

    if args.command == "help":
        print("Paradox Knowledge Backend")
        print(f"Version: {__version__}")
        print("")
        print("Usage: paradox-knowledge [COMMAND]")
        print("")
        print("Commands:")
        print("  help    Show this help message")
        print("")
        print("This is a skeleton implementation. No commands are available yet.")
    else:
        print(f"Unknown command: {args.command}")
        print("Run 'paradox-knowledge help' for usage information.")


if __name__ == "__main__":
    main()
