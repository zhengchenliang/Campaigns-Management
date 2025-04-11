#!/usr/bin/env python3
import json
import csv
import os
import sys

# The variables j2json and j2csv are imported from the fps file

def json_to_csv():
  try:
    # Check if j2json file exists
    if not os.path.exists(j2json):
      print(f"Error: JSON file {j2json} does not exist")
      return 1
    
    # Read JSON file
    with open(j2json, 'r', encoding='utf-8') as f:
      data = json.load(f)
    
    # Write CSV file
    with open(j2csv, 'w', newline='', encoding='utf-8') as csvfile:
      csv_writer = csv.writer(csvfile)
      
      # Write header
      csv_writer.writerow(['Campaign', 'Status'])
      
      # Write data
      for campaign, info in data.items():
        status = "enabled" if info.get('go', False) else "present"
        csv_writer.writerow([campaign, status])
    
    print(f"CSV file successfully created at {j2csv}")
    return 0
  
  except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in {j2json}")
    return 1
  except Exception as e:
    print(f"Error: {str(e)}")
    return 1

if __name__ == "__main__":
  sys.exit(json_to_csv()) 