from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QAction, QFileDialog, QDesktopWidget, QMessageBox, QSizePolicy, QToolBar, QStatusBar, QDockWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import sys

class Editor(QMainWindow):

    def __init__(self):
        super(Editor, self).__init__()
        self.setFixedSize(650,650)
        self.setWindowTitle("Editor de imagenes")

        self.centrar_menu()
        self.barra_herramientas_botones()
        self.crear_menu()
        self.crear_barra_herramientas()
        self.widgets_edicion()


    def crear_menu(self):
        self.act_open = QAction(QIcon("open.png"), "Abrir", self)
        self.act_open.setShortcut("Ctrl+O")
        self.act_open.setStatusTip("Abrir nueva imagen")
        self.act_open.triggered.connect(self.abrir_imagen)

        self.act_save = QAction(QIcon("save.png"), "Guardar", self)
        self.act_save.setShortcut("Ctrl+S")
        self.act_save.setStatusTip("Guardar")
        self.act_save.triggered.connect(self.guardar_imagen)

        self.act_print = QAction(QIcon("printer.png"), "Imprimir", self)
        self.act_print.setShortcut("Ctrl+P")
        self.act_print.setStatusTip("Imprimir")
        self.act_print.triggered.connect(self.imprimir_imagen)

        self.act_exit = QAction(QIcon("exit.png"), "Salir", self)
        self.act_exit.setShortcut("Ctrl+Q")
        self.act_exit.setStatusTip("Salir")
        self.act_exit.triggered.connect(self.close)

        self.act_rotate90 = QAction(QIcon("rotate90.png"), "Rotar 90°", self)
        self.act_rotate90.setStatusTip("Rotar a 90°")
        self.act_rotate90.triggered.connect(self.rotar_90)

        self.act_rotate180 = QAction(QIcon("rotate180.png"), "Rotar 180°", self)
        self.act_rotate180.setStatusTip("Rotar 180°")
        self.act_rotate180.triggered.connect(self.rotar_180)

        self.act_rotar_horiz = QAction(QIcon("rotatetohor.png"), "Rotar Horizontal", self)
        self.act_rotar_horiz.setStatusTip("Rotar Horizontal")
        self.act_rotar_horiz.triggered.connect(self.rotar_horiz)

        self.act_rotar_vert = QAction(QIcon("rotatetovertical.png"), "Rotar Vertical", self)
        self.act_rotar_vert.setStatusTip("Rotar Vertical")
        self.act_rotar_vert.triggered.connect(self.rotar_vertical)

        self.act_resize = QAction(QIcon("resize.png"), "Redimensionar", self)
        self.act_resize.setStatusTip("Redimensionar")
        self.act_resize.triggered.connect(self.redimensionar)

        self.act_clear = QAction(QIcon("clear.png"), "Limpiar", self)
        self.act_clear.setShortcut("Ctrl+D")
        self.act_clear.setStatusTip("Limpiar imagen")
        self.act_clear.triggered.connect(self.limpiar_imagen)

        menu_bar = self.menuBar()

        menu_file = menu_bar.addMenu("Archivo")
        menu_file.addAction(self.act_open)
        menu_file.addSeparator()
        menu_file.addAction(self.act_save)
        menu_file.addSeparator()
        menu_file.addAction(self.act_print)
        menu_file.addSeparator()
        menu_file.addAction(self.act_exit)

        menu_edit = menu_bar.addMenu("Edición")
        menu_edit.addAction(self.act_rotate90)
        menu_edit.addAction(self.act_rotate180)
        menu_edit.addSeparator()
        menu_edit.addAction(self.act_rotar_horiz)
        menu_edit.addAction(self.act_rotar_vert)
        menu_edit.addSeparator()
        menu_edit.addAction(self.act_resize)
        menu_edit.addAction(self.act_clear)

        menu_view = menu_bar.addMenu("Ver")
        menu_view.addAction(self.act_herramientas_barra)

        self.setStatusBar(QStatusBar(self))


    def barra_herramientas_botones(self):
        self.barra_botones = QDockWidget("Barra de Botones")
        self.barra_botones.setAllowedAreas(Qt.LeftDockWidgetArea)

        self.contenedor = QWidget()

        self.btn_rotate90 = QPushButton("Rotar 90°", self)
        self.btn_rotate90.setMinimumSize(QSize(130,40))
        self.btn_rotate90.setStatusTip("Rotar imagen a 90°")
        self.btn_rotate90.setIcon(QIcon("rotate90.png"))
        self.btn_rotate90.clicked.connect(self.rotar_90)

        self.btn_rotate180 = QPushButton("Rotar 180°", self)
        self.btn_rotate180.setMinimumSize(QSize(130, 40))
        self.btn_rotate180.setStatusTip("Rotar imagen 180°")
        self.btn_rotate180.setIcon(QIcon("rotate180.png"))
        self.btn_rotate180.clicked.connect(self.rotar_180)

        self.btn_rotar_horiz = QPushButton("Rotar horizontal", self)
        self.btn_rotar_horiz.setMinimumSize(QSize(130, 40))
        self.btn_rotar_horiz.setStatusTip("Rotar imagen horizontal")
        self.btn_rotar_horiz.setIcon(QIcon("rotatetohor.png"))
        self.btn_rotar_horiz.clicked.connect(self.rotar_horiz)

        self.btn_rotar_vertical = QPushButton("Rotar vertical", self)
        self.btn_rotar_vertical.setMinimumSize(QSize(130, 40))
        self.btn_rotar_vertical.setStatusTip("Rotar imagen vertical")
        self.btn_rotar_vertical.setIcon(QIcon("rotatetovertical.png"))
        self.btn_rotar_vertical.clicked.connect(self.rotar_vertical)

        self.btn_resize = QPushButton("Redimensionar", self)
        self.btn_resize.setMinimumSize(QSize(130, 40))
        self.btn_resize.setStatusTip("Achicar la imagen a la mitad")
        self.btn_resize.setIcon(QIcon("resize.png"))
        self.btn_resize.clicked.connect(self.redimensionar)

        self.btn_exit = QPushButton("Salir", self)
        self.btn_exit.setMinimumSize(QSize(130, 40))
        self.btn_exit.setStatusTip("Cerrar la aplicación")
        self.btn_exit.setIcon(QIcon("exit.png"))
        self.btn_exit.clicked.connect(self.close)

        vlyt_botones = QVBoxLayout()
        vlyt_botones.addWidget(self.btn_rotate90)
        vlyt_botones.addWidget(self.btn_rotate180)
        vlyt_botones.addStretch(1)
        vlyt_botones.addWidget(self.btn_rotar_horiz)
        vlyt_botones.addWidget(self.btn_rotar_vertical)
        vlyt_botones.addStretch(1)
        vlyt_botones.addWidget(self.btn_resize)
        vlyt_botones.addStretch(1)
        vlyt_botones.addWidget(self.btn_exit)

        self.contenedor.setLayout(vlyt_botones)
        self.barra_botones.setWidget(self.contenedor)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.barra_botones)
        self.act_herramientas_barra = self.barra_botones.toggleViewAction()
    def crear_barra_herramientas(self):
        pass

    def centrar_menu(self):
        escritorio = QDesktopWidget().screenGeometry()
        ancho = escritorio.width()
        alto = escritorio.height()

        self.move((ancho - self.width()) // 2, (alto - self.height()) // 2)

    def widgets_edicion(self):
        self.imagen = QPixmap()
        self.lbl_imagen = QLabel()
        self.lbl_imagen.setAlignment(Qt.AlignCenter)
        self.lbl_imagen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        self.setCentralWidget(self.lbl_imagen)

    def abrir_imagen(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "",
                                                "jpg (*.jpeg *.jpg);; PNG (*.png);; GIF (*.gif)")

        if imagen:
            self.imagen = QPixmap(imagen)
            #Escalar la imagen
            self.lbl_imagen.setPixmap(self.imagen.scaled(self.lbl_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QMessageBox.information(self, "Error", "No se pudo abrir la imagen", QMessageBox.Ok)

    def guardar_imagen(self):
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Abrir imagen", "",
                                                "jpg (*.jpeg *.jpg);; PNG (*.png);; GIF (*.gif)")

        if nombre_archivo and self.imagen.isNull() == False:
            self.imagen.save(nombre_archivo)
        else:
            QMessageBox.information(self, "Error", "No se pudo guardar la imagen", QMessageBox.Ok)

    def imprimir_imagen(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat)

        print_dialog = QPrintDialog(printer)

        if (print_dialog.exec_()) == QPrintDialog.Accepted:
            painter = QPainter()
            painter.begin(printer)

            rect = QRect(painter.viewport())

            size = QSize(self.lbl_imagen.pixmap().size())
            size.scaled(rect.size(), Qt.KeepAspectRatio)

            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.lbl_imagen.pixmap().rect())

            painter.drawPixmap(0, 0, self.lbl_imagen.pixmap())
            painter.end()

    def rotar_90(self):
        if self.imagen.isNull() == False:
            transformacion = QTransform().rotate(90)
            pixmap = QPixmap(self.imagen)

            rotado = pixmap.transformed(transformacion)
            self.lbl_imagen.setPixmap(rotado.scaled(self.lbl_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.imagen = QPixmap(rotado)

            self.lbl_imagen.update()

    def rotar_180(self):
        if self.imagen.isNull() == False:
            transformacion = QTransform().rotate(180)
            pixmap = QPixmap(self.imagen)

            rotado = pixmap.transformed(transformacion)
            self.lbl_imagen.setPixmap(rotado.scaled(self.lbl_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.imagen = QPixmap(rotado)

            self.lbl_imagen.update()

    def rotar_horiz(self):
        if self.imagen.isNull() == False:
            transformacion = QTransform().scale(-1,1)
            pixmap = QPixmap(self.imagen)

            rotado = pixmap.transformed(transformacion)
            self.lbl_imagen.setPixmap(rotado.scaled(self.lbl_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.imagen = QPixmap(rotado)

            self.lbl_imagen.update()

    def rotar_vertical(self):
        if self.imagen.isNull() == False:
            transformacion = QTransform().scale(1, -1)
            pixmap = QPixmap(self.imagen)

            rotado = pixmap.transformed(transformacion)
            self.lbl_imagen.setPixmap(
                rotado.scaled(self.lbl_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.imagen = QPixmap(rotado)

            self.lbl_imagen.update()
    def redimensionar(self):
        if self.imagen.isNull() == False:
            transformacion = QTransform().scale(.5,.5)
            pixmap = QPixmap(self.imagen)

            rotado = pixmap.transformed(transformacion)
            self.lbl_imagen.setPixmap(self.imagen.scaled(self.lbl_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.imagen = QPixmap(rotado)

            self.lbl_imagen.update()
    def limpiar_imagen(self):
        self.lbl_imagen.clear()
        self.imagen = QPixmap()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec_())