from tabula import read_pdf
from tabulate import tabulate

# Path to the PDF file
filepath = 'file.pdf'

# Read the PDF and extract tables as dataframes
df_tables = read_pdf(filepath,
                     stream=True,
                     guess=True,
                     pages='all',
                     multiple_tables=True,
                     pandas_options={
                         'header': None
                     }
                )

# Print the number of tables found
print(f"{len(df_tables)} {'tables' if len(df_tables) > 1 else 'table'} found")

# Iterate over each dataframe and print as table
for df_table in df_tables:
    print(tabulate(df_table))
