from email.policy import default
import PySimpleGUI as sg                        # Part 1 - The import
from pathlib import Path

from myowncipher import myowncipher

sg.theme('DarkAmber')

# Define the window's contents
layout = [[sg.Text("Welcome to stream cipher!")],     # Part 2 - The Layout
          [
              sg.Text("Input File Name"),
    sg.Input(key='-INPUT-'),
    sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*"))),
],
    [sg.Text("Output File Name"), sg.Input(key='OUTPUTFILE')],
    [sg.Text('_' * 80)],
    [sg.Text("Plain Text  "), sg.Multiline(size=(43, 3), key='PLAINTEXT')],
    [sg.Text("Key           "), sg.Input(key='KEY')],
    [sg.Text("Cipher Text"), sg.Multiline(size=(43, 3), key='CIPHERTEXT')],
    [sg.Button('Encrypt'), sg.Button('Decrypt'), sg.Button('Save Plain to File'), sg.Button('Save Cipher to File'), sg.Button('RESET')]]

# Create the window
# Part 3 - Window Defintion
window = sg.Window('Stream Cipher', layout)

while True:
    # Display and interact with the Window
    event, values = window.read()
    outputfile = "output.txt"

    if (values["OUTPUTFILE"]):
        outputfile = values["OUTPUTFILE"]

    print(event, values)

    if (values['-INPUT-']):
        filename = values['-INPUT-']
        if Path(filename).is_file():
            try:
                with open(filename, "rb") as f:
                    text = f.read()

                window.Element(key='PLAINTEXT').Update(text)

            except Exception as e:
                print("Error: ", e)

    if event == "Save Plain to File":
        with open(outputfile, 'wb') as f:
            f.write(bytes(values["PLAINTEXT"], "utf-8"))
    if event == "Save Cipher to File":
        with open(outputfile, 'wb') as f:
            f.write(bytes(values["CIPHERTEXT"], "utf-8"))
    if event == "RESET":
        window.Element(key="PLAINTEXT").Update("")
        window.Element(key="CIPHERTEXT").Update("")
        window.Element(key="KEY").Update("")
        window.Element(key="-INPUT-").Update("")
        window.Element(key="OUTPUTFILE").Update("")

    if event == "Encrypt":
        if (values["-INPUT-"]):
            cipher = myowncipher(
                bytes(values["KEY"], "utf-8"), text)
            with open(outputfile, 'wb') as f:
                f.write(cipher)
        else:
            cipher = myowncipher(
                bytes(values["KEY"], "latin-1"), bytes(values["PLAINTEXT"], "latin-1"))
            cipher = str(cipher, 'latin-1')
            window.Element(key='CIPHERTEXT').Update(cipher)

    elif event == "Decrypt":
        if (values["-INPUT-"]):
            plain = myowncipher(
                bytes(values["KEY"], "utf-8"), text)
            with open(outputfile, 'wb') as f:
                f.write(plain)
        else:
            plain = myowncipher(
                bytes(values["KEY"], "latin-1"), bytes(values["CIPHERTEXT"], "latin-1"))
            plain = str(plain, 'latin-1')
            window.Element(key='PLAINTEXT').Update(plain)

    if event == sg.WIN_CLOSED:
        break

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window
