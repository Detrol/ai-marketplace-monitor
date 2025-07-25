#!/usr/bin/env python3
"""
Enkel test för att verifiera svenska stödet
"""

def test_swedish_support():
    print("🇸🇪 Testar svenskt språkstöd för AI Marketplace Monitor\n")
    
    # Läs config.toml
    with open('src/ai_marketplace_monitor/config.toml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Test 1: Svenska översättningar
    print("📝 Test 1: Svenska översättningar")
    if '[translation.sv]' in content:
        print("  ✅ Svenska översättningssektionen finns")
        
        # Kontrollera några nycklar
        svenska_ord = ['Skick', 'Beskrivning', 'Detaljer', 'Platsen är ungefärlig']
        for ord in svenska_ord:
            if ord in content:
                print(f"  ✅ '{ord}' - översättning finns")
            else:
                print(f"  ❌ '{ord}' - översättning saknas")
    else:
        print("  ❌ Svenska översättningssektionen saknas")
    
    print()
    
    # Test 2: Svenska regionen
    print("🗺️  Test 2: Svenska regionen")
    if '[region.swe]' in content:
        print("  ✅ Svenska regionsektionen finns")
        
        svenska_städer = ['Stockholm', 'Göteborg', 'Malmö']
        for stad in svenska_städer:
            if stad in content:
                print(f"  ✅ '{stad}' - stad finns i regionen")
            else:
                print(f"  ❌ '{stad}' - stad saknas")
        
        if 'SEK' in content:
            print("  ✅ 'SEK' - svensk valuta finns")
        else:
            print("  ❌ 'SEK' - svensk valuta saknas")
    else:
        print("  ❌ Svenska regionsektionen saknas")
    
    print()
    
    # Test 3: Exempel-filer
    print("📄 Test 3: Exempel-filer")
    
    try:
        with open('docs/svenska_config_exempel.toml', 'r', encoding='utf-8') as f:
            exempel_content = f.read()
        if 'language = \'sv\'' in exempel_content:
            print("  ✅ Svenskt konfigurationsexempel finns")
        else:
            print("  ❌ Svenskt konfigurationsexempel saknar språkinställning")
    except FileNotFoundError:
        print("  ❌ Svenskt konfigurationsexempel saknas")
    
    try:
        with open('docs/README_sv.md', 'r', encoding='utf-8') as f:
            readme_content = f.read()
        if 'Svenska' in readme_content:
            print("  ✅ Svensk README finns")
        else:
            print("  ❌ Svensk README finns men innehållet verkar saknas")
    except FileNotFoundError:
        print("  ❌ Svensk README saknas")
    
    print()
    
    # Test 4: Uppdaterad dokumentation
    print("📚 Test 4: Uppdaterad dokumentation")
    
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            main_readme = f.read()
        if '- `sv`: Swedish' in main_readme:
            print("  ✅ Svenska språket listat i README.md")
        else:
            print("  ❌ Svenska språket saknas i README.md")
    except FileNotFoundError:
        print("  ❌ README.md saknas")
    
    print("\n🎉 Test avslutat! Om alla tester visar ✅ är svenska stödet korrekt implementerat.")

if __name__ == "__main__":
    test_swedish_support()