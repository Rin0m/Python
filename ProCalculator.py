from tkinter import *

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)  # Aktualisiere das Label

def equals():
    global equation_text
    try:
        result = str(eval(equation_text))
        equation_label.set(result)
        equation_text = result
    except:
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

# Hauptfenster
window = Tk()
window.title("ProCalculator")
window.geometry("400x600")

equation_text = ""
equation_label = StringVar(value="0")  # Startwert "0"

# Label mit verbesserter Darstellung
label = Label(
    window, 
    textvariable=equation_label,
    font=('Arial', 24, 'bold'),  # Größere Schrift
    bg="lightgray",  # Hintergrundfarbe
    fg="black",      # Schriftfarbe
    anchor="e",      # Rechtsbündiger Text
    width=14,       # Breite in Zeichen
    height=2
)
label.pack(pady=20, padx=10, fill="x")

# Frame für Buttons
frame = Frame(window)
frame.pack()

# Zahlen-Buttons
buttons = [
    (7, 2, 0), (8, 2, 1), (9, 2, 2),
    (4, 3, 0), (5, 3, 1), (6, 3, 2),
    (1, 4, 0), (2, 4, 1), (3, 4, 2),
    (0, 5, 0), ('.', 5, 1)
]

for (text, row, col) in buttons:
    Button(
        frame, 
        text=str(text),
        font=('Arial', 18),
        height=2, 
        width=5,
        command=lambda t=text: button_press(t)
    ).grid(row=row, column=col, padx=2, pady=2)

# Operatoren-Buttons
operators = [
    ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3)
]

for (text, row, col) in operators:
    Button(
        frame, 
        text=text,
        font=('Arial', 18),
        height=2, 
        width=5,
        command=lambda t=text: button_press(f" {t} ")  # Leerzeichen für bessere Formatierung
    ).grid(row=row, column=col, padx=2, pady=2)

# Gleichheits-Button
Button(
    frame, 
    text='=', 
    font=('Arial', 18),
    height=2, 
    width=5,
    command=equals
).grid(row=5, column=2, padx=2, pady=2)

# Clear-Button
Button(
    window, 
    text='Clear', 
    font=('Arial', 14),
    height=2, 
    width=10,
    command=clear
).pack(pady=10)

window.mainloop()
