import tkinter as tk
from tkinter import messagebox, ttk

def calculer_trafic_total(nombre_abonnes, taux_congestion, trafic_par_abonne):
    return nombre_abonnes * taux_congestion * trafic_par_abonne

def calculer_trafic_cellule(nombre_porteuses, nb_its, erlangs_par_its):
    return (nombre_porteuses * 8 - nb_its) * erlangs_par_its

def calculer_nombre_cellules(trafic_total, trafic_par_cellule):
    return trafic_total / trafic_par_cellule

def calculer_nombre_sites(nombre_cellules, secteurs_par_site):
    return nombre_cellules / secteurs_par_site

def effectuer_calculs():
    try:
        nombre_abonnes = int(entry_nombre_abonnes.get())
        taux_congestion = float(entry_taux_congestion.get())
        trafic_par_abonne = float(entry_trafic_par_abonne.get())
        nombre_porteuses = int(entry_nombre_porteuses.get())
        nb_its = int(entry_nb_its.get())
        erlangs_par_its = float(entry_erlangs_par_its.get())
        secteurs_par_site = int(entry_secteurs_par_site.get())
        augmentation_trafic = float(entry_augmentation_trafic.get())

        # Calculs
        trafic_total = calculer_trafic_total(nombre_abonnes, taux_congestion, trafic_par_abonne)
        trafic_cellule = calculer_trafic_cellule(nombre_porteuses, nb_its, erlangs_par_its)
        nombre_cellules = calculer_nombre_cellules(trafic_total, trafic_cellule)
        nombre_sites = calculer_nombre_sites(nombre_cellules, secteurs_par_site)

        # Affichage des résultats
        label_resultats_trafic_total_val.config(text=f"{trafic_total:.2f} Erlangs")
        label_resultats_trafic_cellule_val.config(text=f"{trafic_cellule:.2f} Erlangs")
        label_resultats_nombre_cellules_val.config(text=f"{nombre_cellules:.2f}")
        label_resultats_nombre_sites_val.config(text=f"{nombre_sites:.2f}")

        # Recalcul avec augmentation de trafic
        trafic_total_recalc = trafic_total * augmentation_trafic
        nombre_cellules_recalc = calculer_nombre_cellules(trafic_total_recalc, trafic_cellule)
        nombre_sites_recalc = calculer_nombre_sites(nombre_cellules_recalc, secteurs_par_site)

        # Affichage des résultats recalculés
        label_resultats_trafic_total_recalc_val.config(text=f"{trafic_total_recalc:.2f} Erlangs")
        label_resultats_nombre_cellules_recalc_val.config(text=f"{nombre_cellules_recalc:.2f}")
        label_resultats_nombre_sites_recalc_val.config(text=f"{nombre_sites_recalc:.2f}")

    except ValueError:
        messagebox.showerror("Erreur de saisie", "Veuillez entrer des valeurs valides pour tous les champs.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Outil de Dimensionnement de Ville d'un reseau GSM")
root.geometry("800x400")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"), background="#4CAF50", foreground="white")

# Création d'un cadre pour l'entrée des données
frame_inputs = ttk.Frame(root, padding="20 20 20 20", relief="solid")
frame_inputs.grid(row=0, column=0, padx=20, pady=20)

frame_results = ttk.Frame(root, padding="20 20 20 20", relief="solid")
frame_results.grid(row=0, column=1, padx=20, pady=20)

# Champs de saisie
ttk.Label(frame_inputs, text="Nombre d'abonnés:").grid(row=0, column=0, sticky="W", pady=5)
entry_nombre_abonnes = ttk.Entry(frame_inputs)
entry_nombre_abonnes.grid(row=0, column=1, pady=5)

ttk.Label(frame_inputs, text="Taux de congestion:").grid(row=1, column=0, sticky="W", pady=5)
entry_taux_congestion = ttk.Entry(frame_inputs)
entry_taux_congestion.grid(row=1, column=1, pady=5)

