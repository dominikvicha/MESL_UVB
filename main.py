from pathlib import Path

# cílové složky se bubdou měnit a ne vždy budou stejné - nejspíše bude potřebovat z toho udělat proměnnou 
cam_files_path = Path("Cam_files")

# konotrola toho, že se načetly všechny hnc soubory
hnc_files_found = list(cam_files_path.glob("*.hnc"))
print(f"Počet nalezených CAM programů: {len(hnc_files_found)}\n")

# validace toho, že jsou všechny hnc soubory načteny
confirmation = input("Souhlasí počet nalezených CAM souborů? Ano/Ne:")
if confirmation.lower() == "ano":
    print("Pokračuji..")
else:
    print("Zkonotroluj znovu cestu k souborům a spusť program znovu.")


def find_tools():
    
    for file in hnc_files_found:
        
        with open(file, "r", encoding="utf-8") as f:
            tools = []
            
            for line in f:
                if line.startswith("T") and line[1:].strip().isdigit():
                    tools.append(line.strip())
        
                elif "G21" in line:
                    break
        
        #print(f"--- Obsah souboru: {file.name} ---")
        #print(content)
        #print("-" * 30)    
        
        
        





