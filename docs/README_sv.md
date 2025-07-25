# AI Marketplace Monitor - Svenska

AI Marketplace Monitor med stöd för svenska Facebook Marketplace.

## Snabbstart för svenska användare

### 1. Installation
```bash
pip install ai-marketplace-monitor
playwright install firefox
```

### 2. Konfigurera för svenska
Skapa en konfigurationsfil `~/.ai-marketplace-monitor/config.toml`:

```toml
[ai.openai]
api_key = 'ditt-openai-api-nyckel'
model = "gpt-4o"

[marketplace.facebook]
# Aktivera svenska språket
language = 'sv'
search_region = 'swe'
username = 'ditt-facebook-användarnamn'
password = 'ditt-facebook-lösenord'
notify = 'användare1'

[user.användare1]
email = 'din@email.com'

[notification.gmail]
smtp_username = 'din@email.com'
smtp_password = 'ditt-app-lösenord'

[item.bil]
search_phrases = ['volvo', 'saab', 'bil']
description = "Söker efter svenska bilmärken i bra skick"
keywords = ['växellåda', 'motor']
antikeywords = ['skrot', 'trasig', 'olycka']
max_price = '100000 SEK'
notify = 'användare1'
```

### 3. Kör programmet
```bash
ai-marketplace-monitor
```

## Svenska översättningar

Systemet inkluderar svenska översättningar för:
- `Skick` (Condition)
- `Beskrivning` (Description)
- `Detaljer` (Details)
- `Platsen är ungefärlig` (Location is approximate)
- `Om detta fordon` (About this vehicle)
- `Säljarens beskrivning` (Seller's description)
- `Samling av Marketplace-objekt` (Collection of Marketplace items)

## Svenska städer och regioner

Systemet inkluderar stöd för svenska städer:
- Stockholm
- Göteborg  
- Malmö
- Uppsala
- Umeå

Använd `search_region = 'swe'` eller `search_city = 'stockholm'` etc.

## Valuta
Använd `currency = 'SEK'` för svenska kronor.

## Mer information
Se huvuddokumentationen i [README.md](../README.md) för fullständiga instruktioner.