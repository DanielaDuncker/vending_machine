import sys

order = int(input("Paina tuotteesi numeroa.(1, 2 tai 3)"))

if order == 1:
    disPrice = 1.00

elif order == 2:
    disPrice = 1.50

elif order == 3:
    disPrice = 2.00

else:
    sys.exit("Ole hyvä ja kokeile uudestaan")

kaksEuro = int(input("Ilmoita 2€ kolikkojesi määrä."))
yksEuro = int(input("Ilmoita 1€ kolikkojesi määrä."))
viiskytSenttii = int(input("Ilmoita 50snt kolikkojesi määrä."))
kakskytSenttii = int(input("Ilmoita 20snt kolikkojesi määrä."))
kymmeneSenttii = int(input("Ilmoita 10snt kolikkojesi määrä."))
viisSenttii = int(input("Ilmoita 5snt kolikkojesi määrä."))

total = kaksEuro * 2.0 + yksEuro * 1.0 + viiskytSenttii * .50 + kakskytSenttii * .20 + kymmeneSenttii * .10 + viisSenttii * .05

if total >= disPrice:
    print("Vaihtorahasi" + " %.2f" % (total - disPrice) + " Hyvää päivän jatkoa.")
else:
    print("Ole hyvä ja kokeile uudestaan.")