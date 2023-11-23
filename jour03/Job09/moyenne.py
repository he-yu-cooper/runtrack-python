def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = float(input("please entre your first note: "))
note2 = float(input("please entre your secande note: "))
note3 = float(input("please entre your third note:"))

moyenne_etudiant = moyenne(note1, note2, note3)

if 20 >= moyenne_etudiant >= 15: 
    print("Very good student")
elif 14 >= moyenne_etudiant >= 11:
    print("Good student")
elif 10 >= moyenne_etudiant >= 8:
    print("Average student")
else:
    print("Student needing to make efforts")
