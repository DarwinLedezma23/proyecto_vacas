import tkinter as tk
from tkinter import messagebox
import database

def agregar_vaca():
    nombre = entry_nombre.get()
    fecha_inseminacion = entry_fecha_inseminacion.get()
    cantidad_partos = entry_cantidad_partos.get()
    fecha_posible_parto = entry_fecha_posible_parto.get()
    fecha_secado = entry_fecha_secado.get()
    concepcion_exitosa = entry_concepcion_exitosa.get()
    observaciones = entry_observaciones.get()

    database.insertar_vaca(nombre, fecha_inseminacion, cantidad_partos, fecha_posible_parto, fecha_secado, concepcion_exitosa, observaciones)

    messagebox.showinfo("Éxito", "Vaca agregada correctamente.")

    limpiar_campos()

    def limpiar_campos():
        entry_nombre.delete(0, tk.END)
        entry_fecha_inseminacion.delete(0, tk.END)
        entry_cantidad_partos.delete(0, tk.END)
        entry_fecha_posible_parto.delete(0, tk.END)
        entry_fecha_secado.delete(0, tk.END)
        var_concepcion_exitosa.set("No")
        text_observaciones.delete("1.0", tk.END)

    root = tk.Tk()
    root.title("Registro de Vacas Preñadas")
#campos a llenar de la vaca
    tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="e")
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1)


    tk.Label(root, text="Fecha de vacunación:").grid(row=1, column=0, sticky="e")
    entry_fecha_inseminacion = tk.Entry(root)
    entry_fecha_inseminacion.grid(row=1, column=1)

    tk.Label(root, text="Cantidad de partos:").grid(row=2, column=0, sticky="e")
    entry_cantidad_partos = tk.Entry(root)
    entry_cantidad_partos.grid(row=2, column=1)

    tk.Label(root, text="Fecha posible de parto:").grid(row=3, column=0, sticky="e")
    entry_fecha_posible_parto = tk.Entry(root)
    entry_fecha_posible_parto.grid(row=3, column=1)

    tk.Label(root, text="Fecha de secado:").grid(row=4, column=0, sticky="e")
    entry_fecha_secado = tk.Entry(root)
    entry_fecha_secado.grid(row=4, column=1)

    tk.Label(root, text="Concepción exitosa:").grid(row=5, column=0, sticky="e")
    var_concepcion_exitosa = tk.StringVar(value="No")
    tk.OptionMenu(root, var_concepcion_exitosa, "Sí", "No").grid(row=5, column=1)

    tk.Label(root, text="Observaciones:").grid(row=6, column=0, sticky="ne")
    text_observaciones = tk.Text(root, width=30, height=4)
    text_observaciones.grid(row=6, column=1)

    tk.Button(root, text="Guardar", command=agregar_vaca).grid(row=7, column=0, pady=10)
    tk.Button(root, text="Limpiar", command=limpiar_campos).grid(row=7, column=1, pady=10)