# FreeIAM Web (`freeiam.web`)

Web integration components for [FreeIAM](https://freeiam.org/).

This repository provides the separately installable **`freeiam.web`** distribution,
which exposes the Python package `freeiam.web` under the shared `freeiam`
[PEP 420 namespace](https://peps.python.org/pep-0420/).

## Installation

```sh
pip install freeiam.web
```

## Development

```sh
uv venv
source .venv/bin/activate
uv pip install --group dev -e .
make test
make build
```

## Documentation

See the [FreeIAM documentation](https://docs.freeiam.org/) and the
[upstream FreeIAM repository](https://github.com/Free-IAM/freeiam).
Project-specific Sphinx sources are in `docs/`.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

## License

Dual-licensed under the [MIT](LICENSES/MIT.txt) or
[Apache-2.0](LICENSES/Apache-2.0.txt) license.
