import pandas as pd

# Path to the CSV file
csv_file = "csvDataFiles/Results.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Convert the DataFrame to an HTML table
table = df.to_html(index=False, escape=False)

# Save the HTML table to a file
with open("pythonScripts/workflow_summary.html", "w") as f:
    f.write(f"<h2>CSV Data Summary</h2>\n")
    f.write(table)

