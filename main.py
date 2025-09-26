# Risolutore in python di sistemi a due incognite e due equazioni
print("Benvenuto")
print("Questo programma risolve i sistemi lineari a due incognite e due equazioni")
print("- Assicurati che il tuo sistema sia scritto in questo formato prima di inserirlo nel programma")
print(" # 1^ equazione: c1X+c1Y=tn1, 2^ equazione: c2X+C2Y=tn2 # ")
print("- dove c1[lettera] sta per il primo coefficente (nel senso di coefficente della prima equazione, tn[numero equazione] invece indica il termine noto")
print("- Somma tutti i termini noti per ogni equazione, a seguire ti saranno chiesti rispettivamente i coefficenti di X ed Y della prima equazione, dopo il termine noto, sempre della prima equazione. A seguire lo stesso ordine per la seconda")
print(" # Questo risolutore usa il metodo di Cramer, per maggiori informazioni cerca online # ")

# Prima Equazione
c1X = float(input("Inserisci il coefficiente di X della prima Equazione: "))
c1Y = float(input("Inserisci il coefficiente di Y della prima Equazione: "))
tn1 = float(input("Inserisci il termine noto della prima Equazione: "))

# Seconda Equazione
c2X = float(input("Inserisci il coefficiente di X della seconda Equazione: "))
c2Y = float(input("Inserisci il coefficiente di Y della seconda Equazione: "))
tn2 = float(input("Inserisci il termine noto della seconda Equazione: "))

# D = Δ

# Determinante principale
D = (c1X * c2Y) - (c2X * c1Y)

if D == 0:
    print("Il sistema non ha soluzione unica (determinante nullo).")
else:
    # Metodo di Cramer
    X = ((tn1 * c2Y) - (tn2 * c1Y)) / D
    Y = ((c1X * tn2) - (c2X * tn1)) / D

# Risultato del sistema di Equazioni

print(f"Il risultato del sistema di equazioni è: X = {X}, Y = {Y}")