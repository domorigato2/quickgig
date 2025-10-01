import os
import re
from datetime import datetime

# Directory with .nc files
cnc_dir = "/mnt/c/Users/sheil/gig_delivery/Organized/CNC"
log_dir = "/mnt/c/Users/sheil/gig_delivery/Organized"

def analyze_gcode():
    results = []
    for file in os.listdir(cnc_dir):
        if file.endswith(".nc"):
            file_path = os.path.join(cnc_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.readlines()
                    for line in content:
                        # Match G01 commands (e.g., G01 X76 Y76 F785)
                        match = re.match(r'G01\s+X([\d.]+)\s+Y([\d.]+)\s+F([\d.]+)', line.strip())
                        if match:
                            x, y, f = match.groups()
                            results.append(f"{file}: Valid G01 move to X{x}, Y{y} at feedrate F{f}")
            except Exception as e:
                results.append(f"{file}: Error reading file - {str(e)}")
    # Save results to log
    log_file = os.path.join(log_dir, f"gcode_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(log_file, 'w') as f:
        f.write("\n".join(results))
    print(f"G-code analysis saved to {log_file}!")

if __name__ == "__main__":
    analyze_gcode()
