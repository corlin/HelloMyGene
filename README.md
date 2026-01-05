[English](README.md) | [中文](README_zh.md)

# HelloMyGene (Personal Genetic Analysis System)

HelloMyGene is a FastAPI-based personal genetic analysis system. It allows users to upload genotype data files (.txt format) and use AI to generate detailed genetic health reports, including disease risks, drug responses, and hereditary traits.

## ✨ Key Features

- **Genotype Data Upload**: Supports uploading common raw genotype data files (.txt).
- **Intelligent Analysis**: Parses genetic loci and combines them with a built-in knowledge base for health risk assessment.
- **Visual Reports**: Provides intuitive interactive HTML reports.
- **PDF Export**: Supports exporting genetic reports to PDF format for easy saving and sharing.
- **Localization Support**: Perfectly supports Chinese report generation.

## 🛠️ Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/) - High-performance Python Web Framework
- **Database**: SQLite (accessed via SQLAlchemy and aiosqlite)
- **Template Engine**: Jinja2
- **PDF Generation**: xhtml2pdf & reportlab
- **Data Processing**: pandas

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (Recommended) or pip

### Installation

If using `uv` (Recommended):

```bash
uv sync
```

Or using `pip`:

```bash
pip install .
```

### Running the Application

Start in development mode (with hot reload):

```bash
uv run uvicorn src.app:app --reload
```

Or run the entry script directly:

```bash
python main.py
```

After the service starts, visit: http://127.0.0.1:8000

## 📖 Usage Guide

1.  Open your browser and visit the home page.
2.  Click the upload area and select your genotype data file (.txt format).
3.  Wait for the system to parse and analyze (usually takes just a few seconds).
4.  View the generated detailed genetic report.
5.  To save, click the "Download PDF" button in the top right corner of the page.

## 📂 Project Structure

```
HelloMyGene/
├── data/               # Data storage
│   └── raw/            # Raw uploaded files
├── src/                # Source code
│   ├── analysis/       # Analysis logic (parser, report generation)
│   ├── database/       # Database models and initialization
│   ├── models/         # Pydantic data models
│   ├── static/         # Static resources (CSS, fonts)
│   ├── web/            # Web frontend (templates)
│   └── app.py          # FastAPI main application
├── main.py             # Startup entry
├── pyproject.toml      # Project configuration and dependencies
└── README.md           # Project documentation
```

## 📝 License

[MIT License](LICENSE)
