# Maxima Package Index

The community package index for
[mxpm](https://github.com/cmsd2/maxima-mxpm), the Maxima Package
Manager.

This repository contains `index.json`, a machine-readable catalog of
third-party packages for the
[Maxima](https://maxima.sourceforge.io/) computer algebra system.

## Using the index

Install [mxpm](https://github.com/cmsd2/maxima-mxpm/releases), then:

```
mxpm search diophantine
mxpm install diophantine
```

Packages are installed to `~/.maxima/<name>/`. Maxima 5.47+ scans this
directory automatically, so after installing you can simply:

```
(%i1) load("diophantine");
```

## Current packages

| Package | Description |
|---------|-------------|
| clifford | Clifford algebra |
| diophantine | Solver for Diophantine equations |
| diophantine-system | Diophantine system solver |
| json_tools | JSON utilities |
| low_discrepancy | Low-discrepancy sequences |
| numericalmethods | Numerical methods |
| numerics | NumPy-like numerical computing |
| padics | p-adic numbers |
| polyfit | Polynomial fitting |
| qm-maxima | Quantum mechanics calculations |
| superq | Superquadric surfaces |
| texify | TeX formatting utilities |
| timedate_middleendian | Middle-endian date/time formatting |

## Adding a package

Submit a pull request that adds an entry to `index.json`. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the format and requirements.

## Schema

The index format is defined by [schema.json](schema.json) (JSON Schema
draft 2020-12). CI validates all changes against this schema.

## License

CC0-1.0
