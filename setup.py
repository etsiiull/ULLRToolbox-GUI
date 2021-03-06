import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": [	"os", "sys", "PySide.QtGui", "PySide.QtXml", "PySide.QtCore", "PySide.QtUiTools", "rpy2.rinterface", "time", "threading"],
					 "include_files": [("./forms/agregado.ui", "forms/agregado.ui"), 
									 ("./forms/analisis_anova_inter.ui", "forms/analisis_anova_inter.ui"), 
									 ("./forms/analisis_anova_intra.ui", "forms/analisis_anova_intra.ui"), 
									 ("./forms/analisis_anova_split.ui", "forms/analisis_anova_split.ui"), 
									 ("./forms/analisis_contr_inter.ui", "forms/analisis_contr_inter.ui"), 
									 ("./forms/analisis_contr_intra.ui", "forms/analisis_contr_intra.ui"), 
									 ("./forms/analisis_correlacion.ui", "forms/analisis_correlacion.ui"), 
									 ("./forms/analisis_descr_multiple.ui", "forms/analisis_descr_multiple.ui"), 
									 ("./forms/analisis_descr_univar.ui", "forms/analisis_descr_univar.ui"), 
									 ("./forms/analisis_regr_mediacion.ui", "forms/analisis_regr_mediacion.ui"), 
									 ("./forms/analisis_regr_multiple.ui", "forms/analisis_regr_multiple.ui"), 
									 ("./forms/crearvariable_algoritmo.ui", "forms/crearvariable_algoritmo.ui"), 
									 ("./forms/crearvariable_existente.ui", "forms/crearvariable_existente.ui"), 
									 ("./forms/crearvariable_funcion.ui", "forms/crearvariable_funcion.ui"), 
									 ("./forms/discretizar.ui", "forms/discretizar.ui"), 
									 ("./forms/extraer_muestras.ui", "forms/extraer_muestras.ui"), 
									 ("./forms/graf_cajas.ui", "forms/graf_cajas.ui"), 
									 ("./forms/graf_dispersion.ui", "forms/graf_dispersion.ui"), 
									 ("./forms/graf_frecuencias.ui", "forms/graf_frecuencias.ui"), 
									 ("./forms/graf_histograma.ui", "forms/graf_histograma.ui"), 
									 ("./forms/graf_percentiles.ui", "forms/graf_percentiles.ui"), 
									 ("./forms/mainwindow.ui", "forms/mainwindow.ui"), 
									 ("./forms/multiselect_column.ui", "forms/multiselect_column.ui"), 
									 ("./forms/recodificar.ui", "forms/recodificar.ui"), 
									 ("./forms/segmentado.ui", "forms/segmentado.ui"), 
									 ("./forms/sobre_nosotros.ui", "forms/sobre_nosotros.ui"), 
									 ("./forms/tipificar.ui", "forms/tipificar.ui"), 
									 ("./forms/transformar.ui", "forms/transformar.ui"), 
									 ("./resources/agregado.png", "resources/agregado.png"),
									 ("./resources/anova.png", "resources/anova.png"),
									 ("./resources/contraste_medias.png", "resources/contraste_medias.png"),
									 ("./resources/estadisticos_desc.png", "resources/estadisticos_desc.png"),
									 ("./resources/extraer_muestra.png", "resources/extraer_muestra.png"),
									 ("./resources/graficas.png", "resources/graficas.png"),
									 ("./resources/logo128x128.png", "resources/logo128x128.png"),
									 ("./resources/logo32x32.png", "resources/logo32x32.png"),
									 ("./resources/logo512x512.png", "resources/logo512x512.png"),
									 ("./resources/logo64x64.png", "resources/logo64x64.png"),
									 ("./resources/open.png", "resources/open.png"),
									 ("./resources/save.png", "resources/save.png"),
									 ("./resources/segmentado.png", "resources/segmentado.png"),
									 ("./resources/transformar.png", "resources/transformar.png"),
									 ("./resources/variable.png", "resources/variable.png"),
									 ("./script/ULLRtoolbox.v.1.0.R", "script/ULLRtoolbox.v.1.0.R"),
									 ("./samples/ejemplo.manova.Rdata", "samples/ejemplo.manova.Rdata"),
									 ("./samples/ejemplo_R.Rdata", "samples/ejemplo_R.Rdata"),
									 ("./samples/ejemplo_excel.xls", "samples/ejemplo_excel.xls"),
									 ("./samples/ejemplo_spss.sav", "samples/ejemplo_spss.sav"),
									 ("./samples/ejemplo_texto.txt", "samples/ejemplo_texto.txt"),
									 ("./samples/formato_fechas.xls", "samples/formato_fechas.xls"),
									 ("./samples/titanic.Rdata", "samples/titanic.Rdata"),
									 ("./resource.qrc", "./resource.qrc")  ], 
					 "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ullrtoolbox",
        version = "0.1",
        description = "Interfaz para ULLRtoolbox",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])