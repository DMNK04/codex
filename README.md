# Mini PaaS demó

Ez a projekt egy egyszerű, működő PaaS (Platform as a Service) prototípust ad egy webes kezelőfelülettel. Az appok listáját, skálázását és állapotát lokálisan, memóriában kezeli.

## Indítás

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

A weboldal elérhető lesz a `http://localhost:5000` címen.

## API

- `GET /api/apps` – JSON listát ad vissza a telepített alkalmazásokról.
