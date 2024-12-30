import pandas as pd
from prettytable import PrettyTable

csv_file = "GitHubDemo/csvDataFiles/Results.csv"
df = pd.read_csv(csv_file)

table = PrettyTable()
table.field_names = df.columns.tolist()

for _, row in df.iterrows():
    table.add_row(row.tolist())

# Write the table to a Markdown file for GitHub Actions summary
with open("workflow_summary.md", "w") as f:
    f.write(f"## CSV Data Summary\n\n")
    f.write(f"```\n{table}\n```\n")
