import PySimpleGUI as sg
import getruntime
import getleague
import time

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

layout = [
    # [sg.Menu(menu_def, tearoff=True)],
    # [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    # [sg.Text('Here is some text.... and a place to enter text')],
    # [sg.InputText('This is my text')],
    # [sg.Frame(layout=[
    # [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],
    # [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    # [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
    #     sg.Multiline(default_text='A second multi-line', size=(35, 3))],
        # my inputs
    # [sg.InputCombo(('Master', 'Grandmaster', 'Challenger'), size=(20, 1)),
    #     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    # [sg.InputCombo(('BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1'), size=(20, 1)),
    #     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.Text('Please select a player league')],
    [sg.InputCombo(('Master', 'Grandmaster', 'Challenger'), size=(20, 1))],
    [sg.Text('Please select a player region')],
    [sg.InputCombo(('BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1', 'OC1', 'RU', 'TR1'), size=(20, 1))],

    [sg.Text('Please enter an LP minimum')],
    [sg.InputText('', size=(5, 1))],

    [sg.Text('Please enter the number of matches per player to collect data from')],
    [sg.InputText('', size=(5, 1))],

    [sg.Text('Please enter your Riot API key')],
    [sg.InputText('', size=(50, 1))],

    [sg.Text('Choose A Location to Save Data (must have .json extension)', size=(40, 1))],
    [sg.Text('Your File', size=(15, 1), auto_size_text=False, justification='right'),
        sg.InputText(''), sg.FileSaveAs()],
        # inputs
    # [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    # [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
    #     sg.Frame('Labelled Group',[[
    #     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
    #     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
    #     sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
    #     sg.Column(column1, background_color='#F7F3EC')]])],
    # [sg.Text('_'  * 80)],
    # [sg.Text('Choose A Folder', size=(35, 1))],
    # [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
    #     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]
]


window = sg.Window('TFT Player Composition Analyzer', layout, default_element_size=(40, 1), grab_anywhere=False)

event, values = window.read()

# some code that sends values to getleague.py
# results in either error incase key doesnt work or something else or a progress bar based
# off of approximate number of requests
# pop up for success saying where it was save
# give option to go back to generate more, main, or plot data

# *might have to seperate getleague and making requests to get approx runtime*
# *have the approx runtime request also validate the api key!



# sg.popup('Title',
#             'The results of the window.',
#             'The button clicked was "{}"'.format(event),
#             'The values are', values)
print(values)
runtime = getruntime.construct(values)

# for i in range(1000):   # this is your "work loop" that you want to monitor
#     sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')

getleague.getleague(values)
# need a thread to do progress bar
# for i in range(runtime):
#     time.sleep(1)
#     if not sg.OneLineProgressMeter('My 1-line progress meter', i+1, runtime, 'single'):
#         break

window.close()
