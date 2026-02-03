# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PDF Gluer is a CLI tool and Python library that intelligently finds and merges related PDF files in a directory. It uses `pikepdf` for PDF manipulation and `tqdm` for progress bars.

## Installation & Development

Install the tool using `uv`:
```bash
uv tool install .
```

The project uses:
- **Build system**: Hatchling
- **Python version**: >=3.12
- **Dependencies**: `tqdm`, `pikepdf`

## Running the Tool

After installation, the `pdf-gluer` command is available:

```bash
# Default mode: merge all PDFs into merged_all.pdf
pdf-gluer /path/to/directory

# Grouped mode: merge only files with similar names
pdf-gluer /path/to/directory --grouped

# Ask before each merge operation
pdf-gluer /path/to/directory --ask
pdf-gluer /path/to/directory --grouped --ask
```

## Architecture

The project follows a standard Python package structure:

```
pdf_gluer/
├── __init__.py    # Public API exports
└── core.py        # Core implementation
```

### Package Structure

- **`pdf_gluer/__init__.py`**: Exports public API (`merge_pdfs`, `merge_all_pdfs`, `batch_merge_pdfs_grouped`, `main`)
- **`pdf_gluer/core.py`**: Contains all implementation logic

### Core Functions (in `core.py`)

- **`get_base_name(filename)`**: Strips numeric suffixes from filenames to identify related PDFs (e.g., "doc-1.pdf" and "doc-2.pdf" both become "doc")
- **`group_similar_pdfs(directory)`**: Groups PDF files by their base names, returning only groups with multiple files
- **`merge_pdfs(input_files, output_path)`**: Low-level PDF merging using pikepdf
- **`process_pdf_group(directory, base_name, files, ask)`**: Handles merging a single group with user prompts
- **`batch_merge_pdfs_grouped(input_dir, ask)`**: Processes all groups in a directory (grouped mode)
- **`merge_all_pdfs(input_dir, ask)`**: Merges all PDFs in a directory into a single file (default mode)

### Operational Modes

1. **Default mode** (`merge_all_pdfs`): Alphabetically sorts and merges ALL PDF files in the directory into `merged_all.pdf`
2. **Grouped mode** (`batch_merge_pdfs_grouped`): Only merges files that share a base name, creating separate merged files for each group

The `--ask` flag adds user confirmation prompts before merging in either mode.

### Pattern Matching

The grouping algorithm uses regex `r'[-_ ]+\d+$'` to match files with trailing numeric suffixes separated by hyphens, underscores, or spaces. Examples:
- "report-1.pdf", "report-2.pdf" → base name: "report"
- "doc_3.pdf", "doc_4.pdf" → base name: "doc"

## Important Notes

- **README.md must be kept up to date** with any significant project changes
- Output files are named `[base-name].merged.pdf` in grouped mode
- Output file is `merged_all.pdf` in default mode
- Original files are preserved (never deleted)
- The tool skips groups that already have a merged output file (in grouped mode)

## CI/CD

The project uses GitHub Actions for automated releases:

- **`.github/workflows/release.yml`**: Triggers on `pyproject.toml` changes to main branch
  - Runs tests and PII scan
  - Creates GitHub release with auto-generated notes
  - Publishes to PyPI using trusted publishing
