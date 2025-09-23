# analyze_log.py
import os
from collections import Counter

log_file = r"C:\Users\sheil\gig_delivery\FileOrganizer.log"
summary = Counter()

if not os.path.exists(log_file):
    print(f"Log file not found: {log_file}")
else:
    with open(log_file, 'r') as f:
        for line in f:
            if "Moved" in line:
                folder = line.split("to")[-1].strip()
                summary[folder] += 1

    print("File Move Summary:")
    for folder, count in summary.items():
        print(f"{os.path.basename(folder)}: {count} files")