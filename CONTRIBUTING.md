# Contributing to the Maxima Package Index

Thank you for contributing a package to the Maxima ecosystem!

## Adding a package

1. Fork this repository
2. Add your package entry to `index.json`
3. Submit a pull request

### Package entry format

Each package entry in `index.json` looks like this:

```json
"my-package": {
  "description": "A short description (max 200 characters)",
  "repository": "https://github.com/user/repo",
  "keywords": ["keyword1", "keyword2"],
  "license": "GPL-3.0-or-later",
  "authors": ["Your Name"],
  "source": {
    "type": "git",
    "url": "https://github.com/user/repo.git",
    "ref": "abc123def456789012345678901234567890abcd"
  }
}
```

### Required fields

| Field | Description |
|-------|-------------|
| `description` | One-line summary, max 200 characters |
| `repository` | URL of the source repository |
| `source` | How to download the package (see below) |

### Optional fields

| Field | Description |
|-------|-------------|
| `homepage` | Package homepage if different from repository |
| `keywords` | Array of search keywords |
| `license` | SPDX license identifier |
| `authors` | Array of author names |

### Source types

**Git repository** (works with any git hosting):

```json
{
  "type": "git",
  "url": "https://github.com/user/repo.git",
  "ref": "abc123def456789012345678901234567890abcd",
  "subdir": "optional/subdirectory"
}
```

- `url`: Any clonable git URL (HTTPS or SSH)
- `ref`: **Must be a full commit hash** (40-character hex SHA). This ensures reproducible installs — every user gets exactly the same version of the code. Branch names and tags are not accepted.
- `subdir`: Optional. If the package lives in a subdirectory of a monorepo.

To find the current HEAD commit hash for a repository:
```bash
git ls-remote https://github.com/user/repo.git HEAD
```

**Tarball** (direct download URL):

```json
{
  "type": "tarball",
  "url": "https://example.com/my-package-1.0.tar.gz",
  "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "hash_algorithm": "sha256"
}
```

- `url`: Direct HTTPS URL to a `.tar.gz` archive.
- `hash`: Optional but recommended. SHA-256 hash of the tarball (64-character hex string). When present, mxpm verifies the download against this hash and rejects mismatches.
- `hash_algorithm`: Optional. Currently only `"sha256"` is supported (and is the default if omitted).
- Works with GitHub release assets, S3, SourceForge, or any static file host.

To compute the hash of a tarball:
```bash
sha256sum my-package-1.0.tar.gz
```

### Package naming rules

- 2-64 characters
- Lowercase ASCII letters, digits, hyphens, and underscores
- Must start with a letter
- Must be unique within the index

### Checklist

Before submitting your PR, please verify:

- [ ] `index.json` is valid JSON
- [ ] Package name follows the naming rules
- [ ] `description` is under 200 characters
- [ ] `source` URL is publicly accessible
- [ ] Git source `ref` is a full 40-character commit hash (not a branch or tag name)
- [ ] No duplicate package names
