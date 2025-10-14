import csv
import json

links = []

with open("tree_cover_loss_by_driver.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        links.append({
            "source": row["loss_year"],
            "target": row["drivers_type"],
            "value": float(row["loss_area_ha"])
        })

with open("sankey_links.json", "w") as jsonfile:
    json.dump(links, jsonfile, indent=2)
