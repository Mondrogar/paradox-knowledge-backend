"""Tests for the CLI module."""

import subprocess
import sys


def test_cli_help():
    """Test that the CLI help command works."""
    result = subprocess.run(
        [sys.executable, "-m", "paradox_knowledge.cli", "help"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Paradox Knowledge Backend" in result.stdout
    assert "Version:" in result.stdout


def test_cli_version():
    """Test that the CLI version option works."""
    result = subprocess.run(
        [sys.executable, "-m", "paradox_knowledge.cli", "--version"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "0.1.0" in result.stdout


def test_cli_unknown_command():
    """Test that unknown commands are handled gracefully."""
    result = subprocess.run(
        [sys.executable, "-m", "paradox_knowledge.cli", "unknown"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Unknown command:" in result.stdout
