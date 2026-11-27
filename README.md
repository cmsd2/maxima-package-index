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
| [fullsimp](https://github.com/QMeqGR/fsimp-maxima) | Search Maxima's simplification routines for the simplest equivalent form of an expression |
| [json_tools](https://github.com/maxima-project-on-github/maxima-packages) | JSON utilities for Maxima |
| [low_discrepancy](https://github.com/maxima-project-on-github/maxima-packages) | Low-discrepancy sequences for Maxima |
| [maxima-core-docs](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables |
| [maxima-core-docs-de](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables in German, from Maxima's translated manual; install beside maxima-core-docs |
| [maxima-core-docs-es](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables in Spanish, from Maxima's translated manual; install beside maxima-core-docs |
| [maxima-core-docs-ja](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables in Japanese, from Maxima's translated manual; install beside maxima-core-docs |
| [maxima-core-docs-pt](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables in Portuguese, from Maxima's translated manual; install beside maxima-core-docs |
| [maxima-core-docs-pt-br](https://github.com/cmsd2/maxima-core-docs) | Reference documentation for Maxima built-in functions and variables in Brazilian Portuguese, from Maxima's translated manual; install beside maxima-core-docs |
| [mochi](https://github.com/cmsd2/mochi) | Read Modelica models into Maxima symbolic equations via rumoca |
| [numericalmethods](https://github.com/ramaniji/numericalMethods) | Numerical methods for Maxima CAS |
| [numerics](https://github.com/cmsd2/maxima-numerics) | NumPy-like numerical computing for Maxima (SBCL only) |
| [numerics-sundials](https://github.com/cmsd2/maxima-numerics-sundials) | SUNDIALS ODE/DAE solvers for Maxima numerics |
| [padics](https://github.com/josanvallejo/padics) | A package for computing with p-adic numbers in Maxima CAS |
| [permutations](https://github.com/cmsd2/maxima-permutations) | Permutation groups for Maxima, built on cl-permutation (SBCL only) |
| [polyfit](https://github.com/maxima-project-on-github/maxima-packages) | Polynomial fitting for Maxima |
| [qm-maxima](https://github.com/QMeqGR/qm-maxima) | Quantum mechanics calculations using the Maxima CAS |
| [reactive](https://github.com/cmsd2/maxima-reactive) | Named, bounded parameters for Maxima that drive sliders and interactive plots |
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
