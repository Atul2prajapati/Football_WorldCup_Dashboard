
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/FIFA_World_Cup_records_and_statistics"
headers = {"User-Agent": "Mozilla/5.0"}

# NOTE: verify=False suppresses TLS verification; in real use you should set verify=True.
response = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

# Get all tables with class 'wikitable sortable'
tables = soup.find_all("table", {"class": ["wikitable", "sortable"]})

# Select the second table (index 1) as you had in your code
table1 = tables[1]

rows = []
flag_urls = []  # <-- we'll collect flag image URLs per row

# Iterate over table rows
for tr in table1.find_all("tr"):
    cells = tr.find_all(["td", "th"])
    # Extract text cells (as you already do)
    row_text = [td.get_text(strip=True) for td in cells]
    rows.append(row_text)

    # Try to get the flag <img> from the first cell in data rows (skip header rows without <td>)
    if cells and cells[0].name == "td":
        img = cells[0].find("img")
        if img and img.has_attr("src"):
            src = img["src"]
            # Wikipedia often uses            # Wikipedia often uses protocol-relative URLs starting with //...
            if src.startswith("//"):
                src = "https:" + src
            flag_urls.append(src)
        else:
            flag_urls.append("")  # no image found
    else:
        # Header row: keep alignment with rows list
        flag_urls.append("")

# Normalize row lengths (to avoid column mismatch errors)
max_cols = max(len(r) for r in rows)
normalized_rows = [r + [""] * (max_cols - len(r)) for r in rows]

# Convert to DataFrame
df = pd.DataFrame(normalized_rows[1:], columns=normalized_rows[0])

# Inject the Flag URL column, aligned to data rows
# The first element in flag_urls corresponds to the header row; drop it to align with df rows.
if len(flag_urls) == len(df) + 1:
    df["Flag URL"] = flag_urls[1:]
else:
    # Fallback alignment if counts differ for some reason
    df["Flag URL"] = flag_urls[:len(df)]

# Preview
print(df.head())
print(df)

# Rename columns to friendlier names
df = df.rename(columns={
    "Pld": "Matches Played",
    "W": "Wins",
    "D": "Draws",
    "L": "Losses",
    "GF": "Goals For",
    "GA": "Goals Against",
    "GD": "Goal Difference",
    "Pts": "Points"
})

# Clean team names (remove footnote markers like [a], [1])
df["Team"] = df["Team"].str.replace(r"\[.*?\]", "", regex=True).str.strip()
df["Team"] = df["Team"].str.replace(r"\s+", " ", regex=True)

# Save to CSV
df.to_csv("fifa_table1.csv", index=False)