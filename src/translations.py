from PyQt5.QtCore import QTranslator, QLocale

def setup_translator():
    translator = QTranslator()
    locale = QLocale.system().name()
    return translator

class TranslationManager:
    def __init__(self):
        self.translations = {
            'en': {
                'window_title': "MetaReviewX",
                'select_language': "Select Language:",
                'english': "English",
                'spanish': "Spanish",
                'select_files': "Select CSV Files:",
                'browse': "Browse",
                'output_location': "Output File Location:",
                'output_browse': "Browse",
                'process': "Process Files",
                'report_title': "Processing Report",
                'file_not_found': "File not found: {0}",
                'invalid_csv': "File is not CSV: {0}",
                'processing_error': "Error processing {0}: {1}",
                'no_valid_files': "ERROR: No valid CSV files to process.",
                'process_completed': "PROCESS COMPLETED",
                'output_file': "Output file: {0}",
                'total_records': "Total records processed: {0}",
                'duplicates': "Duplicate records identified: {0}",
                'file_contents': "The file contains:",
                'all_sheet': "All",
                'all_sheet_description': "- Sheet 'All' with all articles (duplicates in yellow)",
                'year_sheets': "Year",
                'year_sheets_description': "- Sheets separated by year (without duplicate marking)",
                'summary_sheet': "Summary",
                'summary_sheet_description': "- Sheet 'Summary' with statistics",
                'footer': "- Made by: Ramiro Matta :)",
                'duplicates_report': "DUPLICATES REPORT",
                'total_duplicates': "Total duplicate records: {0}",
                'unique_duplicates': "Unique duplicate articles: {0}",
                'top_duplicates': "Top 10 most duplicated articles:",
                'no_title_column': "⚠ Warning: Column 'Title' not found",
                'no_valid_years': "⚠ No valid years identified in the data",
                'year': "Year",
                'total_articles': "Total Articles",
                'unique_articles': "Unique Articles",
                'duplicate_count': "Duplicates",
                'sources': "Sources"
            },
            'es': {
                'window_title': "MetaReviewX",
                'select_language': "Seleccionar Idioma:",
                'english': "Inglés",
                'spanish': "Español",
                'select_files': "Seleccionar archivos CSV:",
                'browse': "Examinar",
                'output_location': "Ubicación del archivo de salida:",
                'output_browse': "Examinar",
                'process': "Procesar Archivos",
                'report_title': "Reporte de Procesamiento",
                'file_not_found': "Archivo no encontrado: {0}",
                'invalid_csv': "El archivo no es CSV: {0}",
                'processing_error': "Error procesando {0}: {1}",
                'no_valid_files': "ERROR: No hay archivos CSV válidos para procesar.",
                'process_completed': "PROCESO COMPLETADO",
                'output_file': "✓ Archivo generado: {0}",
                'total_records': "✓ Total de registros procesados: {0}",
                'duplicates': "✓ Registros duplicados identificados: {0}",
                'file_contents': "El archivo contiene:",
                'all_sheet': "Todos",
                'all_sheet_description': "- Hoja 'Todos' con todos los artículos (duplicados en amarillo)",
                'year_sheets': "Año",
                'year_sheets_description': "- Hojas separadas por año (sin marcado de duplicados)",
                'summary_sheet': "Resumen",
                'summary_sheet_description': "- Hoja 'Resumen' con estadísticas",
                'footer': "- Hecho por: Ramiro Matta :)",
                'duplicates_report': "REPORTE DE DUPLICADOS",
                'total_duplicates': "Total de registros duplicados: {0}",
                'unique_duplicates': "Artículos únicos duplicados: {0}",
                'top_duplicates': "Top 10 artículos más duplicados:",
                'no_title_column': "⚠ Advertencia: No se encontró la columna 'Title'",
                'no_valid_years': "⚠ No se pudieron identificar años válidos en los datos",
                'year': "Año",
                'total_articles': "Total Artículos",
                'unique_articles': "Artículos Únicos",
                'duplicate_count': "Duplicados",
                'sources': "Fuentes"
            }
        }
    
    def get_translation(self, language, key, *args):
        if language in self.translations and key in self.translations[language]:
            return self.translations[language][key].format(*args)
        return key