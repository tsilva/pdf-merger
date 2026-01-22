<div align="center">
  <img src="logo.png" alt="pdf-merger" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
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
# Install with uv
uv tool install .

# Merge all PDFs in a directory
pdf-merger /path/to/pdfs

# Merge only related file groups
pdf-merger /path/to/pdfs --grouped
```

## Installation

Requires Python 3.7+ and [uv](https://docs.astral.sh/uv/).

```bash
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

## License

[MIT](LICENSE)
