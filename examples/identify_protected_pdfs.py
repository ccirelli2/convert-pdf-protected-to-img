import os
import logging
from PyPDF2 import PdfReader
from decouple import config as d_config

# Setup
logger = logging.getLogger(__name__)
logger.setLevel('INFO')

# Globals
DIR_ROOT = d_config('DIR_ROOT')
DIR_DATA = d_config('DIR_DATA')
FILE_NAME = 'protected_pdf.pdf'


# Create Reader
pdf = PdfReader(os.path.join(DIR_DATA, FILE_NAME))
logger.info('Pdf file loaded successfully')
print('Pdf file loaded successfully')

# Validate if Password Protected
is_encrypted = pdf.is_encrypted
logger.info(f'Pdf is encrypted => {is_encrypted}')
print(f'Pdf is encrypted => {is_encrypted}')
