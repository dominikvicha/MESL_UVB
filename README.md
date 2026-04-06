# MESL_UVB
Low level of MES system. 


# Machine Utilization Tracker — Project Memory

_Poslední aktualizace: 2025-04-05_

---

## Vstupní data
- **ATCmap log** — jeden soubor = jeden den, název obsahuje datum (formát: `AtcMap_YYYY_MM_DD_0.log`)
- **CAM soubory (.hnc)** — operátor je kopíruje do cílové složky (flash disk → server)
- **Workflow sběru dat** — jednou týdně, operátor ukládá .hnc soubory + ATCmap log
- ATCmap log se ve stroji maže po cca 2 týdnech → nutný pravidelný sběr

---

## Cíle systému
1. **Vytíženost stroje** — hlavní výstup, kolik stroj reálně jel vs. stál
2. **Identifikace programů** — které programy v daný den běžely a kolikrát
3. **CAM čas vs. reálný čas** — porovnání plánovaného a skutečného času výroby
4. **Vytíženost nástrojů** — jak dlouho byl každý nástroj ve vřetenu

---

## Výstup
- **Excel soubor** s grafy — vytíženost, porovnání s plánem, časy nástrojů

---

## Logika párování CAM ↔ ATCmap
- Ze .hnc souboru extrahovat **sekvenci nástrojů** (např. T2 → T4 → T11 → T49 → T62 → T85 → T193)
- Poslední nástroj v sekvenci = **konec cyklu**
- Další výskyt prvního nástroje v ATCmap = **nový cyklus**
- Timestamp .hnc souboru = orientační kotva pro daný den (ne přesný čas spuštění)
- Přesný čas cyklu se bere z ATCmap

---

## Edge Cases
- **Zlomený nástroj** → operátor pokračuje od místa přerušení → řešení: **consecutive deduplication** ATCmap sekvence (sloučí pouze po sobě jdoucí stejné nástroje, zachová legitimní opakování nástroje v jiné operaci)
- **Přerušený běh** → ignorujeme v první verzi
- **Opakující se nástroj v programu** → zachováme, consecutive dedup ho nepoškodí

---

## Technologie
- **Python** — zpracování dat
- **Excel/CSV** — výstup
- **SQLite** — možný upgrade v pozdější verzi

---

## Struktura .hnc souboru
- **Začátek programu:** `G90 G17` → `G21` (vždy po soupisu nástrojů v komentářích)
- **Konec programu:** `M2` nebo `M30`
- **Soupis nástrojů:** komentáře na začátku souboru ve formátu `(T2 D=63. CR=0. - ...)`
- Tyto markery slouží **pouze pro parsování .hnc** — ne pro ATCmap matching

---

## Ukázkový soubor
- ATCmap: `AtcMap_2025_03_31_0.log` — stroj VMX42i XP DS, 31 pocketů
- CAM: `MTP_25_V_01776.hnc` — nástroje: T2 (čelní fréza), T4, T11 (válcové frézy), T49 (navrtávák), T62, T85 (vrtáky), T193 (vystružník)

---

## Pipeline (domluvená architektura)
```
1. Parsovat ATCmap → seznam eventů s timestampem
2. Consecutive deduplication sekvence výměn
3. Rozsekat den na cykly podle poslední nástroj → první nástroj
4. Pro každý cyklus porovnat sekvenci s CAM soubory → identifikovat program
5. Spočítat metriky (čas programu, čas nástrojů, pauzy)
6. Exportovat do Excelu s grafy
```