import tkinter as tk
from tkinter import messagebox
import sqlite3

class AdminMenu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menú de Administrador")
        self.geometry("500x500")

        self.label = tk.Label(self, text="Menú de Administrador")
        self.label.pack(pady=10)

        self.view_reservations_button = tk.Button(self, text="Ver Reservas", command=self.view_reservations)
        self.view_reservations_button.pack(pady=5)

        self.delete_id_label = tk.Label(self, text="ID de Reservación a Eliminar")
        self.delete_id_label.pack(pady=5)
        self.delete_id_entry = tk.Entry(self)
        self.delete_id_entry.pack(pady=5)

        self.delete_button = tk.Button(self, text="Eliminar Reservación", command=self.delete_record)
        self.delete_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Regresar", command=self.destroy)
        self.back_button.pack(pady=5)

    def view_reservations(self):
        connection = sqlite3.connect("hotel_reservations.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reservations")
        reservations = cursor.fetchall()
        connection.close()

        if reservations:
            reservations_list = "\n".join([f"{r[0]} - {r[1]} - {r[2]} - {r[3]} to {r[4]}" for r in reservations])
            messagebox.showinfo("Ver Reservas", reservations_list)
        else:
            messagebox.showinfo("Ver Reservas", "No hay reservas")

    def delete_record(self):
        record_id = self.delete_id_entry.get()
        if not record_id.isdigit():
            messagebox.showerror("Error", "Por favor, introduzca un ID válido")
            return

        record_id = int(record_id)
        try:
            sqliteConnection = sqlite3.connect('hotel_reservations.db')
            cursor = sqliteConnection.cursor()
            cursor.execute("DELETE FROM reservations WHERE id = ?", (record_id,))
            sqliteConnection.commit()
            cursor.close()

            if cursor.rowcount == 0:
                messagebox.showinfo("Eliminar Reservación", "No se encontró una reservación con ese ID")
            else:
                messagebox.showinfo("Eliminar Reservación", "Reservación eliminada con éxito")
        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error al eliminar la reservación: {error}")
        finally:
            if sqliteConnection:
                sqliteConnection.close()

def show_admin_menu(master=None):
    admin_menu = AdminMenu(master)
    admin_menu.grab_set()
