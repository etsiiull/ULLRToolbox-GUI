# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './forms/mainwindow.ui'
#
# Created: Sun Mar 30 21:09:58 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_datos = QtGui.QWidget()
        self.tab_datos.setObjectName("tab_datos")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_datos)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.grid_datos = QtGui.QGridLayout()
        self.grid_datos.setObjectName("grid_datos")
        self.tableWidget = QtGui.QTableWidget(self.tab_datos)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.grid_datos.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.grid_datos, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_datos, "")
        self.tab_resultados = QtGui.QWidget()
        self.tab_resultados.setObjectName("tab_resultados")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_resultados)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.list_variables = QtGui.QListWidget(self.tab_resultados)
        self.list_variables.setMaximumSize(QtCore.QSize(200, 16777215))
        self.list_variables.setObjectName("list_variables")
        self.gridLayout.addWidget(self.list_variables, 1, 0, 3, 1)
        self.text_result = QtGui.QTextBrowser(self.tab_resultados)
        self.text_result.setTabChangesFocus(False)
        self.text_result.setUndoRedoEnabled(False)
        self.text_result.setObjectName("text_result")
        self.gridLayout.addWidget(self.text_result, 3, 1, 1, 2)
        self.edit_comandos = QtGui.QTextEdit(self.tab_resultados)
        self.edit_comandos.setMaximumSize(QtCore.QSize(16777215, 100))
        self.edit_comandos.setObjectName("edit_comandos")
        self.gridLayout.addWidget(self.edit_comandos, 1, 1, 1, 1)
        self.label_lista = QtGui.QLabel(self.tab_resultados)
        self.label_lista.setObjectName("label_lista")
        self.gridLayout.addWidget(self.label_lista, 0, 0, 1, 1)
        self.label_resultados = QtGui.QLabel(self.tab_resultados)
        self.label_resultados.setObjectName("label_resultados")
        self.gridLayout.addWidget(self.label_resultados, 2, 1, 1, 2)
        self.label_ejecutar = QtGui.QLabel(self.tab_resultados)
        self.label_ejecutar.setObjectName("label_ejecutar")
        self.gridLayout.addWidget(self.label_ejecutar, 0, 1, 1, 2)
        self.button_ejecutar = QtGui.QPushButton(self.tab_resultados)
        self.button_ejecutar.setObjectName("button_ejecutar")
        self.gridLayout.addWidget(self.button_ejecutar, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_resultados, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName("menubar")
        self.mnu_archivo = QtGui.QMenu(self.menubar)
        self.mnu_archivo.setObjectName("mnu_archivo")
        self.mnu_datos = QtGui.QMenu(self.menubar)
        self.mnu_datos.setObjectName("mnu_datos")
        self.mnu_analisis = QtGui.QMenu(self.menubar)
        self.mnu_analisis.setObjectName("mnu_analisis")
        self.mnu_graficos = QtGui.QMenu(self.menubar)
        self.mnu_graficos.setObjectName("mnu_graficos")
        self.mnu_acerca = QtGui.QMenu(self.menubar)
        self.mnu_acerca.setObjectName("mnu_acerca")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.act_abrir = QtGui.QAction(MainWindow)
        self.act_abrir.setObjectName("act_abrir")
        self.act_guardar = QtGui.QAction(MainWindow)
        self.act_guardar.setObjectName("act_guardar")
        self.act_exportar = QtGui.QAction(MainWindow)
        self.act_exportar.setObjectName("act_exportar")
        self.act_agregado = QtGui.QAction(MainWindow)
        self.act_agregado.setObjectName("act_agregado")
        self.act_segmentado = QtGui.QAction(MainWindow)
        self.act_segmentado.setObjectName("act_segmentado")
        self.act_union = QtGui.QAction(MainWindow)
        self.act_union.setObjectName("act_union")
        self.act_variables = QtGui.QAction(MainWindow)
        self.act_variables.setObjectName("act_variables")
        self.act_descriptiva = QtGui.QAction(MainWindow)
        self.act_descriptiva.setObjectName("act_descriptiva")
        self.act_contraste = QtGui.QAction(MainWindow)
        self.act_contraste.setObjectName("act_contraste")
        self.act_anovas = QtGui.QAction(MainWindow)
        self.act_anovas.setObjectName("act_anovas")
        self.act_regresion = QtGui.QAction(MainWindow)
        self.act_regresion.setObjectName("act_regresion")
        self.act_logistica = QtGui.QAction(MainWindow)
        self.act_logistica.setObjectName("act_logistica")
        self.act_multivariado = QtGui.QAction(MainWindow)
        self.act_multivariado.setObjectName("act_multivariado")
        self.act_sobre = QtGui.QAction(MainWindow)
        self.act_sobre.setObjectName("act_sobre")
        self.act_graficos = QtGui.QAction(MainWindow)
        self.act_graficos.setObjectName("act_graficos")
        self.act_cerrar = QtGui.QAction(MainWindow)
        self.act_cerrar.setObjectName("act_cerrar")
        self.mnu_archivo.addSeparator()
        self.mnu_datos.addAction(self.act_agregado)
        self.mnu_datos.addAction(self.act_segmentado)
        self.mnu_datos.addAction(self.act_union)
        self.mnu_datos.addAction(self.act_variables)
        self.mnu_analisis.addAction(self.act_descriptiva)
        self.mnu_analisis.addAction(self.act_contraste)
        self.mnu_analisis.addAction(self.act_anovas)
        self.mnu_analisis.addAction(self.act_regresion)
        self.mnu_analisis.addAction(self.act_logistica)
        self.mnu_analisis.addAction(self.act_multivariado)
        self.mnu_graficos.addAction(self.act_graficos)
        self.mnu_acerca.addAction(self.act_sobre)
        self.menubar.addAction(self.mnu_archivo.menuAction())
        self.menubar.addAction(self.mnu_datos.menuAction())
        self.menubar.addAction(self.mnu_analisis.menuAction())
        self.menubar.addAction(self.mnu_graficos.menuAction())
        self.menubar.addAction(self.mnu_acerca.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.act_cerrar, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_datos), QtGui.QApplication.translate("MainWindow", "Vista de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lista.setText(QtGui.QApplication.translate("MainWindow", "Lista de variables", None, QtGui.QApplication.UnicodeUTF8))
        self.label_resultados.setText(QtGui.QApplication.translate("MainWindow", "Resultados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ejecutar.setText(QtGui.QApplication.translate("MainWindow", "Comando", None, QtGui.QApplication.UnicodeUTF8))
        self.button_ejecutar.setText(QtGui.QApplication.translate("MainWindow", "Ejecutar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_resultados), QtGui.QApplication.translate("MainWindow", "Vista de comandos", None, QtGui.QApplication.UnicodeUTF8))
        self.mnu_archivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.mnu_datos.setTitle(QtGui.QApplication.translate("MainWindow", "Datos", None, QtGui.QApplication.UnicodeUTF8))
        self.mnu_analisis.setTitle(QtGui.QApplication.translate("MainWindow", "Análisis", None, QtGui.QApplication.UnicodeUTF8))
        self.mnu_graficos.setTitle(QtGui.QApplication.translate("MainWindow", "Gráficos", None, QtGui.QApplication.UnicodeUTF8))
        self.mnu_acerca.setTitle(QtGui.QApplication.translate("MainWindow", "Acerca de", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.act_abrir.setText(QtGui.QApplication.translate("MainWindow", "Abrir archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.act_abrir.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.act_guardar.setText(QtGui.QApplication.translate("MainWindow", "Guardar archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.act_guardar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.act_exportar.setText(QtGui.QApplication.translate("MainWindow", "Exportar", None, QtGui.QApplication.UnicodeUTF8))
        self.act_agregado.setText(QtGui.QApplication.translate("MainWindow", "Agregado", None, QtGui.QApplication.UnicodeUTF8))
        self.act_segmentado.setText(QtGui.QApplication.translate("MainWindow", "Segmentado", None, QtGui.QApplication.UnicodeUTF8))
        self.act_union.setText(QtGui.QApplication.translate("MainWindow", "Union", None, QtGui.QApplication.UnicodeUTF8))
        self.act_variables.setText(QtGui.QApplication.translate("MainWindow", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.act_descriptiva.setText(QtGui.QApplication.translate("MainWindow", "Estadistica descriptiva", None, QtGui.QApplication.UnicodeUTF8))
        self.act_contraste.setText(QtGui.QApplication.translate("MainWindow", "Contraste de medias", None, QtGui.QApplication.UnicodeUTF8))
        self.act_anovas.setText(QtGui.QApplication.translate("MainWindow", "ANOVA", None, QtGui.QApplication.UnicodeUTF8))
        self.act_regresion.setText(QtGui.QApplication.translate("MainWindow", "Regresión múltiple", None, QtGui.QApplication.UnicodeUTF8))
        self.act_logistica.setText(QtGui.QApplication.translate("MainWindow", "Logística", None, QtGui.QApplication.UnicodeUTF8))
        self.act_multivariado.setText(QtGui.QApplication.translate("MainWindow", "Análisis multivariado", None, QtGui.QApplication.UnicodeUTF8))
        self.act_sobre.setText(QtGui.QApplication.translate("MainWindow", "Sobre ULLRToolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.act_graficos.setText(QtGui.QApplication.translate("MainWindow", "Añadir gráficos", None, QtGui.QApplication.UnicodeUTF8))
        self.act_cerrar.setText(QtGui.QApplication.translate("MainWindow", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.act_cerrar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))

