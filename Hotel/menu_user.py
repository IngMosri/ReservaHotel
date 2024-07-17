import tkinter as tk
from tkinter import messagebox

class MenuUser(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menú de Usuario")
        self.geometry("300x200")

        self.label = tk.Label(self, text="Menú de Usuario")
        self.label.pack(pady=10)

        self.book_room_button = tk.Button(self, text="Reservar Habitación", command=self.book_room)
        self.book_room_button.pack(pady=5)

        self.view_bookings_button = tk.Button(self, text="Ver Reservas", command=self.view_bookings)
        self.view_bookings_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Regresar", command=self.destroy)
        self.back_button.pack(pady=5)

    def book_room(self):
        messagebox.showinfo("Reservar Habitación", "Funcionalidad para reservar una habitación")

    def view_bookings(self):
        messagebox.showinfo("Ver Reservas", "Funcionalidad para ver reservas")

def show_menu(master=None):
    user_menu = MenuUser(master)
    user_menu.grab_set()
