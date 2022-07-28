from gtts import gTTS
import pdfplumber
from pathlib import Path


def convert_pdf_to_txt(path_pdf):
    if Path(path_pdf).is_file() and Path(path_pdf).suffix == '.pdf':

        with pdfplumber.PDF(open(path_pdf, 'rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        file_name = Path(path_pdf).stem
        with open(f'files\{file_name}.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        return 'Conversion successful'

    else:
        return 'File not found'


def create_mp3_from_txt(path_txt, language):
    if Path(path_txt).is_file() and Path(path_txt).suffix == '.txt':

        with open(path_txt, 'r', encoding='utf-8') as file:
            text = file.read()
            text.replace('\n', '')
            my_audio = gTTS(text=text, lang=language, slow=False)
            file_name = Path(path_txt).stem
            my_audio.save(f'files\{file_name}.mp3')

        return f'{file_name}.mp3 saved successful'

    else:
        return 'File not found'


def create_mp3_from_pdf(path_pdf, language):
    if Path(path_pdf).is_file() and Path(path_pdf).suffix == '.pdf':

        with pdfplumber.PDF(open(path_pdf, 'rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(path_pdf).stem
        my_audio.save(f'files\{file_name}.mp3')

        return f'{file_name}.mp3 saved successful'

    else:
        return 'File not found'
