import tkinter as tk
from tkinter import messagebox
import sqlite3

class MenuUser(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menú de Usuario")
        self.geometry("500x500")

        self.label = tk.Label(self, text="Menú de Usuario")
        self.label.pack(pady=10)

        self.name_label = tk.Label(self, text="Nombre")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        self.room_type_label = tk.Label(self, text="Tipo de Habitación")
        self.room_type_label.pack(pady=5)
        self.room_type_entry = tk.Entry(self)
        self.room_type_entry.pack(pady=5)

        self.check_in_label = tk.Label(self, text="Fecha de Entrada (YYYY-MM-DD)")
        self.check_in_label.pack(pady=5)
        self.check_in_entry = tk.Entry(self)
        self.check_in_entry.pack(pady=5)

        self.check_out_label = tk.Label(self, text="Fecha de Salida (YYYY-MM-DD)")
        self.check_out_label.pack(pady=5)
        self.check_out_entry = tk.Entry(self)
        self.check_out_entry.pack(pady=5)

        self.book_room_button = tk.Button(self, text="Reservar Habitación", command=self.book_room)
        self.book_room_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Regresar", command=self.destroy)
        self.back_button.pack(pady=5)

    def book_room(self):
        name = self.name_entry.get()
        room_type = self.room_type_entry.get()
        check_in_date = self.check_in_entry.get()
        check_out_date = self.check_out_entry.get()

        if name and room_type and check_in_date and check_out_date:
            connection = sqlite3.connect("hotel_reservations.db")
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO reservations (name, room_type, check_in_date, check_out_date)
                              VALUES (?, ?, ?, ?)''', (name, room_type, check_in_date, check_out_date))
            connection.commit()
            connection.close()
            messagebox.showinfo("Reservar Habitación", "Reservación realizada con éxito")
            self.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos")

def show_menu(master=None):
    user_menu = MenuUser(master)
    user_menu.grab_set()
