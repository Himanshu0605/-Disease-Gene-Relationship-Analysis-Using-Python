import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Load the Excel file
df=pd.read_csv("disgenet_21_01_25.csv")

# Create a directory for saving plots if it doesn't exist
os.makedirs("eda_plots_6day_limited", exist_ok=True)

#DAY 1: Basic Inspections & Score Distribution 
print("--- DAY 1: Basic Inspections & Score Distribution ---")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())
print(df.info())

# Graph 1: Distribution of 'score'
plt.figure(figsize=(8, 6))
sns.histplot(df['score'], bins=30, kde=True)
plt.title('Distribution of Association Score')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.savefig("eda_plots_6day_limited/day1_score_distribution.png")
plt.show()
plt.close()

#DAY 2: Top Diseases & Gene DPI Distribution 
print("\nTop Diseases & Gene DPI Distribution ---")

# Graph 2: Top 10 Diseases by Number of Associated Genes
disease_counts = df['disease_name'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
disease_counts.plot(kind='bar')
plt.title('Top 10 Diseases by Number of Associated Genes')
plt.xlabel('Disease Name')
plt.ylabel('Number of Genes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("eda_plots_6day_limited/day2_top_diseases.png")
plt.show()
plt.close()

# Graph 3: Distribution of 'gene_dpi'
if 'gene_dpi' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df['gene_dpi'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Gene-Disease Perturbation Index (DPI)')
    plt.xlabel('Gene DPI')
    plt.ylabel('Frequency')
    plt.savefig("eda_plots_6day_limited/day2_gene_dpi_distribution.png")
    plt.show()
    plt.close()
else:
    print("Column 'gene_dpi' not found.")

# DAY 3: Gene DSI Distribution & DPI vs DSI Scatter Plot 
print("\nGene DSI Distribution & DPI vs DSI Scatter Plot ---")

# Graph 4: Distribution of 'gene_dsi'
if 'gene_dsi' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df['gene_dsi'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Gene-Disease Specificity Index (DSI)')
    plt.xlabel('Gene DSI')
    plt.ylabel('Frequency')
    plt.savefig("eda_plots_6day_limited/day3_gene_dsi_distribution.png")
    plt.show()
    plt.close()
else:
    print("Column 'gene_dsi' not found.")

# Graph 5: Scatter plot of 'gene_dpi' vs 'gene_dsi'
if 'gene_dpi' in df.columns and 'gene_dsi' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='gene_dpi', y='gene_dsi', data=df)
    plt.title('Scatter Plot of Gene DPI vs Gene DSI')
    plt.xlabel('Gene DPI')
    plt.ylabel('Gene DSI')
    plt.savefig("eda_plots_6day_limited/day3_dpi_vs_dsi.png")
    plt.show()
    plt.close()
else:
    print("Columns 'gene_dpi' or 'gene_dsi' not found for scatter plot.")

# DAY 4: Correlation Heatmap 
print("\nCorrelation Heatmap ---")

# Graph 6: Correlation Heatmap of Numerical Features
numerical_cols = df.select_dtypes(include=np.number)
if numerical_cols.shape[1] > 1:
    corr_matrix = numerical_cols.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm')
    plt.title('Correlation Heatmap of Numerical Features')
    plt.savefig("eda_plots_6day_limited/day4_correlation_heatmap.png")
    plt.show()
    plt.close()
else:
    print("Not enough numerical columns to generate a correlation heatmap.")

# DAY 5: Score by Gene Type 
print("\nScore by Gene Type ---")

# Graph 7: Boxplot of 'score' by a categorical gene feature ('gene_type')
if 'gene_type' in df.columns and 'score' in df.columns:
    top_gene_types = df['gene_type'].value_counts().nlargest(5).index
    df_top_types = df[df['gene_type'].isin(top_gene_types)]
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='gene_type', y='score', data=df_top_types)
    plt.title('Score Distribution by Top 5 Gene Types')
    plt.xlabel('Gene Type')
    plt.ylabel('Score')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("eda_plots_6day_limited/day5_score_by_gene_type.png")
    plt.show()
    plt.close()
else:
    print("Columns 'gene_type' or 'score' not found for boxplot.")

# DAY 6: Top Genes by Disease Association & Optional pLI 
print("\nTop Genes by Disease Association & Optional pLI ---")

# Graph 8: Top 10 Genes by Number of Associated Diseases
gene_counts = df['gene_symbol'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
gene_counts.plot(kind='bar')
plt.title('Top 10 Genes by Number of Associated Diseases')
plt.xlabel('Gene Symbol')
plt.ylabel('Number of Diseases')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("eda_plots_6day_limited/day6_top_genes.png")
plt.show()
plt.close()

#Graph 9: Distribution of another relevant gene feature ('gene_pli')
if 'gene_pli' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(df['gene_pli'].dropna(), bins=30, kde=True)
    plt.title('Distribution of pLI Score')
    plt.xlabel('pLI Score')
    plt.ylabel('Frequency')
    plt.savefig("eda_plots_6day_limited/day6_gene_pli_distribution.png")
    plt.show()
    plt.close()
else:
    print("Column 'gene_pli' not found.")

