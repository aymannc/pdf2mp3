import PySimpleGUI as sg
import pdftotext
from gtts import gTTS

langs = ["English", "French "]
window = sg.Window('Get filename example',
                   [[sg.Text('Filename')],
                    [sg.Input(), sg.FileBrowse('Chopse a pdf file ',
                                               file_types=(("PDF Files", "*.pdf"),))],
                    [sg.Text('Language :'), sg.DropDown(langs, default_value=langs[0])],
                    [sg.OK(), sg.Cancel()]])

event, values = window.Read()
window.close()
pdf = None
try:
    with open(values[0], "rb") as f:
        pdf = pdftotext.PDF(f)
except pdftotext.Error as e:
    print(e)
except TypeError as e:
    print("Didn't choose a file!", '\n', 'closed !')
except Exception as e:
    print(e)
if pdf:
    lang_option = values[1][:2].lower()
    string_of_text = ''.join(e for e in pdf)
    print(string_of_text)
    print("Processing ")
    final_file = gTTS(text=string_of_text, lang=lang_option)
    name = F"{values[0].split('/')[-1][:-4]}_{lang_option}.mp3"
    final_file.save(name)
    print(name, " is ready !")
