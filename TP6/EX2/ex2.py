import re

notes = open("notes.txt", "r")

ids = open("ids.txt", "r").read()
subjects = notes.readline()
subjects = subjects.replace('\n', "")
subjects = subjects.split(';')
listnotes = notes.read()
listnotes = listnotes.split('\n')
noteseleves = [item.split(';') for item in listnotes]
# print(noteseleves)
# print(subjects)
#print(words)
ids = ids.split('\n')
print(ids)
moyennetotale = 0 

frapport = open('rapport.txt', 'w')
valide = ""
nvalide = ""
for i in range(len(ids)):
    rapport = {}
    rapport['id'] = ids[i]
    rapport[subjects[0]] = noteseleves[i][0]
    rapport[subjects[1]] = noteseleves[i][1]
    rapport[subjects[2]] = noteseleves[i][2]
    moyenne = (float(noteseleves[i][0]) + float(noteseleves[i][1]) +float(noteseleves[i][2]))/3
    rapport['Moyenne'] = moyenne
    frapport.write(str(rapport)+'\n')
    if(moyenne >= 12):
        valide += str(rapport)+'\n'
    else:
        nvalide += str(rapport)+'\n'
    moyennetotale += moyenne
moyennetotale = moyennetotale/len(ids)
frapport.write("Liste des etudiants qui ont valide la semestre: \n")
frapport.write(valide)
frapport.write("Liste des etudiants qui n'ont pas valide la semestre: \n")
frapport.write(nvalide)
frapport.write("Moyenne de la classe est: " + str(moyennetotale))
print(rapport)
