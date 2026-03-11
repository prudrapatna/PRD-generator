import csv
import io
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

sheets = re.split(r'Sheet Name:\s*', content)
data_sheet_content = ""
for sheet in sheets:
    if sheet.startswith('Data\n'):
        data_sheet_content = sheet[5:]
        break

reader = csv.reader(io.StringIO(data_sheet_content))
rows = list(reader)

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

self_rep = []
meas = []

for row in rows[header_row_idx+1:]:
    if len(row) > max(sr_idx, m_idx):
        try:
            s_val = float(row[sr_idx])
            m_val = float(row[m_idx])
            self_rep.append(s_val)
            meas.append(m_val)
        except ValueError:
            continue

print(f"Self-Reported Min: {min(self_rep)} inches")
print(f"Self-Reported Max: {max(self_rep)} inches")
print(f"Measured Min: {min(meas)} inches")
print(f"Measured Max: {max(meas)} inches")
