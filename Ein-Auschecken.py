import time
import csv

def log_time(name):
    """ Speichert die Arbeitszeit in einer CSV-Datei basierend auf dem Namen """
    filename = "arbeitszeiten.csv"
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Überprüfen, ob der Nutzer bereits eingecheckt ist
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            last_entry = None
            for line in lines:
                if line.startswith(name):
                    last_entry = line.strip().split(",")
            
            if last_entry and last_entry[2] == "Check-in":
                with open(filename, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, timestamp, "Check-out"])
                print(f"Check-out erfolgreich für {name} um {timestamp}")
                return
    except FileNotFoundError:
        pass  

    # Neuen Check-in speichern
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, timestamp, "Check-in"])
    print(f"Check-in erfolgreich für {name} um {timestamp}")

print("Gib deinen Namen ein, um ein- oder auszuchecken. (Zum Beenden 'exit' eingeben)")
while True:
    name = input("Name: ").strip()
    if name.lower() == "exit":
        print("Beende das Programm...")
        break
    elif name:
        log_time(name)