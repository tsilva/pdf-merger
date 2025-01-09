# 📄 PDF Merger

<p align="center">
  <img src="logo.jpg" alt="PDF Merger Logo" width="400"/>
</p>

> 🚀 Effortlessly merge related PDF files with smart auto-detection and batch processing

## ✨ Features

- 🤖 Smart detection of related PDF files by name patterns
- 🔄 Interactive merge confirmation system
- 📊 Real-time progress tracking
- 📝 Detailed logging
- 🛡️ Safe file handling with collision detection
- ⚡ Fast and efficient processing

## 🛠️ Installation

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

## 🚀 Usage

Simply point the script to your PDF directory:

```bash
python main.py /path/to/pdf/directory
```

### What it does:
1. 🔍 Scans directory for PDF files
2. 🤝 Groups related files (e.g., "report-1.pdf", "report-2.pdf")
3. ❓ Asks for your confirmation
4. ✨ Creates clean merged files with ".merged.pdf" suffix

## 📚 Example

Given a directory with:
```
📄 document-1.pdf
📄 document-2.pdf
📄 document-3.pdf
📄 other.pdf
```

The magic happens:
1. 🔍 Finds the related "document" files
2. 💬 Asks if you want to merge them
3. ✨ Creates "document.merged.pdf"
4. ⏩ Skips unrelated files automatically

## 📝 License

This project was developed in collaboration with `claude-3.5-sonnet` and is available under the [MIT License](LICENSE) 📜
