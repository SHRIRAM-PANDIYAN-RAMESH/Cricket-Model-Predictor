import os
import yaml
import pandas as pd

folder_path = r"C:\Users\rames\Desktop\WARPE_Programs\Web_Scraping_Automation_Project_2\data\raw"

matches = []

for filename in os.listdir(folder_path):

    if filename.endswith(".yaml"):

        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:

                data = yaml.safe_load(file)

                info = data["info"]

                teams = info.get("teams", ["Unknown", "Unknown"])

                outcome = info.get("outcome", {})
                toss = info.get("toss", {})

                row = {
                    "team1": teams[0],
                    "team2": teams[1],
                    "winner": outcome.get("winner", "No Result"),
                    "venue": info.get("venue", ""),
                    "city": info.get("city", ""),
                    "date": info.get("dates", [""])[0],
                    "toss_winner": toss.get("winner", "")
                }

                matches.append(row)

        except Exception as e:
            print(f"Error in {filename}: {e}")

df = pd.DataFrame(matches)

df.to_csv(r"C:\Users\rames\Desktop\WARPE_Programs\Web_Scraping_Automation_Project_2\data\processed\matches.csv", index=False)

print(f"{len(df)} matches saved.")
