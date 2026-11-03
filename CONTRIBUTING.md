# Contributing to Kerno

Follow the setup, checks, and distribution validation commands in the [README](README.md). Include the commands and their results in pull request descriptions, along with any checks you could not run and the reason.

Keep the public interface and configuration in Python. Implement execution components in Rust and use PyO3 for the native boundary. Include type information for public Python contracts.

Add regression tests for behavior changes. Native or packaging changes require a fresh native build, distribution builds, and installed-wheel tests. Add dependencies only when the implementation needs them.

Write code, documentation, diagnostics, and commit messages in English. Use meaningful names and API docstrings. Keep Markdown prose paragraphs on one source line.

Keep changes focused. Never commit credentials, local environments, or build output. Package publication and merges require explicit maintainer approval.
