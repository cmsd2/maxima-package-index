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
| [ax-plots](https://github.com/cmsd2/ax-plots) | Interactive Plotly.js plotting for Maxima via Aximar |
| [clifford](https://github.com/dprodanov/clifford) | Clifford algebra for CAS Maxima |
| [dataframes](https://github.com/cmsd2/maxima-dataframes) | Pandas-like tabular data for Maxima (SBCL only) |
| [diophantine](https://github.com/sdemarre/maxima-diophantine) | Solver for Diophantine equations |
| [diophantine-system](https://github.com/maxima-project-on-github/maxima-packages) | Diophantine system solver for Maxima |
| [json_tools](https://github.com/maxima-project-on-github/maxima-packages) | JSON utilities for Maxima |
| [low_discrepancy](https://github.com/maxima-project-on-github/maxima-packages) | Low-discrepancy sequences for Maxima |
| [maxima-core-docs](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables |
| [numericalmethods](https://github.com/ramaniji/numericalMethods) | Numerical methods for Maxima CAS |
| [numerics](https://github.com/cmsd2/maxima-numerics) | NumPy-like numerical computing for Maxima (SBCL only) |
| [numerics-sundials](https://github.com/cmsd2/maxima-numerics-sundials) | SUNDIALS ODE/DAE solvers for Maxima numerics |
| [padics](https://github.com/josanvallejo/padics) | A package for computing with p-adic numbers in Maxima CAS |
| [polyfit](https://github.com/maxima-project-on-github/maxima-packages) | Polynomial fitting for Maxima |
| [qm-maxima](https://github.com/QMeqGR/qm-maxima) | Quantum mechanics calculations using the Maxima CAS |
| [reactive](https://github.com/cmsd2/maxima-reactive) | First-class signals for Maxima — identity-bearing parameter objects that survive symbolic processing and resolve to numeric values on demand. |
| [superq](https://github.com/maxima-project-on-github/maxima-packages) | Superquadric surfaces for Maxima |
| [texify](https://github.com/maxima-project-on-github/maxima-packages) | TeX formatting utilities for Maxima |
| [timedate_middleendian](https://github.com/maxima-project-on-github/maxima-packages) | Middle-endian date/time formatting for Maxima |

## Adding a package

Submit a pull request that adds an entry to `index.json`. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the format and requirements.

## Schema

The index format is defined by [schema.json](schema.json) (JSON Schema
draft 2020-12). CI validates all changes against this schema.

## License

CC0-1.0
