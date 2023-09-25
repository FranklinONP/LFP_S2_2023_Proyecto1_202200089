import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz con columna numerada")
        self.geometry("400x300")

        self.column_label = tk.Label(self, text="No.", width=5, anchor="w")
        self.column_label.grid(row=0, column=0)

        self.data_labels = []
        self.insert_row_labels()

    def insert_row_labels(self):
        for row in range(1, 30):  # Insertar 10 filas numeradas
            label = tk.Label(self, text=str(row), width=5, anchor="w")
            label.grid(row=row, column=0)
            self.data_labels.append(label)

app = App()
app.mainloop()