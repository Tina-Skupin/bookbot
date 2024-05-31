text = "Ja ja Ding DONG"
grossliste = list(text)
grundliste = []
for buchstabe in grossliste:
    kleinbuchstabe = buchstabe.lower()
    grundliste.append(kleinbuchstabe)
print (grundliste)