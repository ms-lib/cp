import os

root_dir = "/Users/mahative/Documents/CLAUDE/CW/CP/CP-Mothers-Day"

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Find the line with **Status:**
            status_index = -1
            for i, line in enumerate(lines):
                if "**Status:**" in line:
                    status_index = i
                    break
            
            if status_index != -1:
                # We found it. Now let's remove it and everything after.
                new_lines = lines[:status_index]
                
                # Check if there's a '---' before it that should be removed too
                # Usually there's an empty line and then ---
                while new_lines and (new_lines[-1].strip() == "---" or not new_lines[-1].strip()):
                    new_lines.pop()
                
                # Write back
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                print(f"Cleaned: {filepath}")
