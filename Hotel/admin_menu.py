import tkinter as tk
from tkinter import messagebox

class AdminMenu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menú de Administrador")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Menú de Administrador")
        self.label.pack(pady=10)

        self.add_room_button = tk.Button(self, text="Agregar Habitación", command=self.add_room)
        self.add_room_button.pack(pady=5)

        self.view_reservations_button = tk.Button(self, text="Ver Reservas", command=self.view_reservations)
        self.view_reservations_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Regresar", command=self.destroy)
        self.back_button.pack(pady=5)

    def add_room(self):
        messagebox.showinfo("Agregar Habitación", "Funcionalidad para agregar una habitación")

    def view_reservations(self):
        messagebox.showinfo("Ver Reservas", "Funcionalidad para ver reservas")

def show_admin_menu(master=None):
    admin_menu = AdminMenu(master)
    admin_menu.grab_set()
