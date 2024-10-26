import tkinter as tk
from tkinter import messagebox

# Función para calcular el punto de equilibrio
def calcular_punto_equilibrio():
    try:
        precio_venta = float(entry_precio_venta.get())
        costo_variable = float(entry_costo_variable.get())
        gastos_fijos = float(entry_gastos_fijos.get())
        
        if precio_venta <= costo_variable:
            messagebox.showerror("Error", "El precio de venta debe ser mayor al costo variable")
            return
        
        # Cálculo del punto de equilibrio
        punto_equilibrio_unidades = gastos_fijos / (precio_venta - costo_variable)
        punto_equilibrio_quetzales = punto_equilibrio_unidades * precio_venta
        
        # Mostrar los resultados en celdas de entrada
        entry_resultado_unidades.config(state='normal')
        entry_resultado_unidades.delete(0, tk.END)
        entry_resultado_unidades.insert(0, f"{punto_equilibrio_unidades:.2f}")
        
        entry_resultado_quetzales.config(state='normal')
        entry_resultado_quetzales.delete(0, tk.END)
        entry_resultado_quetzales.insert(0, f"Q{punto_equilibrio_quetzales:.2f}")
        
        entry_resultado_unidades.config(state='readonly')
        entry_resultado_quetzales.config(state='readonly')
        
        # Llenar la tabla de datos
        tabla.delete(0, tk.END)  # Limpiar la tabla antes de llenarla
        niveles_unidades = [3000, 4000, 5000, 6000, 7000]
        
        for unidades in niveles_unidades:
            ventas = precio_venta * unidades
            costos_variables = costo_variable * unidades
            margen_contribucion = ventas - costos_variables
            utilidad_perdida = margen_contribucion - gastos_fijos
            
            # Insertar la fila en la tabla
            tabla.insert(tk.END, f"Unidades: {unidades}, Ventas: Q{ventas:.2f}, Costos Variables: Q{costos_variables:.2f}, "
                                  f"Margen de Contribución: Q{margen_contribucion:.2f}, Costos Fijos: Q{gastos_fijos:.2f}, "
                                  f"Utilidad/Pérdida: Q{utilidad_perdida:.2f}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

# Interfaz gráfica
root = tk.Tk()
root.title("Calculadora del Punto de Equilibrio")
root.configure(bg='#98FF98')  # Color de fondo verde menta

# Crear un frame para los inputs de datos
input_frame = tk.Frame(root, bg='#98FF98', padx=20, pady=20)
input_frame.pack(padx=20, pady=20)

# Etiquetas y campos de entrada dentro del frame de inputs
label_precio_venta = tk.Label(input_frame, text="Precio por Unidad (Q):", bg='#98FF98', fg='blue', font=("Arial", 12, "bold"))
label_precio_venta.grid(row=0, column=0, padx=10, pady=10)
entry_precio_venta = tk.Entry(input_frame, font=("Arial", 12))
entry_precio_venta.grid(row=0, column=1, padx=10, pady=10)

label_costo_variable = tk.Label(input_frame, text="Costo Variable por Unidad (Q):", bg='#98FF98', fg='blue', font=("Arial", 12, "bold"))
label_costo_variable.grid(row=1, column=0, padx=10, pady=10)
entry_costo_variable = tk.Entry(input_frame, font=("Arial", 12))
entry_costo_variable.grid(row=1, column=1, padx=10, pady=10)

label_gastos_fijos = tk.Label(input_frame, text="Gastos Fijos Mensuales (Q):", bg='#98FF98', fg='blue', font=("Arial", 12, "bold"))
label_gastos_fijos.grid(row=2, column=0, padx=10, pady=10)
entry_gastos_fijos = tk.Entry(input_frame, font=("Arial", 12))
entry_gastos_fijos.grid(row=2, column=1, padx=10, pady=10)

# Botón para calcular el punto de equilibrio
boton_calcular = tk.Button(input_frame, text="Calcular Punto de Equilibrio", command=calcular_punto_equilibrio, bg='lightblue', font=("Arial", 12, "bold"))
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Etiquetas y campos de entrada para mostrar el resultado
label_resultado_unidades = tk.Label(root, text="Punto de Equilibrio (Unidades):", bg='#98FF98', fg='blue', font=("Arial", 12, "bold"))
label_resultado_unidades.pack(pady=5)
entry_resultado_unidades = tk.Entry(root, state='readonly', font=("Arial", 12))
entry_resultado_unidades.pack(pady=5)

label_resultado_quetzales = tk.Label(root, text="Punto de Equilibrio (Quetzales):", bg='#98FF98', fg='blue', font=("Arial", 12, "bold"))
label_resultado_quetzales.pack(pady=5)
entry_resultado_quetzales = tk.Entry(root, state='readonly', font=("Arial", 12))
entry_resultado_quetzales.pack(pady=5)

# Tabla de resultados de datos
tabla = tk.Listbox(root, width=80, bg='white', font=("Arial", 12))
tabla.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
