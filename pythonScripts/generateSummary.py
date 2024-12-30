import pandas as pd

csv_file = "csvDataFiles/Results.csv"
df = pd.read_csv(csv_file)

markdown_table = df.to_markdown(index=False)

# Write the Markdown table to a file for GitHub Actions summary
with open("pythonScripts/workflow_summary.md", "w") as f:
    f.write(f"## CSV Data Summary\n\n")
    f.write(f"{markdown_table}\n")

# Optional: Print to confirm the content
print("Markdown table written to pythonScripts/workflow_summary.md.")
