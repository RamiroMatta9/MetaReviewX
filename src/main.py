import sys
from PyQt5.QtWidgets import QApplication
from gui import MainWindow
from translations import setup_translator

def main():
    app = QApplication(sys.argv)
    
    # Configurar el traductor (inglés por defecto)
    translator = setup_translator()
    app.installTranslator(translator)
    
    # Crear y mostrar la ventana principal (inglés por defecto)
    window = MainWindow(translator, default_language='en')
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()