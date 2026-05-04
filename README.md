# Virtualisierung

*Dieses Projekt dient zur strukturierten Erarbeitung und praktischen Umsetzung von Virtualisierungskonzepten anhand verschiedener Technologien.*

## Überblick
Dieses Repository begleitet die Auseinandersetzung mit dem Thema Virtualisierung. Ziel ist es, verschiedene Virtualisierungstypen praktisch umzusetzen und deren Unterschiede zu verstehen. Die Struktur ist in mehrere Teilbereiche gegliedert, die jeweils eigene Konfigurationsdateien enthalten. Das Projekt befindet sich aktuell in Entwicklung und wird schrittweise erweitert.

## Installation

1. Repository klonen:  
git clone https://github.com/pantrimasi/virtualisierung_mk_2026.git  

2. In das Projektverzeichnis wechseln:  
cd virtualisierung_mk_2026  

3. Struktur prüfen:  
tree

## Beitrag leisten (Contributing)
Änderungen erfolgen über Pull Requests. Jede Anpassung soll klar beschrieben und sinnvoll strukturiert sein. Issues können für Fehler oder neue Ideen erstellt werden. Die bestehende Ordnerstruktur muss eingehalten werden.

## Lizenz & Credits
**Autor:** PantriMasi  
Dieses Projekt basiert auf Unterrichtsmaterial zum Thema Virtualisierung sowie praktischen Übungen und eigenen Implementationen.

## Zusätzliche Links
- Docker Repository: https://hub.docker.com/repository/docker/pantrimasi/pythonwebserver/general

**Source Directory:**  
- Aufgabenstellung Virtualisierung (Repository-Struktur und Umsetzungsvorgaben)

------------------------------------------------------------

# Aufgaben
## Vorgehen alle Spuren löschen

### 1. Alle Container anzeigen

```docker ps -a```


### 2. Container-ID finden

Aus der Ausgabe von docker ps -a wird die Container ID des hello-world Containers kopiert.

Beispiel:
```
CONTAINER ID   IMAGE          STATUS  
a1b2c3d4e5f6   hello-world    Exited  
```


### 3. Container löschen

```docker rm a1b2c3d4e5f6```

### 4. Image anzeigen

```docker images```

### 5. Image-ID ermitteln

Aus der Liste wird die IMAGE ID kopiert.

Beispiel:
```
REPOSITORY     TAG      IMAGE ID  
hello-world    latest   f9078146db2e  
```

### 6. Image löschen

```docker rmi f9078146db2e```

### 7. Kontrolle

```docker ps -a```
```docker images```

Es sollte kein hello-world Container und kein Image mehr vorhanden sein.

## sudo bei Docker

Ich arbeite auf Windows mit Docker Desktop und WSL2. Deshalb ist kein `sudo` notwendig, da Docker dort automatisch mit den richtigen Berechtigungen läuft.

## Image auf Docker Hub Pushen
### 1. Einloggen:
```docker login```

### 2. Tag erstellen:
```docker tag <local-image> <username>/<repository>:tagname```

### 3. Einloggen:
```docker push <username>/<repository>:tagname```

------------------------------------------------------------

# Container Performance
| Command | Beschreibung |
| ---------------- | --------------- |
| Docker stats <Container ID> | $250 |
| February | $80 |
| March | $420 |
