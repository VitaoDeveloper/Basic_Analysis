# Basic_Analysis

A hands-on educational project demonstrating basic exploratory data analysis with **pandas**, using a financial institution's customer dataset.

The project is a single Python script (`main.py`), commented step by step, aiming to be a clear, educational walkthrough of core pandas operations, without relying on machine learning or external APIs.

## About the project

A financial institution wants to reward customers with a good credit history, but the sheer number of customers makes manual review impractical. The script walks through a full exploratory analysis of the customer dataset:

- Reading the dataset (`assets/clientes.csv`) with `pandas`;
- Inspecting the table structure and column types (`info`);
- Computing descriptive statistics for the numeric columns (`describe`);
- Checking for missing values (`isnull`);
- Analyzing the distribution of the `score_credito` column (`value_counts`);
- Comparing average salary, debt, and loans across credit score groups (`groupby`);
- Listing the most common professions among customers with a good score;
- Checking correlations between numeric variables (`corr`);
- Building a list of customers eligible for a benefit (score `Good`) and exporting it to a new CSV file (`to_csv`).

This version replaces the original machine learning pipeline (encoding, classification models, accuracy comparison) and the OpenAI-based report generation with plain pandas operations, keeping the analysis simple and dependency-free.

## Tech stack

- **Python 3**
- **pandas** — data loading, exploration, and manipulation

## Repository structure

```
AI_DataAnalysis/
├── assets/
│   └── clientes.csv          # Customer dataset used for the analysis
├── main.py                   # Main script with the full analysis
├── requirements.txt          # Project dependencies
└── .gitignore
```

## Getting started

### Prerequisites

- Python 3.10+ installed

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/VitaoDeveloper/AI_DataAnalysis.git
   cd AI_DataAnalysis
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .venv\Scripts\activate         # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

The script prints the analysis results to the console and generates `assets/clientes_elegiveis.csv`, containing the IDs of customers eligible for the benefit.

## About the data

The dataset (`clientes.csv`) contains financial and behavioral information for fictional customers — age, profession, annual salary, number of accounts and cards, payment history, total debt, and more — alongside a `score_credito` column (`Good`, `Standard`, `Poor`).

## Context

This project was built as a practical exercise for a lesson on data analysis, focused on core pandas concepts: reading data, descriptive statistics, grouping, filtering, and exporting results.

## License

This project currently has no defined license. Feel free to use it as a study reference.
