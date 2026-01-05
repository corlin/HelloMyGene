[English](README.md) | [中文](README_zh.md)

# HelloMyGene (Personal Genetic Analysis System)

HelloMyGene is a FastAPI-based personal genetic analysis system. It allows users to upload genotype data files (.txt format) and use AI to generate detailed genetic health reports, including disease risks, drug responses, and hereditary traits.

## ✨ Key Features

- **Genotype Data Upload**: Supports uploading common raw genotype data files (.txt).
- **Intelligent Analysis**: Parses genetic loci and combines them with a built-in knowledge base for health risk assessment.
- **Visual Reports**: Provides intuitive interactive HTML reports.
- **PDF Export**: Supports exporting genetic reports to PDF format for easy saving and sharing.
- **Localization Support**: Perfectly supports Chinese report generation.

## 📚 Genetic Knowledge Base

HelloMyGene includes a comprehensive database of genetic markers covering the following key areas:

### 1. ACMG59 Genetic Screening
Screening for 59 actionable hereditary conditions based on the ACMG (American College of Medical Genetics and Genomics) SF v3.2 guidelines:
- **Hereditary Cancer Syndromes**: Hereditary Breast/Ovarian Cancer (BRCA1/2), Lynch Syndrome, Li-Fraumeni Syndrome (TP53), etc.
- **Cardiovascular Diseases**: Long QT Syndrome, Familial Hypercholesterolemia (LDLR), Hypertrophic Cardiomyopathy, etc.

### 2. Pharmacogenomics (PGx)
Covers metabolism and response predictions for **53 common drugs**, based on CPIC and PharmGKB guidelines:
- **Cardiovascular**: Warfarin, Clopidogrel, Statins.
- **Neuropsychiatric**: SSRIs (Antidepressants), Opioids (Codeine, Tramadol).
- **Oncology/Immunology**: Tacrolimus, Fluorouracil, Thiopurines.
- **Anti-infectives**: Voriconazole, Isoniazid, etc.

### 3. Polygenic Risk Scores (PRS)
Assess genetic susceptibility to complex diseases using GWAS data:
- **Tumor Susceptibility (17 types)**: Lung, Liver, Gastric, Colorectal, Prostate, Breast, Thyroid Cancer, etc.
- **Chronic Disease Risks (62 types)**:
    - **Cardiovascular**: Coronary Heart Disease, Hypertension, Atrial Fibrillation, Stroke.
    - **Endocrine/Metabolic**: Type 2 Diabetes, Hyperlipidemia, Gout, Hypothyroidism.
    - **Immune/Orthopedic**: Rheumatoid Arthritis, SLE, Ankylosing Spondylitis, Osteoarthritis.
    - **Neuro/Psych**: Alzheimer's, Parkinson's, Migraine, Depression susceptibility.

### 4. Traits & Wellness
- **Nutrition & Metabolism**: Alcohol/Caffeine metabolism, Lactose Intolerance, Vitamin (A/B12/C/D/E) & Mineral (Ca/Fe/Zn) needs.
- **Sports Genetics**: Power/Endurance potential (ACTN3), Weight loss response to exercise, Injury risk (Achilles/Ligament), Recovery speed.
- **Skin Traits**: Anti-glycation/Anti-oxidation capacity, Freckle susceptibility, Skin elasticity, Tanning ability.
- **Psychological Traits**: Stress tolerance (COMT), Empathy, Novelty seeking, Circadian rhythm (Chronotype).
- **Other Traits**: Absolute pitch, Earwax type (Wet/Dry), Taste sensitivity, etc.

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
