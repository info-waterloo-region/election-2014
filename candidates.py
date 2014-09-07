import config
import gspread
import csv
import json

from collections import OrderedDict

# Get worksheet (w) from Google
g = gspread.login(config.user, config.password)
s = g.open(config.spreadsheet)
w = s.get_worksheet(0)

# Get worksheet values as list (l) of lists and write to csv file (f)
l = w.get_all_values()
f = open("candidates.csv", "wb")
c = csv.writer(f, quoting=2)
c.writerows(l)

# Get worksheet values as list (l) of dictionaries (d)
# Create dictionary (e) with data nested under municipality (m) and office (o)
# (Ordering of municipalities, offices, and candidates is done in spreadsheet)
# Convert to json (j) and write to file (f)
l = w.get_all_records()
e = OrderedDict()
for d in l:
  m = d.pop("Municipality").strip()
  if m not in e:
    e[m] = OrderedDict()
  o = d.pop("Office").strip()
  if o not in e[m]:
    e[m][o] = []
  e[m][o].append(d)
f = open("candidates.json", "wb")
j = json.dumps(e, sort_keys=False, indent=2)
print >> f, j

