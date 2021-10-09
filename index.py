from tkinter import ttk
from tkinter import *

class Tablero:

    def __init__(self, ventana):
        self.wind =ventana
        self.wind.title("Tablero Kanban")

        # Creando un cuadro contenedor
        frame = LabelFrame(self.wind, text = "Registro")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        #entrada del dato
        Label(frame, text="Nombre: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

if __name__ == "__main__":
    ventana = Tk()
    aplicacion = Tablero(ventana)
    ventana.mainloop()



