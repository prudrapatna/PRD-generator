import csv
import io
import statistics
import math
import re
import json

file_path = '/Users/prudrapatna/.gemini/tmp/prd-generator/tool-outputs/session-d2620239-3ed8-4f4d-97c3-454781019bbe/sheets_gettext_sheets_gettext_1772656587073_0_7pw1cq.txt'

with open(file_path, 'r') as f:
    raw_content = f.read()

try:
    data = json.loads(raw_content)
    content = data.get("output", raw_content)
except json.JSONDecodeError:
    content = raw_content

# Split by sheet names
sheets = re.split(r'Sheet Name:\s*', content)
data_sheet_content = ""
for sheet in sheets:
    if sheet.startswith('Data'):
        data_sheet_content = sheet
        break

reader = csv.reader(io.StringIO(data_sheet_content))
rows = list(reader)

# Find header row
header_row_idx = -1
for i, row in enumerate(rows):
    if any('Self reported Height' in str(cell) for cell in row):
        header_row_idx = i
        break

header = rows[header_row_idx]
sr_idx = -1
m_idx = -1
for i, col in enumerate(header):
    if 'Self reported Height' in str(col):
        sr_idx = i
    if 'Clinically measured Height' in str(col):
        m_idx = i

diff = []
abs_diff = []

for row in rows[header_row_idx+1:]:
    if len(row) > max(sr_idx, m_idx):
        try:
            s_val = float(row[sr_idx])
            m_val = float(row[m_idx])
            error = s_val - m_val
            diff.append(error)
            abs_diff.append(abs(error))
        except ValueError:
            continue

diff.sort()
abs_diff.sort()

def percentile(data, p):
    n = len(data)
    if n == 0:
        return 0
    k = (n - 1) * p / 100.0
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data[int(k)]
    d0 = data[int(f)] * (c - k)
    d1 = data[int(c)] * (k - f)
    return d0 + d1

p1 = percentile(diff, 1)
median_diff = statistics.median(diff)
p99 = percentile(diff, 99)

abs_p1 = percentile(abs_diff, 1)
abs_median = statistics.median(abs_diff)
abs_p99 = percentile(abs_diff, 99)

print(f"Error (Self-Reported - Measured):")
print(f"  1st Percentile: {p1:.2f} inches")
print(f"  Median: {median_diff:.2f} inches")
print(f"  99th Percentile: {p99:.2f} inches")
print(f"")
print(f"Absolute Error (|Self-Reported - Measured|):")
print(f"  1st Percentile: {abs_p1:.2f} inches")
print(f"  Median: {abs_median:.2f} inches")
print(f"  99th Percentile: {abs_p99:.2f} inches")
