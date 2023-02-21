from translate import Translator
import os

def translate_html_file(html_file_path):
    if not os.path.isfile(html_file_path):
        print(f'Error: File "{html_file_path}" not found.')
        return

    # Load the HTML file contents into a string
    with open(html_file_path, 'r') as f:
        html_contents = f.read()

    # Create a Translator object and translate the HTML contents to Hindi
    translator = Translator(to_lang='hi')
    translated_html = translator.translate(html_contents)

    # Create a new file with the translated HTML contents
    output_file_path = f'translated_{os.path.basename(html_file_path)}'
    with open(output_file_path, 'w') as f:
        f.write(translated_html)

    return output_file_path

html_file_path = 'index.html'
output_file_path = translate_html_file(html_file_path)
print(f'Translated HTML saved to {output_file_path}')

