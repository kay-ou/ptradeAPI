# Ptrade API Dokumentationsprojekt

**[English](README.md)** | **[中文](README_CN.md)** | **[Deutsch](README_DE.md)**

---

**Vollständige Dokumentationsbibliothek für die quantitative Handels-API von Ptrade** — Detaillierte Vergleichsanalyse und Nutzungsleitfaden basierend auf drei Hauptversionen

> **Empfohlen: SimTradeDesk** — Eine professionelle Desktop-Umgebung für Ptrade-Strategieentwickler mit PTrade-kompatiblen APIs, Strategie-Editor, Backtesting-System, Parameteroptimierung und mehr. Keine Python-Umgebung nötig — einfach herunterladen, installieren und loslegen. Details unter **[SimTradeDesk](http://github.com/kay-ou/SimTradeDesk)**.

> Für offizielle Zugangsinformationen zu Ptrade-Schnittstellen senden Sie bitte eine Direktnachricht. Ich stelle einen Referenzpfad bereit, der „ausschließlich offizielle Informationsquellen" enthält.
> Ptrade-Entwickler QQ-Gruppe: 590529320

## 🌐 API-Dokumentation — Sprachversionen

- [Chinesische API-Dokumentation](docs/api-reference/README.md)
- [Englische API-Dokumentation](docs/api-reference-en/README.md)

## 🎯 Projektübersicht

Ptrade ist eine von Hundsun Electronics entwickelte quantitative Handels-API-Plattform, die von mehreren Wertpapierfirmen übernommen und angepasst wird. Dieses Projekt dokumentiert drei Hauptversionen:

- **Dongguan Securities** (PBOXQT1.0V202202.01.041) — Neueste Funktionsversion
- **Guosheng Securities** (PBOXQT1.0V202202.01.016) — Stabile Standardversion
- **Community-Version** (PBOXQT1.0V202202.00.005) — Community-erweiterte Version

## ✨ Projektmerkmale

### 📊 Versionsvergleich auf Basis realer API-Dokumentation
- Technische Unterschiede durch Vergleich dreier Versionsdokumente entdeckt
- Detaillierte Analyse der Funktionsaufrufe und Rückgabewerte
- Upgrade-Leitfaden und Kompatibilitätsempfehlungen

### 🔍 Vollständige Funktionsklassifizierung und Indexierung
- Alle API-Schnittstellen nach Funktion kategorisiert
- Versionsunterstützung klar gekennzeichnet
- Vollständige Strategiebeispiel-Bibliothek

### 💡 Praktische Best Practices
- Best Practices basierend auf offizieller QA-Dokumentation
- Tipps zur Leistungsoptimierung und Stabilität
- Fehlerbehandlung und Debugging-Techniken

### 📚 Umfangreiche Lernressourcen
- Vollständige Strategiebeispiele von Grundlagen bis Fortgeschritten
- Detaillierte Finanzdaten-API-Dokumentation
- Nützliche Links und Lernressourcen

## 🚀 Schnellstart

### 1. Version auswählen
Wählen Sie die passende Version basierend auf Ihrer Broker-Umgebung:

| Broker | Version | Merkmale | Empfohlen für |
|--------|---------|----------|---------------|
| **Dongguan Securities** | V041 | Neueste Funktionen, volle Unterstützung | Professioneller Handel, neueste Features benötigt |
| **Guosheng Securities** | V016 | Stabil und zuverlässig, Standardfunktionen | Produktionsumgebung, Stabilität bevorzugt |
| **Community** | V005 | Lernfreundlich, umfangreiche Beispiele | Studium & Forschung, Funktionserkundung |

👉 **Unsicher?** Sehen Sie den [Versionsauswahl-Leitfaden](docs/getting-started/README.md) oder den [Detaillierten Versionsvergleich](docs/versions/version-comparison-table.md)

### 2. Einstiegspunkt nach Bedarf wählen

#### 🎓 Anfänger — Lernen
- [📖 Einstiegsanleitung](docs/getting-started/) — Ptrade von Grund auf lernen
- [💡 Strategiebeispiele](docs/examples.md) — Aus echtem Code lernen
- [📚 Dokumentationsnavigation](docs/) — Haupteinstieg zur Dokumentation

#### 🔍 API nachschlagen
- [📋 API-Referenz](docs/api-reference/) — Vollständige API-Beschreibungen und Navigation
- [🔖 API-Klassifizierungsindex](docs/api-classification.md) — Funktionsbasierte Schnellreferenz
- [📊 Branchen-/Konzeptdaten](docs/industry-concept-data.md) — Branchenklassifizierung und Konzeptsektoren

#### ⚖️ Versionsunterschiede vergleichen
- [🔍 Versionsvergleich](docs/version-differences.md) — Analyse der technischen Hauptunterschiede
- [📊 Versionsdetails](docs/versions/) — Vollständiger Funktionsvergleich und Auswahlleitfaden
- [📄 Originaldokumente](docs/original/) — Vollständige Original-API-Dokumentation aller drei Versionen

#### ❓ Probleme
- [🔧 Erweiterte Funktionen und FAQ](docs/advanced/) — Häufige Fragen, Bibliotheken, Versionsänderungen
- [❓ Häufig gestellte Fragen](docs/advanced/faq.md) — Detaillierte Fehlerbehebung

## 📁 Dokumentationsstruktur

```
docs/
├── README.md              # 📚 Haupteinstieg der Dokumentation
├── getting-started/       # 🎓 Einstiegsanleitung
│   ├── README.md          # Einstiegsnavigation
│   ├── quick-start.md     # Schnellstart
│   └── ...               # Weitere Einstiegsdokumente
├── api-reference/         # 📋 API-Referenz
│   ├── README.md          # API-Startseite und Navigation
│   ├── stock-trading.md   # Aktienhandel-Schnittstellen
│   ├── market-data.md     # Marktdaten-Schnittstellen
│   ├── technical-indicators.md # Technische Indikatoren
│   └── ...               # Weitere API-Module
├── examples.md           # 💡 Strategiebeispiele
├── api-classification.md  # 🔖 API-Klassifizierungsindex
├── industry-concept-data.md # 📊 Branchen-/Konzeptdaten
├── versions/              # ⚖️ Versionsinformationen und Vergleich
│   ├── README.md          # Versionsauswahl-Leitfaden
│   ├── version-comparison-table.md # Funktionsvergleichstabelle
│   └── ...               # Weitere Versionsdokumente
├── version-differences.md # 🔍 Versionsunterschiede
├── original/              # 📄 Originaldokumente
│   ├── README.md          # Originaldokument-Navigation
│   ├── Ptrade社区.md      # Community-Version
│   ├── Ptrade国盛.md      # Guosheng-Version
│   └── ...               # Weitere Originaldokumente
└── advanced/              # 🔧 Erweiterte Funktionen
    ├── README.md          # Navigation erweiterte Funktionen
    ├── faq.md            # Häufig gestellte Fragen
    └── ...               # Weitere erweiterte Dokumente
```

## 🔍 Wichtige Erkenntnisse

### Wesentliche technische Unterschiede
Durch Vergleich der tatsächlichen API-Dokumentation der drei Versionen wurden folgende wichtige Unterschiede festgestellt:

#### 1. Auftragsstatusfeld-Typänderung ⚠️ (Wichtigste)
```python
# V005: int-Typ
if order.status == 8:

# V016/V041: str-Typ
if order.status == '8':
```

#### 2. Versionsexklusive Funktionen
- **V005 exklusiv**: WeChat-Work-Push, Kapitaltransfer, E-Mail-Einstellungen
- **V016 fehlt**: WeChat Work, Wandelanleihen-Schnittstellen, Margin-Trading-Abfrage
- **V041 vollständig**: Alle neuen Funktionen und neueste Feldaktualisierungen

#### 3. Technische Indikatoren
- **V005**: Manuelle MACD-Berechnung erforderlich
- **V016/V041**: Eingebaut `get_MACD()`, `get_KDJ()`, `get_RSI()`, `get_CCI()`

## 📖 Nutzungsleitfaden

### 🎯 Navigation nach Rolle

#### Neue Benutzer
1. **Grundlagen verstehen** → [Einstiegsanleitung](docs/getting-started/)
2. **Aus Code lernen** → [Strategiebeispiele](docs/examples.md)
3. **Schnittstellen finden** → [API-Referenz](docs/api-reference/)

#### Entwickler
1. **Vollständige API ansehen** → [API-Referenz](docs/api-reference/)
2. **Best Practices lernen** → [Strategiebeispiele](docs/examples.md)
3. **Versionskompatibilität** → [Versionsvergleich](docs/version-differences.md)

#### Betriebspersonal
1. **Plattformbeschränkungen** → [Versionsunterschiede](docs/version-differences.md)
2. **Häufige Probleme lösen** → [FAQ](docs/advanced/faq.md)
3. **Bibliotheken ansehen** → [Erweiterte Funktionen](docs/advanced/)

## 📚 Lernressourcen

- [Strategiebeispiel-Bibliothek](docs/examples.md) — Vollständige Beispiele von Grundlagen bis Fortgeschritten
- [Erweiterte Funktionen](docs/advanced/) — Häufige Fragen, Bibliotheken, Versionsänderungen

## 🤝 Beitragsrichtlinien

Dieses Projekt basiert auf öffentlich verfügbarer API-Dokumentation. Beiträge sind willkommen:

1. **Fehler melden**: Issue einreichen
2. **Inhalte ergänzen**: PR mit neuen Strategiebeispielen oder Best Practices
3. **Versionsaktualisierung**: API-Unterschiede für neue Versionen dokumentieren

## ⚠️ Haftungsausschluss

- Dieses Projekt dient ausschließlich Lern- und Forschungszwecken
- Alle Strategiebeispiele dienen nur als Referenz — bitte vor Live-Trading ausgiebig testen
- Spezifische API-Funktionen hängen von der jeweiligen Broker-Implementierung ab
- Investitionen bergen Risiken — handeln Sie mit Bedacht

## 📄 Lizenz

MIT-Lizenz — Siehe [LICENSE](LICENSE).

---

> **Letzte Aktualisierung**: Dezember 2024
> **Wartungsstatus**: Aktiv gepflegt
> **Dokumentationsversion**: Basierend auf tatsächlicher API-Dokumentation dreier Hauptversionen
