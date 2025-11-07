# Doku

## Webshop aufrufen

### 1. Git-Repository in VS Code klonen

> Hierfür muss GIT lokal installiert sein: https://git-scm.com/download/win
> Die Installation/Version kann mit `git --version` in der CLI überprüft werden
> Ebenfalls muss Python installiert sein: https://www.python.org/downloads/windows/
> „Add Python to PATH“ aktivieren → Installation abschließen
> Die Installation kann im Anschluss wiefolgt geprpüft werden: python --version pip --version

- Öffne Visual Studio Code
- Klicke auf Quellcodeverwaltung (linke Seitenleiste, Symbol mit drei verbundenen Punkten)
- Wähle **Repository klonen**
- Gib die URL deines Git-Repositories ein, z. B.:
  ```
  https://github.com/philippGtz/E3FIAE-Team-1
  ```
**Alternativ als Terminal Eingabe:**

```bash
git clone https://github.com/philippGtz/E3FIAE-Team-1
```
- Wähle den Zielordner auf deinem Rechner: cd E3FIAE-Team-1
- Öffne den geklonten Ordner in VS Code

## Config

Fülle die fehlenden Werte in der `config_samples.py` und nenne die Datei in `config.py` um.

Eine Beispiel `config.py` sieht so aus:

```python
class Config:
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8899
```

### 2. Virtual Environment installieren und starten

#### Auf Windows

Folgende Eingaben im Terminal durchführen:

```bash
python -m venv venv
venv\Scripts\activate
pip install flask
python main.py
```

> Empfehlung: `python main.py` in einem neuem Terminal ausführen

Dann Localhost aufrufen: `http://127.0.0.1:XXXX`
(Der Link wird nach Ausführung von `python main.py` im Terminal vorgegeben)

#### Auf macOS

Folgende Terminal Befehle sind nötig:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
pip freeze > requirements.txt
python main.py
```

---

**Hinweis:** Alle Befehle sind ohne die Backticks (`) einzugeben!
