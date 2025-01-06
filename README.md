# pdf-merger

<p align="center">
  <img src="logo.jpg" alt="PDF Merger Logo" width="400"/>
</p>

A Python command-line tool to batch merge related PDF files in a directory.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tsilva/pdf-merger.git
cd pdf-merger
```

2. Create conda environment:
```bash
conda env create -f environment.yml
conda activate pdf-merger
```

## Usage

Run the script with a directory containing PDF files:

```bash
python main.py /path/to/pdf/directory
```

The script will:
1. Scan the directory for PDF files
2. Group files with similar names (e.g., "report-1.pdf", "report-2.pdf")
3. Prompt for confirmation before merging each group
4. Create merged files with ".merged.pdf" suffix

## Example

If your directory contains:
```
document-1.pdf
document-2.pdf
document-3.pdf
other.pdf
```

The script will:
1. Identify "document-1.pdf", "document-2.pdf", and "document-3.pdf" as related
2. Prompt you to merge them
3. If confirmed, create "document.merged.pdf"
4. Skip "other.pdf" as it has no related files

## License

This project was developed in collaboration with the `claude-3.5-sonnet` and is made available under the [MIT License](LICENSE).