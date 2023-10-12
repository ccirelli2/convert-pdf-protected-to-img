import os
import logging
import pypdfium2 as pdfium
from decouple import config as d_config

# Setup
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

# Globals
DIR_ROOT = d_config('DIR_ROOT')
DIR_DATA = d_config('DIR_DATA')
FILE_NAME = 'protected_pdf.pdf'

# Read Pdf
pdf = pdfium.PdfDocument(os.path.join(DIR_DATA, FILE_NAME))


