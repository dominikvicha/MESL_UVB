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
                if line[0] == "(" and line[1] == "T" and line[2].isdigit():
                    tools.append(line.strip())
        
                elif "G21" in line:
                    break
        print(f"--- Nástroje nalezené v souboru: {file.name} ---")
        print(tools)
        
        #print(f"--- Obsah souboru: {file.name} ---")
        #print(content)
        #print("-" * 30)    
        
        
def find_meta_data():
    for file in hnc_files_found:
        
        with open(file, "r", encoding="utf-8") as f:
            meta_data = []
            
            for line in f:
                if "Celkovy vyrobni cas - " in line:
                    parts = line.split(" - ")
                    meta_data.append(parts[1].strip(")\n"))
            print(f"--- Výrobní čas nalezený v souboru: {file.name}: {meta_data[0]} ---")
                    
# nemůže být else prootže else u for cyklu se spustí když cyklus doběhned o konce bez přerušení!
            if not meta_data:
                print("Nenalezen výrobní čas u daného souboru.")
        
                    
    



def performance():
    pass        
        
        

if __name__ == "__main__":
    find_tools()    
    find_meta_data()
        





