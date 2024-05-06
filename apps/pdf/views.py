from django.template.loader import render_to_string
from weasyprint import HTML
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
from apps.pdf.base_urls import PDF_BASE_FOLDER
import os




def create_pdf (request):
    context = {
        "STATIC_URL": settings.STATIC_URL,
    }

    html_template = render_to_string(
        "pdfs_templates/Certificado Servicio.html", context
    )
    pdf_file = HTML(
        string=html_template, base_url=request.build_absolute_uri()
    ).write_pdf()
    pdf_file = BytesIO(pdf_file)
    nombre_archivo = "example.pdf"
    ruta_carpeta_servidor = PDF_BASE_FOLDER
    ruta_completa_archivo = os.path.join(ruta_carpeta_servidor, nombre_archivo)

    with open(ruta_completa_archivo, "wb") as f:
        f.write(pdf_file.getvalue())

    response = HttpResponse(content_type="application/pdf")
    # response["Content-Disposition"] = f'attachment; filename="{nombre_archivo}"'
    response.write(pdf_file.getvalue())
    return response