# ISS Tracker

Este es un programa sencillo que nos dice el número de astronautas que se encuentran en el espacio al momento de correr el programa, así como el vehículo en el que se encuentran.

También nos da las coordenadas instantáneas de la ISS, y al mismo tiempo crea un servidor local de `Dash` que nos muestra un mapa sencillo con la ubiccación de la ISS. Sólo copia la dirección del servidor y pégala en tu navegador para poder observar el mapa.

Esta información se obtiene a través de esta [API](http://open-notify.org/Open-Notify-API/).

Para correr el programa es necesario tener las siguientes librerías instaladas:
- `json`
- `pandas`
- `dash`
- `plotly`
- `urllib`

Con el siguiente comando puedes correr el código:
```bash
python iss-tracker.py
```
