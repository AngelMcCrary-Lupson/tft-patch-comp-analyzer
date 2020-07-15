import PySimpleGUI as sg
import queue
import threading
import getruntime
import getleague
import time

regions = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1']
leagues = ['Master', 'Grandmaster', 'Challenger']

def long_function_wrapper(work_id, gui_queue, values):

    print("Thread Start")
    getleague.getleague(values)
    gui_queue.put('{} ::: done'.format(work_id))

    return

def input_validation(values):
    print(values)
    if not ".json" in values['-FILESAVE-'][-5:]:
        print("bad input")
        return False
    elif not values['-LEAGUE-'] in leagues:
        print("bad input")
        return False
    elif not values['-REGION-'] in regions:
        print("bad input")
        return False
    elif not values['-LPMIN-'].isnumeric() or int(values['-LPMIN-']) < 0:
        print("bad input")
        return False
    elif not values['-MATCHES-'].isnumeric() or int(values['-MATCHES-']) < 0:
        print("bad input")
        return False
    print("good input")
    return True

def the_gui():
    sg.ChangeLookAndFeel('GreenTan')

    # ------ Menu Definition ------ #
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    # ------ Column Definition ------ #
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
                [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

    gui_queue = queue.Queue()

    layout = [

        [sg.Text('Please select a player league')],
        [sg.InputCombo(('Master', 'Grandmaster', 'Challenger'), size=(20, 1), key='-LEAGUE-', enable_events=True)],
        [sg.Text('Please select a player region')],
        [sg.InputCombo(('BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1'), size=(20, 1), key='-REGION-', enable_events=True)],

        [sg.Text('Please enter an LP minimum')],
        [sg.InputText(size=(5, 1), key='-LPMIN-', enable_events=True)],

        [sg.Text('Please enter the number of matches per player to collect data from')],
        [sg.InputText( size=(5, 1), key='-MATCHES-', enable_events=True)],

        [sg.Text('Please enter your Riot API key')],
        [sg.InputText(size=(50, 1), key='-API-', enable_events=True)],

        [sg.Text('Choose A Location to Save Data (must have .json extension)', size=(50, 1))],
        [sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),
            sg.Input(key='-FILESAVE-', enable_events=True), sg.FileSaveAs()],

        [sg.Button('Go'), sg.Cancel()]
    ]

    window = sg.Window('TFT Player Composition Analyzer', layout, default_element_size=(40, 1), grab_anywhere=False)
    event, values = window.read()

    work_id = 0
    while True:
        event, values = window.Read(timeout=100)

        if event is None or event == 'Cancel':
            window.close()
            break
        if event == 'Go':

            input_valid = input_validation(values)
            if input_valid:
                runtime = getruntime.construct(values)
                print(f"Runtime offset: {runtime}")
                if "status_code" in runtime.keys():
                    sg.Popup('Looks like one or more of your API key is invalid or the Riot API servers are down, please try again')
                else:
                    print("Build Thread")
                    thread_id = threading.Thread(target=long_function_wrapper, args=(work_id, gui_queue, values,), daemon=True)
                    thread_id.start()
                    for i in range(runtime["runtime"]):
                        time.sleep(1)
                        if not sg.OneLineProgressMeter('File Generating', i+1, runtime["runtime"], 'single'):
                            break
            else:
                sg.Popup('Looks like one or more of your inputs is invalid, please try again')
        try:
            message = gui_queue.get_nowait()
        except queue.Empty:
            message = None

        if message is not None:
            print("Completed")
            sg.Popup('Your file has finished generating!')
            window.close()
    return 1
