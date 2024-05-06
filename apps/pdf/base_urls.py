from django.conf import settings
import os

PDF_BASE_FOLDER = str(settings.BASE_DIR) + "\\apps\\PDFS"

if not os.path.exists(PDF_BASE_FOLDER):
    os.makedirs(PDF_BASE_FOLDER)
    print(f"La carpeta {PDF_BASE_FOLDER} ha sido creada.")


