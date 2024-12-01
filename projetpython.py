import tkinter as tk

def calcul():
    try:
        a = int(entree_a.get())
        b = int(entree_b.get())
        def pgcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        pgcdresultat = pgcd(a, b)

        ppcmresultat = (a * b) // pgcdresultat

        parite_a = "est un nombre pair" if a % 2 == 0 else "est un nombre impair"
        parite_b = "est un nombre pair" if b % 2 == 0 else "est un nombre impair"

        def prem(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        nbrprem = [i for i in range(2, a + b + 1) if prem(i)]

        resultat_label.config(text=f"PGCD: {pgcdresultat}\nPPCM: {ppcmresultat}\n{a} est {parite_a}\n{b} est {parite_b}\nNombres premiers entre 1 et {a+b}: {nbrprem}")
    except ValueError:
        resultat_label.config(text="Veuillez entrer des nombres entiers.")

fenetre = tk.Tk()
fenetre.title("Calculs mathématiques")
label_a = tk.Label(fenetre, text="Entrez le premier nombre:")
entree_a = tk.Entry(fenetre)
label_b = tk.Label(fenetre, text="Entrez le deuxième nombre:")
entree_b = tk.Entry(fenetre)
bouton_calcul = tk.Button(fenetre, text="allez zouuu!", command=calcul)
resultat_label = tk.Label(fenetre, text="")
label_a.pack()
entree_a.pack()
label_b.pack()
entree_b.pack()
bouton_calcul.pack()
resultat_label.pack()
fenetre.mainloop()
