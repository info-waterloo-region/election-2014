import config
import gspread
import json
import time

# Get worksheet (w) from Google
g = gspread.login(config.user, config.password)
s = g.open(config.news)
w = s.get_worksheet(0)

# Get worksheet values as list (l) of dictionaries (d)
# Sort list by date
# Create list of headlines (h)
# Convert to json (j) and write to file (f)
l = w.get_all_records()
l = sorted(l, key=lambda d: time.strptime(d["Date"], "%d/%m/%Y"), reverse=True)  
h = []
for d in l:
  d["Tags"] = d["Tags"].split(",")
  d["Date"] = time.strftime("%Y-%m-%d", time.strptime(d["Date"], "%d/%m/%Y"))
  h.append(d)
f = open("headlines.json", "wb")
j = json.dumps(h, sort_keys=False, indent=2)
print >> f, j

