# Ein-Auschecken 
import time
import csv
import tkinter as tk
from tkinter import messagebox

# CSV-Datei für die Zeiterfassung
FILENAME = "arbeitszeiten.csv"

def log_time(name):
    """ Speichert die Arbeitszeit in einer CSV-Datei basierend auf dem Namen """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Überprüfen, ob der Nutzer bereits eingecheckt ist
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            last_entry = None
            for line in lines:
                if line.startswith(name):
                    last_entry = line.strip().split(",")
            
            if last_entry and last_entry[2] == "Check-In":
                with open(FILENAME, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, timestamp, "Check-Out"])
                messagebox.showinfo("Erfolgreich", f"Check-out für {name} um {timestamp}")
                return
    except FileNotFoundError:
        pass  

    # Neuen Check-in speichern
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, timestamp, "Check-in"])
    messagebox.showinfo("Erfolgreich", f"Check-in für {name} um {timestamp}")

def on_submit():
    """ Holt den Namen aus dem Eingabefeld und loggt die Zeit """
    name = entry.get().strip()
    if name:
        log_time(name)
        entry.delete(0, tk.END)  # Löscht das Eingabefeld nach dem Check-in/Check-out
    else:
        messagebox.showwarning("Fehler", "Bitte einen Namen eingeben!")

# GUI-Fenster erstellen
root = tk.Tk()
root.title("Zeiterfassung")
root.geometry("300x200")

label = tk.Label(root, text="Gib deinen Namen ein:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Einchecken / Auschecken", command=on_submit, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
