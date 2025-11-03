# Doku


## Config

Fülle die fehlenden Werte in der config_samples.py und nenne die datei in config.py um.  
Eine Beispiel config.py sieht so aus:   
class Config:  
    DEBUG = True  
    HOST = "0.0.0.0"  
    PORT = 8899


## Webshop aufrufen

### 1. Git-Repository in VS Code klonen  

- Öffne Visual Studio Code.  
- Klicke auf Quellcodeverwaltung (linke Seitenleiste, Symbol mit drei verbundenen Punkten).  
- Wähle Repository klonen.  
- Gib die URL deines Git-Repositories ein, z. B.:  
  https://github.com/dein-benutzername/dein-repo.git
- Wähle den Zielordner auf deinem Rechner.  
- Öffne den geklonten Ordner in VS Code.

(Alternativ als Terminal Eingabe: git clone https://github.com/<BENUTZER>/<REPOSITORY>.git
  
### 2. Virtual Environment installieren und starten


Die Einrichtung und das Starten des Virtual Environment und dem Modul "flask" erfolgt auf Windows durch folgende Eingaben in das Terminal:  

- python -m venv venv  
- cd venv  
- source bin/activate  
- pip install flask  
- (In neuem Terminal) python main.py  

Dann Localhost aufrufen: http://127.0.0.1:XXXX (wird im Terminal als Link vorgegeben)

Auf Mac sind hingegen folgende Terminal Prompts nötig:  

- python3 -m venv venv
- source venv/bin/activate
- pip install flask  
- pip freeze > requirements.txt
- python main.py
