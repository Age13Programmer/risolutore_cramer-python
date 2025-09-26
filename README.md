# Risolutore di Sistemi Lineari a 2 Incognite

Questo programma in **Python** risolve sistemi lineari di due equazioni a due incognite utilizzando il **metodo di Cramer**.  
È pensato come esercizio didattico per capire meglio come funziona la risoluzione manuale dei sistemi.

---

## ✨ Funzionalità
- Richiede in input i coefficienti delle due equazioni.
- Calcola il determinante principale.
- Verifica se il sistema ha una soluzione unica.
- Fornisce le soluzioni `(X, Y)` se esistono.

---

## 📖 Formato del sistema

Il sistema deve essere scritto nel formato:
```bash
{ c1X * X + c1Y * Y = tn1
  c2X * X + c2Y * Y = tn2
```

Esempio:
```bash
{ X + Y = -1
  2X - 3Y = 1
```

---

## 🚀 Esecuzione

Assicurati di avere **Python 3** installato, poi esegui:

```bash
python3 main.py
```

Il programma ti guiderà nell’inserimento dei coefficienti e dei termini noti.

📌 Esempio di utilizzo
```bash

Inserisci il coefficiente di X della prima Equazione: 1

Inserisci il coefficiente di Y della prima Equazione: 1

Inserisci il termine noto della prima Equazione: -1

Inserisci il coefficiente di X della seconda Equazione: 2

Inserisci il coefficiente di Y della seconda Equazione: 3

Inserisci il termine noto della seconda Equazione: 1

Il risultato del sistema di equazioni è: X = -4.0, Y = 3.0
```
