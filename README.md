# Mini PaaS demó

Ez a projekt egy egyszerű, működő PaaS (Platform as a Service) prototípust ad egy webes kezelőfelülettel. Az appok listáját, skálázását és állapotát lokálisan, memóriában kezeli.

## Mire használható?

Ez egy demó felület, amellyel megmutatható, hogyan nézhet ki egy PaaS vezérlőpult. Nem telepít valódi konténereket, nem futtat CI/CD-t, és nem tartja meg az adatokat újraindítás után. A cél a felhasználói folyamatok és az API útvonalak szemléltetése.

### Mi történik, ha hozzáadsz egy alkalmazást?

- A rendszer létrehoz egy új bejegyzést a memóriában (név, runtime, repo URL, darabszám, státusz).
- Megjelenik a kártya a dashboardon, ahol skálázható, leállítható, vagy törölhető.
- Az `/api/apps` végpont az aktuális, memória-alapú állapotot adja vissza.

Ha „valódi” PaaS-ként szeretnéd használni, szükség lenne háttérfolyamatokra (pl. konténer indítás, build pipeline, naplózás, monitorozás), amit ez a demó nem tartalmaz.

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
