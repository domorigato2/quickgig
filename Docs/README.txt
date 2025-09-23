File Organizer
=============
This tool organizes files in C:\Users\sheil\gig_delivery into folders based on extension:
- PDFs (.pdf) -> PDFs
- Images (.jpg, .png, .gif) -> Images
- Docs (.doc, .docx, .txt) -> Docs
- Code (.py, .ps1, .js) -> Code

Requirements:
- PowerShell (included with Windows)
- Python 3.12+ (installed at C:\Users\sheil\AppData\Local\Programs\Python\Python312)

Usage:
1. Place files in C:\Users\sheil\gig_delivery
2. Run: .\FileOrganizer.ps1
3. View summary: python .\analyze_log.py
4. Check log: Get-Content .\FileOrganizer.log

Notes:
- Skips FileOrganizer.ps1 and analyze_log.py to prevent moving itself.
- Logs all actions in FileOrganizer.log.