ttk.Label(frame_inputs, text="Trafic par abonné (Erlangs):").grid(row=2, column=0, sticky="W", pady=5)
entry_trafic_par_abonne = ttk.Entry(frame_inputs)
entry_trafic_par_abonne.grid(row=2, column=1, pady=5)

ttk.Label(frame_inputs, text="Nombre de porteuses par cellule:").grid(row=3, column=0, sticky="W", pady=5)
entry_nombre_porteuses = ttk.Entry(frame_inputs)
entry_nombre_porteuses.grid(row=3, column=1, pady=5)

ttk.Label(frame_inputs, text="Nombre d'ITs TCH:").grid(row=4, column=0, sticky="W", pady=5)
entry_nb_its = ttk.Entry(frame_inputs)
entry_nb_its.grid(row=4, column=1, pady=5)

ttk.Label(frame_inputs, text="Erlangs par IT:").grid(row=5, column=0, sticky="W", pady=5)
entry_erlangs_par_its = ttk.Entry(frame_inputs)
entry_erlangs_par_its.grid(row=5, column=1, pady=5)

ttk.Label(frame_inputs, text="Secteurs par site:").grid(row=6, column=0, sticky="W", pady=5)
entry_secteurs_par_site = ttk.Entry(frame_inputs)
entry_secteurs_par_site.grid(row=6, column=1, pady=5)

ttk.Label(frame_inputs, text="Augmentation du trafic:").grid(row=7, column=0, sticky="W", pady=5)
entry_augmentation_trafic = ttk.Entry(frame_inputs)
entry_augmentation_trafic.grid(row=7, column=1, pady=5)

# Bouton pour lancer les calculs
btn_calculer = ttk.Button(frame_inputs, text="Calculer", command=effectuer_calculs)
btn_calculer.grid(row=8, column=0, columnspan=2, pady=20)

# Création d'un cadre pour afficher les résultats
ttk.Label(frame_results, text="Trafic total à l'heure de pointe:").grid(row=0, column=0, sticky="W", pady=5)
label_resultats_trafic_total_val = ttk.Label(frame_results, text="")
label_resultats_trafic_total_val.grid(row=0, column=1, sticky="W", pady=5)

ttk.Label(frame_results, text="Trafic par cellule:").grid(row=1, column=0, sticky="W", pady=5)
label_resultats_trafic_cellule_val = ttk.Label(frame_results, text="")
label_resultats_trafic_cellule_val.grid(row=1, column=1, sticky="W", pady=5)

ttk.Label(frame_results, text="Nombre de cellules nécessaires:").grid(row=2, column=0, sticky="W", pady=5)
label_resultats_nombre_cellules_val = ttk.Label(frame_results, text="")
label_resultats_nombre_cellules_val.grid(row=2, column=1, sticky="W", pady=5)

ttk.Label(frame_results, text="Nombre de sites tri-sectoriels:").grid(row=3, column=0, sticky="W", pady=5)
label_resultats_nombre_sites_val = ttk.Label(frame_results, text="")
label_resultats_nombre_sites_val.grid(row=3, column=1, sticky="W", pady=5)

ttk.Label(frame_results, text="Trafic total recalculé:").grid(row=4, column=0, sticky="W", pady=5)
label_resultats_trafic_total_recalc_val = ttk.Label(frame_results, text="")
label_resultats_trafic_total_recalc_val.grid(row=4, column=1, sticky="W", pady=5)

ttk.Label(frame_results, text="Nombre de cellules nécessaires (recalculé):").grid(row=5, column=0, sticky="W", pady=5)
label_resultats_nombre_cellules_recalc_val = ttk.Label(frame_results, text="")
label_resultats_nombre_cellules_recalc_val.grid(row=5, column=1, sticky="W", pady=5)

ttk.Label(frame_results, text="Nombre de sites tri-sectoriels (recalculé):").grid(row=6, column=0, sticky="W", pady=5)
label_resultats_nombre_sites_recalc_val = ttk.Label(frame_results, text="")
label_resultats_nombre_sites_recalc_val.grid(row=6, column=1, sticky="W", pady=5)

# Lancement de la boucle principale
root.mainloop()
