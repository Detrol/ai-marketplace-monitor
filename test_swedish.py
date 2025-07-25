#!/usr/bin/env python3
"""
Enkel test för att verifiera svenska översättningar
"""

# Simulera översättningsläsning från config.toml
def test_swedish_translations():
    # Läs svenska översättningar från config.toml
    import re
    
    with open('src/ai_marketplace_monitor/config.toml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrahera svenska översättningssektionen
    sv_match = re.search(r'\[translation\.sv\](.*?)(?=\[|\Z)', content, re.DOTALL)
    if not sv_match:
        print("ERROR: Svenska översättningar inte funna i config.toml!")
        return False
    
    sv_section = sv_match.group(1)
    print("Svenska översättningar funna i config.toml:")
    
    # Kontrollera specifika översättningar
    expected_translations = {
        'Condition': 'Skick',
        'Description': 'Beskrivning', 
        'Details': 'Detaljer',
        'Location is approximate': 'Platsen är ungefärlig',
        'About this vehicle': 'Om detta fordon',
        "Seller's description": 'Säljarens beskrivning',
        'Collection of Marketplace items': 'Samling av Marketplace-objekt'
    }
    
    all_found = True
    for english, swedish in expected_translations.items():
        # Kontrollera både ' och " citattecken
        found = (f"'{english}'" in sv_section and f"'{swedish}'" in sv_section) or \
                (f'"{english}"' in sv_section and f'"{swedish}"' in sv_section)
        if found:
            print(f"  ✓ {english} = {swedish}")
        else:
            print(f"  ✗ Översättning saknas: {english} = {swedish}")
            all_found = False
    
    return all_found

def test_swedish_region():
    # Kontrollera svenska regionen
    import re
    with open('src/ai_marketplace_monitor/config.toml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrahera svenska regionen
    swe_match = re.search(r'\[region\.swe\](.*?)(?=\[|\Z)', content, re.DOTALL)
    if not swe_match:
        print("ERROR: Svenska regionen inte funna i config.toml!")
        return False
    
    swe_section = swe_match.group(1)
    print("\nSvenska regionen funna i config.toml:")
    
    # Kontrollera specifika värden
    expected_values = [
        ('full_name', 'Sweden'),
        ('currency', 'SEK'),
        ('Stockholm', 'stockholm'),
        ('Göteborg', 'göteborg'),
        ('Malmö', 'malmö')
    ]
    
    all_found = True
    for key, value in expected_values:
        if value in swe_section or f'"{value}"' in swe_section or f"'{value}'" in swe_section:
            print(f"  ✓ {key}: {value}")
        else:
            print(f"  ✗ Värde saknas: {key}: {value}")
            all_found = False
    
    return all_found

if __name__ == "__main__":
    print("Testar svenska översättningar och regioner...\n")
    
    translations_ok = test_swedish_translations()
    region_ok = test_swedish_region()
    
    if translations_ok and region_ok:
        print("\n✅ Alla tester passerade! Svenska stödet är korrekt konfigurerat.")
    else:
        print("\n❌ Några tester misslyckades. Kontrollera konfigurationen.")