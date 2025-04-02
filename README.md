# 📄 pdf-merger

<p align="center">
  <img src="logo.jpg" alt="Logo" width="400"/>
</p>

🔍 A simple CLI tool that intelligently finds and merges related PDF files in a directory

## 📖 Overview

PDF Merger is a command-line utility that identifies PDF files with similar names in a directory and offers to merge them into a single document. It uses pattern matching to group related files (like "document-1.pdf", "document-2.pdf"), asks for confirmation before merging, and creates a new combined PDF while preserving the originals.

## 🚀 Installation

```bash
pipx install . --force
```

## 🛠️ Usage

Run the tool by pointing it to a directory containing PDF files:

```bash
pdf-merger /path/to/your/pdfs
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