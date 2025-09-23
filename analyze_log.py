# analyze_log.py
import os
from collections import Counter

log_file = r"C:\Users\sheil\gig_delivery\FileOrganizer.log"
summary = Counter()
skipped_files = Counter()
zips_created = []

if not os.path.exists(log_file):
    print(f"Log file not found: {log_file}")
else:
    print(f"Reading log file: {log_file}")
    try:
        encodings = ['utf-8', 'utf-16']
        for encoding in encodings:
            try:
                with open(log_file, 'r', encoding=encoding) as f:
                    lines = f.readlines()
                    break
            except UnicodeDecodeError:
                continue
        else:
            print("Error: Could not decode log file with UTF-8 or UTF-16")
            lines = []

        for line in lines:
            if "Moved" in line and "to" in line:
                if "FileOrganizer.ps1" in line or "analyze_log.py" in line:
                    continue
                folder = line.split("to")[-1].strip().split('\\')[-1]
                summary[folder] += 1
                print(f"Found move: {line.strip()}")
            elif "Skipped" in line and "already exists" in line:
                file = line.split("Skipped ")[1].split(" - ")[0].strip()
                skipped_files[file] += 1
                print(f"Found skip: {line.strip()}")
            elif "Created zip" in line:
                zips_created.append(line.split("Created zip:")[-1].strip())
                print(f"Found zip: {line.strip()}")

    except Exception as e:
        print(f"Error reading log file: {e}")

    print("\nFile Move Summary:")
    if not summary:
        print("No files moved.")
    else:
        for folder, count in summary.items():
            print(f"{folder}: {count} file{'s' if count > 1 else ''}")
    if skipped_files:
        print("\nSkipped Files:")
        for file, count in skipped_files.items():
            print(f"{file}: {count} time{'s' if count > 1 else ''}")
    if zips_created:
        print("\nZips Created:")
        for zip_file in zips_created:
            print(zip_file)

# ... (keep existing code) ...

# Visualize with matplotlib
import matplotlib.pyplot as plt

if summary or skipped_files:
    folders = list(summary.keys())
    moves = list(summary.values())
    skips_total = sum(skipped_files.values())
    skips_label = 'Skips' if skips_total > 0 else None

    fig, ax = plt.subplots()
    ax.bar(folders, moves, color='blue', label='Moved')
    if skips_label:
        ax.bar(['Total'], [skips_total], color='red', label='Skipped')
    ax.set_ylabel('Count')
    ax.set_title('File Organization Stats')
    ax.legend()
    plt.show()
else:
    print("No data for visualization.")