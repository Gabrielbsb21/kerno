"""Run integration tests against one built wheel outside the source checkout."""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    """Install the wheel into an isolated environment and run the package tests."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--python",
        default=f"{sys.version_info.major}.{sys.version_info.minor}",
        help="Python version used to install and test the wheel.",
    )
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    wheels = list((repository / "dist").glob("*.whl"))
    if len(wheels) != 1:
        parser.error(f"Expected one wheel in dist/, found {len(wheels)}.")

    with tempfile.TemporaryDirectory(prefix="kerno-wheel-") as directory:
        subprocess.run(
            [
                "uv",
                "run",
                "--isolated",
                "--no-project",
                "--python",
                arguments.python,
                "--with",
                str(wheels[0]),
                "--with",
                "pytest>=9,<10",
                "python",
                "-m",
                "pytest",
                str(repository / "tests"),
                "-q",
            ],
            cwd=directory,
            check=True,
        )


if __name__ == "__main__":
    main()
