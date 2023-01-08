import re

notes = open("notes.txt", "r")
noms = open("noms.txt", "r").read()
ids = open("ids.txt", "r").read()
subjects = notes.readline()
subjects = subjects.replace('\n', "")
subjects = subjects.split(';')
listnotes = notes.read()
listnotes = listnotes.split('\n')
noms = noms.split('\n')
noteseleves = [item.split(';') for item in listnotes]
ids = ids.split('\n')
moyennetotale = 0 

for i in range(len(ids)):
    moyenne = (float(noteseleves[i][0]) + float(noteseleves[i][1]) +float(noteseleves[i][2]))/3
    moyennetotale += moyenne
moyennetotale = moyennetotale/len(ids)

for i in range(len(ids)):
    ffile = open(noms[i] + ".txt", "w")
    ffile.write("Nom et Prenom: " + noms[i] + "        ID: " + ids[i] + "\n")
    ffile.write("| " + subjects[0] + "   | "+ subjects[1] + "    | "+ subjects[2] + "\n")
    ffile.write("| " + str(noteseleves[i][0]) + "      | "+ str(noteseleves[i][1]) + "      | "+ str(noteseleves[i][2]) + "\n\n")
    moyenne = (float(noteseleves[i][0]) + float(noteseleves[i][1]) +float(noteseleves[i][2]))/3
    ffile.write("Moyenne: "+ str(moyenne) + " \nMoyenne de la classe: " + str(moyennetotale) + "\n")
    if(moyenne>=12):
        ffile.write("Resultat: Valide")
    else:
        ffile.write("Resultat: Non Valide")
    
    
    
#