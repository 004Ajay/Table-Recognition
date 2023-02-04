import tabula
import pandas as pd

"""
PLEASE NOTE
→ PDF should have a recognizable tabular data
→ It is good to have single values in each cell, else more post-formatting may need.
→ If your pdf has more than 1 page and you need tables from all of them, pass arg pages='all'
→ If any hash symbol like error comes while opening the CSV, then extend the height & width of cell
"""

file_path = "table_OnePage.pdf" # path to your pdf file
tables = tabula.read_pdf(file_path)

for table in tables:
    df = pd.DataFrame(table)
    print("\nDataFrame:\n", df)
    df.to_csv('CSV/table.csv', index=False) # put index=True, if you want to see index of rows on first col of CSV file