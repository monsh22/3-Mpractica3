
import tkinter as tk

def convertir_a_celsius():
    Faret = float(entry1.get())
    #Celsius = (Farenheit-32)*5.0/9.0
    Cels = (Fart-32)*5/9
    entry2.delete(0, tk.END)
    entry2.insert(0,f"{Cels:.2f}")

def reset():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0, tk.END)
    entry2.insert(0, "0.0")

def convert_to_farenheit():
 cel = float(entry2.get())
 fahit = (cel* 9 /5) + 32
 entry1.delete(0, tk.END)
 entry1.insert(0,f"{fahit:.2f}")

app = tk.Tk()
app.title("Conversor de Temperatura")

label1 = tk.Label(app, text="Farenheit: ")
label1.grid(row=0, column=0)

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

button1 = tk.Button(app, text="Convertir a celsius", command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2 = tk.Label(app, text="Celsius:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

button2 = tk.Button(app, text="Convertir a Farenheit", command=convert_to_farenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(app, text="Restablecer", command=reset)
button3.grid(row=2, column=1)

app.mainloop()