# 📄 PDF Merger

<p align="center">
  <img src="logo.jpg" alt="PDF Merger Logo" width="400"/>
</p>

> 🔍 Simple tool to find and merge related PDF files in a directory

## ✨ Features

- 📁 Finds PDF files with similar names
- 💬 Asks before merging files
- 📊 Shows merge progress
- 📝 Keeps you informed with logs
- 🛡️ Checks for existing files

## 🛠️ Installation

```bash
git clone https://github.com/tsilva/pdf-merger.git
cd pdf-merger
curl -L https://gist.githubusercontent.com/tsilva/258374c1ba2296d8ba22fffbf640f183/raw/venv-install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

```bash
curl -L https://gist.githubusercontent.com/tsilva/8588cb367242e3db8f1b33c42e4e5e06/raw/venv-run.sh -o run.sh && chmod +x run.sh && ./run.sh
```

### How it works:
1. 🔍 Looks for PDF files in your directory
2. 📋 Groups files with similar names
3. ❓ Checks with you before merging
4. 📄 Creates the merged PDF

## 📚 Example

Your files:
```
📄 document-1.pdf
📄 document-2.pdf
📄 document-3.pdf
📄 other.pdf
```

What happens:
1. 🔍 Spots the related "document" files
2. 💬 Asks if you want them merged
3. 📄 Creates "document.merged.pdf"
4. ➡️ Leaves other files alone

## 📝 License

This project is available under the [MIT License](LICENSE) 📜

