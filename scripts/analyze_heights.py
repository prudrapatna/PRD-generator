import csv
import io
import math
import statistics
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
    if sheet.startswith('Data\n'):
        data_sheet_content = sheet[5:]
        break

if not data_sheet_content:
    print("Could not find 'Data' sheet content.")
    exit(1)

reader = csv.reader(io.StringIO(data_sheet_content))
rows = list(reader)

# Find header row
header_row_idx = -1
for i, row in enumerate(rows):
    if any('Self reported Height' in str(cell) for cell in row):
        header_row_idx = i
        break

if header_row_idx == -1:
    print("Could not find headers.")
    exit(1)

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
diff = []

for row in rows[header_row_idx+1:]:
    if len(row) > max(sr_idx, m_idx):
        try:
            s_val = float(row[sr_idx])
            m_val = float(row[m_idx])
            self_rep.append(s_val)
            meas.append(m_val)
            diff.append(s_val - m_val)
        except ValueError:
            continue

n = len(self_rep)
if n == 0:
    print("No valid data pairs found.")
    exit(1)

mean_sr = statistics.mean(self_rep)
mean_meas = statistics.mean(meas)
mean_diff = statistics.mean(diff)
std_diff = statistics.stdev(diff) if n > 1 else 0

mae = sum(abs(d) for d in diff) / n
rmse = math.sqrt(sum(d**2 for d in diff) / n)

# Pearson correlation
mean_s = mean_sr
mean_m = mean_meas
cov = sum((self_rep[i] - mean_s) * (meas[i] - mean_m) for i in range(n)) / (n - 1) if n > 1 else 0
std_s = statistics.stdev(self_rep) if n > 1 else 1
std_m = statistics.stdev(meas) if n > 1 else 1
corr = cov / (std_s * std_m) if std_s * std_m != 0 else 0

print(f"Number of valid pairs: {n}")
print(f"Mean Self-Reported: {mean_sr:.2f}")
print(f"Mean Measured: {mean_meas:.2f}")
print(f"Mean Difference (Self - Measured): {mean_diff:.4f} inches")
print(f"Standard Deviation of Difference: {std_diff:.4f} inches")
print(f"Mean Absolute Error (MAE): {mae:.4f} inches")
print(f"Root Mean Square Error (RMSE): {rmse:.4f} inches")
print(f"Pearson Correlation: {corr:.4f}")

# Differences breakdown
diff_counts = {}
for d in diff:
    d_round = round(d, 2)
    diff_counts[d_round] = diff_counts.get(d_round, 0) + 1

print("\nValue counts of differences (rounded to 2 decimal places):")
for k in sorted(diff_counts.keys()):
    print(f"{k}: {diff_counts[k]}")
