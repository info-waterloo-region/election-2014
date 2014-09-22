import config
import gspread
import json

# Get worksheet (w) from Google
g = gspread.login(config.user, config.password)
s = g.open(config.news)
w = s.get_worksheet(0)

# Get worksheet values as list (l) of dictionaries (d)
# Create dictionary (e) with data nested under municipality (m) and office (o)
# (Ordering of municipalities, offices, and candidates is done in spreadsheet)
# Convert to json (j) and write to file (f)
l = w.get_all_records()
e = []
for d in l:
  d["Tags"] = d["Tags"].split(",")
  e.append(d)
f = open("headlines.json", "wb")
j = json.dumps(e, sort_keys=False, indent=2)
print >> f, j

