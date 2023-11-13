
# --- Add 'file is opened' check when clearing output folder
# --- Default files selected when opening the software
# --- Reset button can replace Clear Output folder button completely
# --- Drag & Drop functionality

import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

welcome = 'Welcome to tpCDE Dummy Generator v1.01 - © 2021 by Paul Koops\n'\
          '-----------------------------------------------------------------------\n\n'
str_log = ''
txt_file = 'dummy_list.txt'
dummy_file = 'dummy.pdf'
extension = '.pdf'


def open_txt_file():
    global txt_file

    if not txt_file:
        txt_file = filedialog.askopenfilename()
        logging = 'Opening txt file:\n\n'
        logging += f'{txt_file}\n\n'

    else:
        logging = 'You have already selected a txt file.\n\n'
        logging += f'Current file:\n{txt_file}'

    str_log.set(logging)


def clear_txt_file():
    global txt_file

    logging = 'Removing txt file:\n\n'
    logging += f'{txt_file}\n\n'
    txt_file = ''
    str_log.set(logging)


def open_dummy_file():
    global dummy_file

    if not dummy_file:
        dummy_file = filedialog.askopenfilename()
        logging = 'Opening dummy PDF file:\n\n'
        logging += f'{dummy_file}\n\n'

    else:
        logging = 'You have already selected a dummy PDF file.\n\n'
        logging += f'Current file:\n{dummy_file}'

    str_log.set(logging)


def clear_dummy_file():
    global dummy_file

    logging = 'Removing dummy PDF file:\n\n'
    logging += f'{dummy_file}\n\n'
    dummy_file = ''
    str_log.set(logging)


def create_dummies():
    logging = 'Creating Dummies...\n\n'
    str_log.set(logging)

    filenames = []
    try:

        with open(txt_file) as file:
            for line in file.readlines():
                if extension not in line:
                    line = line[:-1] + extension
                filenames.append(line)

                print(filenames)
    except:
        logging = 'Error! You have not selected a (valid) TXT file!'
        str_log.set(logging)

    try:
        if filenames:
            for filename in filenames:
                shutil.copy(dummy_file, f'Output/{filename}')

            open_output_folder()

    except FileNotFoundError or UnicodeDecodeError:
        logging = 'Error! You have not selected a (valid) PDF file!'
        str_log.set(logging)

    logging += '\n\nProcess is finished!'

    str_log.set(logging)


def open_output_folder():
    import subprocess
    subprocess.Popen('explorer "Output"')


def clear_output_folder():
    import os
    import glob

    files = glob.glob('Output/*')
    for file in files:
        os.remove(file)

    logging = 'Output folder has been cleared!'
    logging += '\n\nProcess is finished!'

    str_log.set(logging)


def reset_all():
    global txt_file, dummy_file
    txt_file = ''
    dummy_file = ''
    clear_output_folder()
    str_log.set(welcome)


root = tk.Tk()
root.title('tpCDE - Dummy Generator - v1.01')
root.geometry('800x600')
root.resizable(False, True)
root.iconbitmap('Img/favicon.ico')

title = ttk.Frame(root, padding=25)
content = ttk.Frame(root, padding=50)
log_area = ttk.Frame(content, relief='sunken', borderwidth=5)

s = ttk.Style()
s.configure('Log.TFrame', background='white')

# ----- TITLE LABEL & LOGO-----
lbl_title = ttk.Label(title, text='Dummy Generator', font='TkTextFont 20 bold')
img_logo = tk.PhotoImage(file='Img/logo_tp_cde.png')
lbl_logo = ttk.Label(title, image=img_logo)

# ----- CONTENT LABELS-----
lbl_txt_file = ttk.Label(content, text='Select filenames TXT file', font='TkTextFont 14 normal')
lbl_dummy_file = ttk.Label(content, text='Select dummy PDF file', font='TkTextFont 14 normal', padding='0 0 0 25')
sep1 = ttk.Separator(content)
lbl_create = ttk.Label(content, text='Create Dummies', font='TkTextFont 14 normal', padding='0 25 0 0')
lbl_clear = ttk.Label(content, text='Clear Output folder', font='TkTextFont 14 normal', padding='0 0 0 25')

# ----- CONTENT BUTTONS -----
btn_txt_file = ttk.Button(content, text='Open', command=open_txt_file)
btn_txt_file_clear = ttk.Button(content, text='Clear', command=clear_txt_file)
btn_dummy_file = ttk.Button(content, text='Open', command=open_dummy_file)
btn_dummy_file_clear = ttk.Button(content, text='Clear', command=clear_dummy_file)
btn_create = ttk.Button(content, text='Create', command=create_dummies)
btn_show = ttk.Button(content, text='Show', command=open_output_folder)
btn_clear = ttk.Button(content, text='Clear', command=clear_output_folder)
btn_reset = ttk.Button(content, text='Reset', command=reset_all)

# ----- LOG -----
log_area.configure(height=400)
str_log = tk.StringVar()
lbl_logging = ttk.Label(log_area, textvariable=str_log, background='white', foreground='black', padding=20)

# ----- GEOMETRY MANGER -----
title.grid(row=0, column=0, sticky='N E S W')
lbl_title.grid(row=0, column=0, sticky='W')
lbl_logo.grid(row=0, column=1, sticky='E')

content.grid(row=1, column=0, sticky='N E S W')
lbl_txt_file.grid(row=0, column=0, sticky='W')
lbl_dummy_file.grid(row=1, column=0, sticky='W')

sep1.grid(row=2, column=0, columnspan=3, sticky='N E S W')

lbl_create.grid(row=3, column=0, sticky='W')
lbl_clear.grid(row=4, column=0, sticky='W')
btn_txt_file.grid(row=0, column=1, sticky='E')
btn_dummy_file.grid(row=1, column=1, sticky='N W')
btn_create.grid(row=3, column=1, sticky='E S')
btn_show.grid(row=3, column=2, sticky='S W')
btn_clear.grid(row=4, column=1, sticky='N E')
btn_txt_file_clear.grid(row=0, column=2, sticky='W')
btn_dummy_file_clear.grid(row=1, column=2, sticky='N W')

log_area.grid(row=5, column=0, columnspan=3, sticky='N E S W')
log_area.configure(style='Log.TFrame')
lbl_logging.grid(row=0, sticky='N W')
btn_reset.grid(row=6, column=0, sticky="S W")
1
root.columnconfigure(0, weight=1)
title.columnconfigure(0, weight=1)
title.columnconfigure(1, weight=1)
content.columnconfigure(0, weight=2)
content.columnconfigure(2, weight=3)


str_log.set(welcome)

root.mainloop()
