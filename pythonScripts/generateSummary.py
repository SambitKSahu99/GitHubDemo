import pandas as pd

def dataframe_to_markdown(df):
    # Create the markdown table header
    headers = "| " + " | ".join(df.columns) + " |"
    separator = "| " + " | ".join(["---"] * len(df.columns)) + " |"
    # Create markdown table rows
    rows = "\n".join("| " + " | ".join(map(str, row)) + " |" for row in df.values)
    return f"{headers}\n{separator}\n{rows}"

# Path to the CSV file
csv_file = "csvDataFiles/Results.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Convert the DataFrame to a markdown table and print it
print("## CSV Data Summary\n")
print(dataframe_to_markdown(df))
