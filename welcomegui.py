import PySimpleGUI as sg
import generategui
import barchart
from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

def plot_fig(fig):
    sg.theme('LightGreen')

    layout = [[sg.Text('Plot TFT Test')],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Button('Back')]]

# create the form and show it without the plot
    window = sg.Window('Demo Application TFT', layout, finalize=True, element_justification='center', font='Helvetica 18')
    # add the plot to the window
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    event, values = window.read()
    window.close()
    return 1

sg.theme('Dark Blue 3')
# Welcome Window layout
layout = [
            [sg.Text('Welcome'), sg.Text('', key='-OUTPUT-')],
            [sg.Text('Would you like to generate TFT player composition data or read a data file?')],
            [sg.Button('Generate'), sg.Button('Read'), sg.Button('Exit')]
         ]

layout_read = [
                [sg.Text('Filename')],
                [sg.Input(key='-FILEIN-', enable_events=True), sg.FileBrowse()],
                [sg.OK(), sg.Cancel()]
               ]

main_window = sg.Window('TFT Player Composition Analyzer', layout, location=(800,600))
fileread_active = False
i=0
file_valid = False
while True:             # Event Loop
    event, values = main_window.read(timeout=100)
    if event != sg.TIMEOUT_KEY:
        # print(i, event, values)
        continue
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Generate':
        main_window.Hide()
        gen_active = generategui.the_gui()
        if gen_active == 1:
            main_window.UnHide()
    i+=1
    if event == 'Read' and not fileread_active:     # only run if not already showing a fileread_window
        fileread_active = True
        main_window.Hide()
        fileread_window = sg.Window('Select a file to read', layout_read)

    if fileread_active:
        event, values = fileread_window.read(timeout=100)

        if event != sg.TIMEOUT_KEY:
            # print("fileread ", event)
            # print(values)
            continue
        if event == '-FILEIN-' and ".json" in values['-FILEIN-'][-5:]:
            file_valid = True
            # print("valid file")
        elif event == '-FILEIN-' and not ".json" in values['-FILEIN-'][-5:]:
            file_valid = False
            # print("invalid file")

        if event == 'Cancel' or event == sg.WIN_CLOSED:
            fileread_active = False
            fileread_window.close()

        if event == 'OK':
            # print(file_valid)
            if file_valid:
                try:
                    fig = barchart.gen_graph(values['-FILEIN-'])
                    fileread_window.Hide()
                    plot_active = plot_fig(fig)
                    if plot_active == 1:
                        fileread_active = True
                        fileread_window.UnHide()
                except:
                    sg.Popup('Error: Invalid File, Please Try Again')
                    fileread_window['-FILEIN-'].update("")
            else:
                sg.Popup('Error: Invalid File, Please Try Again')
                fileread_window['-FILEIN-'].update("")
    else:
        main_window.UnHide()

main_window.close()
