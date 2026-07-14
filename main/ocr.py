"""
Modulo de extraccion OCR para imagenes de consulta vehicular SUNARP.

Usa pytesseract para extraer texto de la imagen y luego parsea
los campos estructurados con un mapeo posicional (labels y valores
se extraen en columnas separadas por Tesseract).
"""
import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


def extraer_texto_imagen(imagen):
    # 1. Leer la imagen
    file_bytes = np.frombuffer(imagen.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # 2. Escalar la imagen (Mejora clave)
    image = image[160:,:]
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # 3. Convertir a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 4. Aplicar Blur para reducir el ruido
    blur = cv2.GaussianBlur(gray, (3,3), 0)

    # 5. Thresholding (Usar THRESH_BINARY para texto negro sobre fondo blanco)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # 6. Operación morfológica para hacer los caracteres más nítidos/sólidos
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    thresh = cv2.erode(thresh, kernel, iterations=1) 
    data = pytesseract.image_to_string(thresh, lang='spa',config='--psm 6')

    return data