from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton

class ListaTareasApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de Tareas")

        self.lista_tareas = QListWidget(self)
        self.input_tarea = QLineEdit(self)
        self.boton_agregar = QPushButton("Agregar", self)
        self.boton_editar = QPushButton("Editar", self)
        self.boton_eliminar = QPushButton("Eliminar", self)

        #Diseño de la interfaz
        layout_principal = QVBoxLayout(self)
        layout_botones = QHBoxLayout()

        layout_principal.addWidget(self.lista_tareas)
        layout_principal.addWidget(self.input_tarea)

        layout_botones.addWidget(self.boton_agregar)
        layout_botones.addWidget(self.boton_editar)
        layout_botones.addWidget(self.boton_eliminar)

        layout_principal.addLayout(layout_botones)

        #conectar eventos a funciones
        self.boton_agregar.clicked.connect(self.agregar_tarea)
        self.boton_editar.clicked.connect(self.editar_tarea)
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)

    def agregar_tarea(self):
        tarea = self.input_tarea.text()
        if tarea:
            self.lista_tareas.addItem(tarea)
            self.input_tarea.clear()

    def editar_tarea(self):
        item_seleccionado = self.lista_tareas.currentItem()
        if item_seleccionado:
            nueva_tarea, aceptado = self.input_dialog("Editar Tarea", "Editar Tarea:", item_seleccionado.text())
            if aceptado:
                item_seleccionado.setText(nueva_tarea)

    def eliminar_tarea(self):
        item_seleccionado = self.lista_tareas.currentItem()
        if item_seleccionado:
            self.lista_tareas.takeItem(self.lista_tareas.row(item_seleccionado))

    def input_dialog(self, titulo, mensaje, valor_inicial=""):
        texto, aceptado = QtWidgets.QInputDialog.getText(self, titulo, mensaje, text=valor_inicial)
        return texto, aceptado

if __name__ == "__main__":
    app = QApplication([])
    ventana = ListaTareasApp()
    ventana.show()
    app.exec_()