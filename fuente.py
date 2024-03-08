import tkinter as tk
from tkinter import messagebox

class NodoEmpleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        self.siguiente = None

class ListaCircularEmpleados:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_empleado(self, nombre, salario):
        nuevo_empleado = NodoEmpleado(nombre, salario)
        if not self.primero:
            self.primero = nuevo_empleado
            self.ultimo = nuevo_empleado
        else:
            self.ultimo.siguiente = nuevo_empleado
            nuevo_empleado.siguiente = self.primero
            self.ultimo = nuevo_empleado

    def buscar_salario(self, nombre):
        if not self.primero:
            return None  # La lista está vacía

        actual = self.primero
        while True:
            if actual.nombre == nombre:
                return actual.salario

            actual = actual.siguiente
            if actual is None or actual == self.primero:
                return None  # No se encontró el empleado en la lista

    def eliminar_empleado(self, nombre):
        if not self.primero:
            return False  # La lista está vacía

        actual = self.primero
        anterior = self.ultimo

        while True:
            if actual.nombre == nombre:
                if actual == self.primero:
                    self.primero = actual.siguiente
                    self.ultimo.siguiente = self.primero
                    if actual == self.ultimo:
                        self.ultimo = anterior
                elif actual == self.ultimo:
                    anterior.siguiente = self.primero
                    self.ultimo = anterior
                else:
                    anterior.siguiente = actual.siguiente
                return True  # Empleado eliminado con éxito

            anterior = actual
            actual = actual.siguiente

            if actual is None or actual == self.primero:
                return False  # No se encontró el empleado en la lista

    def mostrar_lista(self):
        if not self.primero:
            return []  # La lista está vacía

        empleados = []
        actual = self.primero
        while True:
            empleados.append((actual.nombre, actual.salario))
            actual = actual.siguiente
            if actual is None or actual == self.primero:
                break

        return empleados

class AplicacionGestionEmpleados:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Empleados")

        self.lista_empleados = ListaCircularEmpleados()

        # Widgets
        self.label_nombre = tk.Label(master, text="Nombre:")
        self.label_salario = tk.Label(master, text="Salario:")

        self.entry_nombre = tk.Entry(master)
        self.entry_salario = tk.Entry(master)

        self.boton_agregar = tk.Button(master, text="Agregar Empleado", command=self.agregar_empleado)
        self.boton_buscar = tk.Button(master, text="Buscar Salario", command=self.realizar_busqueda_salario)
        self.boton_eliminar = tk.Button(master, text="Eliminar Empleado", command=self.eliminar_empleado)
        self.boton_mostrar_lista = tk.Button(master, text="Mostrar Lista", command=self.mostrar_lista)

        # Posicionamiento de widgets
        self.label_nombre.grid(row=0, column=0)
        self.label_salario.grid(row=1, column=0)
        self.entry_nombre.grid(row=0, column=1)
        self.entry_salario.grid(row=1, column=1)
        self.boton_agregar.grid(row=2, column=0, pady=10)
        self.boton_buscar.grid(row=2, column=1, pady=10)
        self.boton_eliminar.grid(row=3, column=0, columnspan=2)
        self.boton_mostrar_lista.grid(row=4, column=0, columnspan=2)

    def agregar_empleado(self):
        nombre = self.entry_nombre.get()
        salario_str = self.entry_salario.get()

        if not salario_str.isdigit():
            messagebox.showwarning("Error", "Por favor, ingrese un salario válido (solo números).")
            return

        salario = int(salario_str)

        if nombre and salario:
            self.lista_empleados.agregar_empleado(nombre, salario)
            messagebox.showinfo("Éxito", "Empleado agregado correctamente.")
        else:
            messagebox.showwarning("Error", "Por favor, complete todos los campos.")

    def realizar_busqueda_salario(self):
        nombre = self.entry_nombre.get()

        if nombre:
            salario = self.lista_empleados.buscar_salario(nombre)
            if salario is not None:
                messagebox.showinfo("Resultado", f"El salario de {nombre} es {salario}.")
            else:
                messagebox.showwarning("Error", f"No se encontró el empleado {nombre} en la lista.")
        else:
            messagebox.showwarning("Error", "Por favor, ingrese el nombre del empleado.")

    def eliminar_empleado(self):
        nombre = self.entry_nombre.get()

        if nombre:
            if self.lista_empleados.eliminar_empleado(nombre):
                messagebox.showinfo("Éxito", f"Empleado {nombre} eliminado correctamente.")
            else:
                messagebox.showwarning("Error", f"No se encontró el empleado {nombre} en la lista.")
        else:
            messagebox.showwarning("Error", "Por favor, ingrese el nombre del empleado.")

    def mostrar_lista(self):
        empleados = self.lista_empleados.mostrar_lista()

        if empleados:
            lista_texto = "\n".join([f"{nombre}: {salario}" for nombre, salario in empleados])
            messagebox.showinfo("Lista de Empleados", lista_texto)
        else:
            messagebox.showinfo("Lista de Empleados", "La lista de empleados está vacía.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGestionEmpleados(root)
    root.mainloop()
