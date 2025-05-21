from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, 
                             QPushButton, QTextEdit, QFileDialog, QWidget, QLineEdit)
from PyQt5.QtCore import Qt, pyqtSignal
from processing import process_files
from translations import TranslationManager
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    language_changed = pyqtSignal(str)  # Señal para cambios de idioma
    
    def __init__(self, translator, default_language='en'):
        super().__init__()
        self.translator = translator
        self.translation_manager = TranslationManager()
        self.current_language = default_language
        self.updating_language = False  # Bandera para controlar actualizaciones
        self.setWindowIcon(QtGui.QIcon('../assets/icon.ico'))  # Asegúrate de tener el archivo en la ruta correcta
        
        # Lista de widgets que necesitan actualización de idioma
        self.translatable_widgets = []
        
        self.setup_ui()
        self.update_ui_language()
    
    def setup_ui(self):
        # Configuración inicial de la UI
        self.setWindowTitle(self.translation_manager.get_translation(self.current_language, 'window_title'))
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Language selection
        lang_layout = QHBoxLayout()
        self.lang_label = QLabel()
        self.lang_combo = QComboBox()
        self.lang_combo.addItem("English", 'en')
        self.lang_combo.addItem("Español", 'es')
        self.lang_combo.setCurrentIndex(0 if self.current_language == 'en' else 1)
        self.lang_combo.currentIndexChanged.connect(self.on_language_combo_changed)
        
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()
        main_layout.addLayout(lang_layout)
        
        # File selection
        file_layout = QHBoxLayout()
        self.file_label = QLabel()
        self.file_edit = QLineEdit()
        self.file_edit.setReadOnly(True)
        self.file_browse = QPushButton()
        self.file_browse.clicked.connect(self.browse_files)
        
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_edit)
        file_layout.addWidget(self.file_browse)
        main_layout.addLayout(file_layout)
        
        # Output location
        output_layout = QHBoxLayout()
        self.output_label = QLabel()
        self.output_edit = QLineEdit()
        self.output_browse = QPushButton()
        self.output_browse.clicked.connect(self.browse_output)
        
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_edit)
        output_layout.addWidget(self.output_browse)
        main_layout.addLayout(output_layout)
        
        # Process button
        self.process_btn = QPushButton()
        self.process_btn.clicked.connect(self.process)
        main_layout.addWidget(self.process_btn)
        
        # Report area
        self.report_label = QLabel()
        main_layout.addWidget(self.report_label)
        
        self.report_area = QTextEdit()
        self.report_area.setReadOnly(True)
        main_layout.addWidget(self.report_area)
        
        # Registrar widgets para actualización de idioma
        self.register_translatable_widgets()
        
        # Conectar señal de cambio de idioma
        self.language_changed.connect(self.handle_language_change)
    
    def register_translatable_widgets(self):
        """Registra todos los widgets que necesitan actualización de idioma"""
        self.translatable_widgets = [
            (self.lang_label, 'select_language'),
            (self.file_label, 'select_files'),
            (self.file_browse, 'browse'),
            (self.output_label, 'output_location'),
            (self.output_browse, 'output_browse'),
            (self.process_btn, 'process'),
            (self.report_label, 'report_title'),
            (self, 'window_title')  # Para el título de la ventana
        ]
    
    def update_ui_language(self):
        """Actualiza todos los textos de la interfaz según el idioma actual"""
        self.updating_language = True  # Activamos bandera
        
        for widget, key in self.translatable_widgets:
            if isinstance(widget, QLabel):
                widget.setText(self.translation_manager.get_translation(self.current_language, key))
            elif isinstance(widget, QPushButton):
                widget.setText(self.translation_manager.get_translation(self.current_language, key))
            elif isinstance(widget, QMainWindow):
                widget.setWindowTitle(self.translation_manager.get_translation(self.current_language, key))
        
        # Actualizar textos del combo box manteniendo la selección actual
        current_data = self.lang_combo.currentData()
        self.lang_combo.blockSignals(True)  # Bloqueamos señales temporalmente
        self.lang_combo.clear()
        self.lang_combo.addItem(self.translation_manager.get_translation(self.current_language, 'english'), 'en')
        self.lang_combo.addItem(self.translation_manager.get_translation(self.current_language, 'spanish'), 'es')
        self.lang_combo.setCurrentIndex(self.lang_combo.findData(current_data))
        self.lang_combo.blockSignals(False)  # Desbloqueamos señales
        
        self.updating_language = False  # Desactivamos bandera
    
    def on_language_combo_changed(self, index):
        """Manejador del cambio en el combo box de idioma"""
        if not self.updating_language:  # Solo procesar si no es una actualización programática
            new_language = self.lang_combo.itemData(index)
            self.language_changed.emit(new_language)
    
    def handle_language_change(self, new_language):
        """Maneja el cambio de idioma"""
        if new_language != self.current_language:
            self.current_language = new_language
            self.update_ui_language()
    
    def browse_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            self.translation_manager.get_translation(self.current_language, 'select_files'),
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        if files:
            self.file_edit.setText("; ".join(files))
    
    def browse_output(self):
        file, _ = QFileDialog.getSaveFileName(
            self,
            self.translation_manager.get_translation(self.current_language, 'output_location'),
            "",
            "Excel Files (*.xlsx);;All Files (*)"
        )
        if file:
            self.output_edit.setText(file)
    
    def process(self):
        input_files = self.file_edit.text().split("; ")
        output_file = self.output_edit.text()
        
        if not input_files or not output_file:
            return
        
        # Call the processing function
        success, report = process_files(input_files, output_file, self.current_language)
        
        # Display the report
        self.report_area.setPlainText(report)