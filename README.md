<div align="center">
  <img src="logo.png" alt="pdf-merger" width="512"/>

  [![PyPI](https://img.shields.io/pypi/v/pdf-merger.svg)](https://pypi.org/project/pdf-merger/)
  [![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **📄 Intelligently find and merge related PDF files with a single command 🔗**

</div>

## Overview

pdf-merger is a CLI tool that scans directories for PDF files and merges them together. It can combine all PDFs into one file or intelligently group related files by name pattern (e.g., "report-1.pdf", "report-2.pdf") and merge each group separately.

## Features

- **Smart grouping** - Automatically detects related PDFs by filename patterns (`doc-1.pdf`, `doc-2.pdf` → merged)
- **Two merge modes** - Merge all PDFs or only related file groups
- **Interactive prompts** - Optional confirmation before each merge operation
- **Preserves originals** - Source files are never modified or deleted
- **Progress tracking** - Visual progress bars for batch operations

## Quick Start

```bash
# Install from PyPI
pip install pdf-merger

# Merge all PDFs in a directory
pdf-merger /path/to/pdfs

# Merge only related file groups
pdf-merger /path/to/pdfs --grouped
```

## Installation

Requires Python 3.12+.

```bash
# From PyPI (recommended)
pip install pdf-merger

# Or with pipx for isolated install
pipx install pdf-merger

# Or from source with uv
git clone https://github.com/tsilva/pdf-merger.git
cd pdf-merger
uv tool install .
```

## Usage

### Default Mode

Merges all PDF files alphabetically into a single `merged_all.pdf`:

```bash
pdf-merger /path/to/directory
```

### Grouped Mode

Merges only files with similar names. Files like `invoice-1.pdf`, `invoice-2.pdf`, `invoice-3.pdf` become `invoice.merged.pdf`:

```bash
pdf-merger /path/to/directory --grouped
```

### Interactive Mode

Add `--ask` to confirm before each merge:

```bash
pdf-merger /path/to/directory --ask
pdf-merger /path/to/directory --grouped --ask
```

### Example Output

```
Found potentially related PDFs for 'document':
  1. document-1.pdf
  2. document-2.pdf
  3. document-3.pdf

Would you like to merge these files? [Y/n]:
```

## Pattern Matching

The grouping algorithm matches files with trailing numeric suffixes:

| Files | Base Name | Output |
|-------|-----------|--------|
| `report-1.pdf`, `report-2.pdf` | report | `report.merged.pdf` |
| `doc_3.pdf`, `doc_4.pdf` | doc | `doc.merged.pdf` |
| `scan 1.pdf`, `scan 2.pdf` | scan | `scan.merged.pdf` |

Supported separators: `-`, `_`, and spaces.

## Programmatic API

You can also use pdf-merger as a library:

```python
from pdf_merger import merge_pdfs, merge_all_pdfs, batch_merge_pdfs_grouped

# Merge specific files
merge_pdfs(["/path/to/file1.pdf", "/path/to/file2.pdf"], "/path/to/output.pdf")

# Merge all PDFs in a directory
merge_all_pdfs("/path/to/directory")

# Merge grouped PDFs by name pattern
batch_merge_pdfs_grouped("/path/to/directory")
```

## License

[MIT](LICENSE)
