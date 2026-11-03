# Kerno

Python interface, Rust execution core for AI runtimes.

Kerno is an early development scaffold. The Python package loads a compiled Rust extension through PyO3. The initial public API exposes `kerno.__version__`; task execution and model integrations are planned.

## Architecture

Python owns the public interface, configuration, and typing. Rust owns execution components. PyO3 connects the two languages, and maturin builds the native Python package.

```text
python/kerno/    Public Python package and type information
src/lib.rs      Rust extension: kerno._core
tests/          Package integration tests
scripts/        Installed-wheel validation
Cargo.toml      Rust dependencies and the shared package version
pyproject.toml  Python metadata, build configuration, and development tools
```

## Requirements

- Python 3.13 or 3.14 for the initial test matrix.
- Rust stable with Cargo, rustfmt, and Clippy. The declared minimum Rust version is 1.85; CI uses stable.
- [uv](https://docs.astral.sh/uv/) for Python environments, dependencies, and builds.
- Native compiler tools for your platform: Apple Command Line Tools, Linux build tools, or Visual Studio Build Tools with C++.

## Development setup

```sh
git clone https://github.com/Gabrielbsb21/kerno.git
cd kerno
uv python install 3.13
uv sync --locked --reinstall-package kerno
uv run python -c "import kerno; print(kerno.__version__)"
```

The setup command creates `.venv` and compiles the extension. It does not require environment activation. Run it again after removing native artifacts or recreating the environment.

After changing Rust source, rebuild the editable extension:

```sh
uv run maturin develop
```

Use a release build for performance measurements:

```sh
uv run maturin develop --release
```

## Checks

```sh
uv run cargo fmt --check
uv run cargo clippy --all-targets -- -D warnings
uv run cargo test
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Run Cargo through `uv run` so PyO3 uses the project's Python interpreter. The integration tests check native imports, version consistency, and packaged type information. Runtime behavior tests will accompany runtime implementation.

## Build and test distributions

```sh
uv build --no-sources
uv run python scripts/check_wheel.py
```

The build produces a source distribution and a platform-specific wheel in `dist/`. The validation script requires exactly one wheel there. It installs that wheel in an isolated environment outside the checkout and runs the package integration tests. If `dist/` contains older wheels, move them elsewhere before validation. To select another interpreter, pass `--python 3.14` to the script after building its matching wheel.

The version is defined in `Cargo.toml` and supplied to Python metadata by maturin. Commit both `Cargo.lock` and `uv.lock`.

## Continuous integration

The [CI workflow](.github/workflows/ci.yml) runs on pull requests and pushes to `main`. It tests Python 3.13 and 3.14 on Linux, macOS, and Windows, including distribution builds and installed-wheel tests. Rust and Python lint checks run on Linux with Python 3.13. This is the configured test matrix; check each workflow run for its actual results. CI does not publish packages.

## Next steps

1. Define the first text request, configuration, result, and error contracts.
2. Implement the Python-to-Rust execution path with deterministic integration tests.
3. Integrate one model provider.
4. Add asynchronous execution, timeouts, cancellation, and concurrency limits.

## Contributing

Use English for project content. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance.

## License

Kerno is available under the [MIT License](LICENSE).
