from pathlib import Path

cam_files_path = Path("Cam_files")

# konotrola toho, že se načetly všechny hnc soubory
hnc_files_found = list(cam_files_path.glob("*.hnc"))
print(f"Počet nalezených CAM programů: {len(hnc_files_found)}\n")

for file in hnc_files_found:
    
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        
        #print(f"--- Obsah souboru: {file.name} ---")
        #print(content)
        #print("-" * 30)    
        





