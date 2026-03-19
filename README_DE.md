# Ptrade API Dokumentationsprojekt

[中文](./README.md) | Deutsch

**Vollständige Dokumentationsbibliothek für die quantitative Handels-API von Ptrade** — Basierend auf detaillierter Vergleichsanalyse und Nutzungshinweisen dreier Hauptversionen

> Für die lokale Strategievalidierung oder Prototypenentwicklung siehe das Open-Source-Projekt **[SimTradeLab](http://github.com/kay-ou/SimTradeLab)**. Es simuliert den ereignisgesteuerten Mechanismus und die Schnittstellengestaltung von PTrade mit **20–30x+ schnellerem** lokalem Backtesting!

## 🎯 Projektübersicht

Ptrade ist eine von Hengsheng Electronic entwickelte quantitative Handels-API-Plattform, die von mehreren Brokern übernommen und angepasst wird. Dieses Projekt dokumentiert drei Hauptversionen:

- **Dongguan Securities** (V041) — Neueste Funktionsversion
- **Guosheng Securities** (V016) — Stabile Standardversion
- **Community-Version** (V005) — Community-erweiterte Version

## ✨ Projektmerkmale

### 📊 Versionsvergleich auf Basis realer API-Dokumentation
- Technische Unterschiede durch Vergleich dreier Versionsdokumente entdeckt
- Detaillierte Analyse der Funktionsaufrufe und Rückgabewerte
- Upgrade-Leitfaden und Kompatibilitätsempfehlungen

### 🔍 Vollständige Funktionsklassifizierung und Indexierung
- Alle API-Schnittstellen nach Funktion kategorisiert
- Versionsunterstützung klar gekennzeichnet
- Vollständige Strategiebeispiel-Bibliothek

## 🚀 Schnellstart

### 1. Version auswählen

| Broker | Version | Merkmale | Empfohlen für |
|--------|---------|----------|---------------|
| **Dongguan Securities** | V041 | Neueste Funktionen | Professioneller Handel |
| **Guosheng Securities** | V016 | Stabil, zuverlässig | Produktionsumgebung |
| **Community** | V005 | Lernfreundlich | Studium & Forschung |

### 2. Navigation nach Bedarf

#### 🎓 Anfänger
- [📖 Einstiegsanleitung](docs/getting-started/) — Von Grund auf lernen
- [💡 Strategiebeispiele](docs/examples.md) — Aus Code lernen
- [📚 Dokumentationsnavigation](docs/) — Gesamtübersicht

#### 🔍 API nachschlagen
- [📋 API-Referenz](docs/api-reference/) — Vollständige API-Dokumentation
- [🔖 API-Klassifizierungsindex](docs/api-classification.md) — Schnellsuche nach Funktion
- [📊 Branchen-/Konzeptdaten](docs/industry-concept-data.md) — Branchenklassifizierung

#### ⚖️ Versionsunterschiede
- [🔍 Versionsvergleich](docs/version-differences.md) — Technische Unterschiede
- [📊 Versionsdetails](docs/versions/) — Vollständiger Funktionsvergleich
- [📄 Originaldokumente](docs/original/) — Vollständige Original-API-Dokumente

## 📁 Dokumentationsstruktur

```
docs/
├── README.md              # 📚 Dokumentationsübersicht
├── getting-started/       # 🎓 Einstiegsanleitung
├── api-reference/         # 📋 API-Referenz
├── examples.md            # 💡 Strategiebeispiele
├── api-classification.md  # 🔖 API-Klassifizierungsindex
├── versions/              # ⚖️ Versionsinformationen
├── version-differences.md # 🔍 Versionsunterschiede
├── original/              # 📄 Originaldokumente
└── advanced/              # 🔧 Erweiterte Funktionen & FAQ
```

## 🔍 Wichtige Erkenntnisse

### Wesentliche technische Unterschiede

#### 1. Auftragsstatusfeld-Typänderung ⚠️ (Wichtigste)
```python
# V005: int-Typ
if order.status == 8:

# V016/V041: str-Typ
if order.status == '8':
```

#### 2. Versionsexklusive Funktionen
- **V005**: WeChat-Push, Kapitaltransfer, E-Mail-Einstellungen
- **V016 fehlt**: WeChat, Wandelanleihen, Margin-Info
- **V041 vollständig**: Alle neuen Funktionen und Feldaktualisierungen

#### 3. Technische Indikatoren
- **V005**: Manuelle MACD-Berechnung erforderlich
- **V016/V041**: Eingebaut `get_MACD()`, `get_KDJ()`, `get_RSI()`, `get_CCI()`

## 🤝 Beitragsrichtlinien

1. **Fehler entdeckt**: Issue einreichen
2. **Inhalte ergänzen**: PR mit neuen Strategiebeispielen oder Best Practices
3. **Versionsaktualisierung**: Neue API-Unterschiede dokumentieren

## ⚠️ Haftungsausschluss

- Dieses Projekt dient ausschließlich Lern- und Forschungszwecken
- Alle Strategiebeispiele dienen nur als Referenz
- Spezifische API-Funktionen hängen von der Broker-Implementierung ab
- Investitionen bergen Risiken — handeln Sie mit Bedacht

## 📄 Lizenz

MIT-Lizenz — Siehe [LICENSE](LICENSE).

---

> **Letzte Aktualisierung**: Dezember 2024
> **Wartungsstatus**: Aktiv gepflegt
