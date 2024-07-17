import tkinter as tk
from tkinter import messagebox
import sqlite3
import admin_menu
import menu_user

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Reservas de Habitaciones")
        self.geometry("1280x720")

        self.label = tk.Label(self, text="Sistema de Reservas")
        self.label.pack(pady=10)

        self.admin_button = tk.Button(self, text="Menú de Administrador", command=self.open_admin_menu)
        self.admin_button.pack(pady=5)

        self.user_button = tk.Button(self, text="Menú de Usuario", command=self.open_user_menu)
        self.user_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=5)

    def open_admin_menu(self):
        admin_menu.show_admin_menu(self)
        messagebox.showinfo("Menú de Administrador", "Opción de Administrador seleccionada")

    def open_user_menu(self):
        menu_user.show_menu(self)
        messagebox.showinfo("Menú de Usuario", "Opción de Usuario seleccionada")

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()