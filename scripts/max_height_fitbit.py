import csv
import io
import re
import json

file_path = '/Users/prudrapatna/.gemini/tmp/prd-generator/tool-outputs/session-d2620239-3ed8-4f4d-97c3-454781019bbe/sheets_gettext_sheets_gettext_1772655597178_0_4jkwhz.txt'

with open(file_path, 'r') as f:
    raw_content = f.read()

try:
    data = json.loads(raw_content)
    content = data.get("output", raw_content)
except json.JSONDecodeError:
    content = raw_content

sheets = re.split(r'Sheet Name:\s*', content)
raw_data_sheet = ""
for sheet in sheets:
    if 'Raw Data | PW + Ch6' in sheet:
        raw_data_sheet = sheet
        break
    elif 'Raw Data (Height in mm)' in sheet:
        raw_data_sheet = sheet

# Wait, let's just parse all sheets to find the absolute max for row starting with '100'
max_val = 0
for sheet in sheets:
    reader = csv.reader(io.StringIO(sheet))
    for row in reader:
        if len(row) > 0 and row[0] == '100':
            for val in row[1:]:
                if val.strip():
                    try:
                        v = float(val.replace(',', '').replace('"', ''))
                        if v > max_val:
                            max_val = v
                    except ValueError:
                        pass

print(f"Tallest user: {max_val} mm")
