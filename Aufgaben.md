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


