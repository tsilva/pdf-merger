# 📄 pdf-merger

<p align="center">
  <img src="logo.jpg" alt="Logo" width="400"/>
</p>

🔍 A simple CLI tool that intelligently finds and merges related PDF files in a directory

## 📖 Overview

PDF Merger is a command-line utility that identifies PDF files with similar names in a directory and offers to merge them into a single document. It uses pattern matching to group related files (like "document-1.pdf", "document-2.pdf"), asks for confirmation before merging, and creates a new combined PDF while preserving the originals.

## 🚀 Installation

Install using [pipx](https://pypa.github.io/pipx/):

```sh
pipx install . --force
```

## 🛠️ Usage

After installation, use the `pdf-merger` command:

```sh
pdf-merger /path/to/pdf-directory
```

### Operational Modes

- **Default mode**:  
  Merges all PDF files in the directory (sorted alphabetically) into a single file named `merged_all.pdf`.

- **Grouped mode**:  
  Use the `--grouped` flag to merge only files that can be grouped together (e.g., files with similar names). Each group is merged into its own file.

### Optional Prompt

Add the `--ask` flag to prompt before performing each merge operation.

#### Examples

Merge all PDFs into one file (no prompt):

```sh
pdf-merger /path/to/pdf-directory
```

Merge only grouped PDFs, prompting before each merge:

```sh
pdf-merger /path/to/pdf-directory --grouped --ask
```

The tool will:
1. Scan the directory for PDF files with similar names
2. Group them together (e.g., "report-1.pdf", "report-2.pdf")
3. Ask for confirmation before merging each group
4. Create a new file named "[base-name].merged.pdf" for each group

Example output:
```
Found potentially related PDFs for 'document':
  1. document-1.pdf
  2. document-2.pdf
  3. document-3.pdf

Would you like to merge these files? [Y/n]:
```

If you confirm, it will create "document.merged.pdf" containing all pages from the source files.

## 📄 License

This project is available under the [MIT License](LICENSE)