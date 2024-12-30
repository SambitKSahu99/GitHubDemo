import pandas as pd
from prettytable import PrettyTable

# Load CSV data
csv_file = "csvDataFiles/Results.csv"
df = pd.read_csv(csv_file)

# Create a PrettyTable instance
table = PrettyTable()

# Set the field names as the column names from the DataFrame
table.field_names = df.columns.tolist()

# Add the rows from the DataFrame to the PrettyTable
for _, row in df.iterrows():
    table.add_row(row.tolist())

# Format the table to be in the proper Markdown format with borders
table_str = str(table)

# Clean up the table output to match the Markdown format
table_markdown = "```\n" + table_str + "\n```"

# Write the table to a Markdown file for GitHub Actions summary
with open("pythonScripts/workflow_summary.md", "w") as f:
    f.write(f"## Result Summary\n\n")
    f.write(f"{table_markdown}\n")

# Optional: Print to confirm the content
print("Markdown table with borders written to pythonScripts/workflow_summary.md.")
