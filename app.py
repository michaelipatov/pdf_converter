from utils import *


def main():
    home = Path.home()
    user_input = input('Select the required operation:\n'
          'Enter 1 to convert pdf to txt\n'
          'Enter 2 to create mp3 from txt\n'
          'Enter 3 to create mp3 from pdf\n')

    if user_input == "1":
        pdf_file = input('Enter file_name (for example - test.pdf):\n')
        path_pdf = Path(home, 'PycharmProjects', 'pdf_converter', 'files', pdf_file)
        print("Process in progress")
        convert_pdf_to_txt(path_pdf)
        print(convert_pdf_to_txt(path_pdf))

    elif user_input == "2":
        txt_file = input('Enter file_name (for example - test.txt):\n')
        language = input('Choose language (for example - en or ru):\n')
        path_txt = Path(home, 'PycharmProjects', 'pdf_converter', 'files', txt_file)
        print("Process in progress")
        create_mp3_from_txt(path_txt, language)
        print(create_mp3_from_txt(path_txt, language))

    elif user_input == "3":
        pdf_file = input('Enter file_name (for example - test.pdf):\n')
        language = input('Choose language (for example - en or ru):\n')
        path_pdf = Path(home, 'PycharmProjects', 'pdf_converter', 'files', pdf_file)
        print("Process in progress")
        create_mp3_from_pdf(path_pdf, language)
        print(create_mp3_from_pdf(path_pdf, language))

    else:
        return 'Something wrong Ebatb'


if __name__ == '__main__':
    main()
