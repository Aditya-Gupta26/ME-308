# For making requisu=ite changes into mdp file to suit user needs

# index of data is 0,1 and so on

import tkinter as tk
import pandas as pd
import numpy as np
import restore
x = restore.x

# Create the root window
root = tk.Tk()
root.geometry('300x200')

# Create the options for the first dropdown menu
# options_1 = ['Ghatkopar Railway Station', 'R-City Mall Ghatkopar', 'Vikhroli Railway Station', 'IIT Bombay', 'Kanjurmarg Railway station', 'Magnet Mall Bhandup', 'Bhandup Railway Station', 'Nahur Railway Station', 'Fortis Mulund', 'Mulund Railway Station', 'Thane railway Station', 'Ashok Cinema Thane']
options_1 = [ "Ghatkopar railway station", "Suyog Urology Centre", "Rcity mall ghatkopar", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "THC Thane Health Clinic", "Thane railway station"]
# [ "Ghatkopar railway station", "Sujog Urology Centre", "Rcity mall ghatkopar", "91springboard Vikhroli", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Dreams Mall Bhandup", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "THC Thane Health Clinic", "Thane railway station"]
# print(cont)
label_1 = tk.Label(root, text='Enter Your Source Station')
label_1.pack()
# Create a variable to store the selected option for the first dropdown menu
selected_option_1 = tk.StringVar(root)
selected_option_1.set(options_1[0])  # Set the default value to the first option

# Create the first dropdown menu widget
dropdown_1 = tk.OptionMenu(root, selected_option_1, *options_1)
dropdown_1.pack()

# Create a function to handle the selection of an option in the first dropdown menu
entr=""
def on_select_1(option):
    global entr
    selected_value_1 = selected_option_1.get()
    entr = selected_value_1
    print(f'You selected {selected_value_1} from the first dropdown menu')

# Bind the function to the first dropdown menu
selected_option_1.trace('w', lambda *args: on_select_1(selected_option_1.get()))

# Create the options for the second dropdown menu
# options_2 = ['Ghatkopar Railway Station', 'R-City Mall Ghatkopar', 'Vikhroli Railway Station', 'IIT Bombay', 'Kanjurmarg Railway station', 'Magnet Mall Bhandup', 'Bhandup Railway Station', 'Nahur Railway Station', 'Fortis Mulund', 'Mulund Railway Station', 'Thane railway Station', 'Ashok Cinema Thane']
options_2 = [ "Ghatkopar railway station", "Suyog Urology Centre", "Rcity mall ghatkopar", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "THC Thane Health Clinic", "Thane railway station"]
# [ "Ghatkopar railway station", "Sujog Urology Centre", "Rcity mall ghatkopar", "91springboard Vikhroli", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Dreams Mall Bhandup", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "THC Thane Health Clinic", "Thane railway station"]
label_2 = tk.Label(root, text='Enter Your Destination Station')
label_2.pack()
# Create a variable to store the selected option for the second dropdown menu
selected_option_2 = tk.StringVar(root)
selected_option_2.set(options_2[0])  # Set the default value to the first option

# Create the second dropdown menu widget
dropdown_2 = tk.OptionMenu(root, selected_option_2, *options_2)
dropdown_2.pack()

# Create a function to handle the selection of an option in the second dropdown menu
exit = ""
def on_select_2(option):
    global exit
    selected_value_2 = selected_option_2.get()
    exit = selected_value_2
    print(f'You selected {selected_value_2} from the second dropdown menu')

# Bind the function to the second dropdown menu
selected_option_2.trace('w', lambda *args: on_select_2(selected_option_2.get()))

# Start the main event loop
root.mainloop()
print(entr,exit)
ind1 = options_1.index(entr)
ind2 = options_1.index(exit)

# Open the file in 'read' mode
with open('new_try.txt', 'r') as file:
    # Read the content of the file into a list
    file_content = file.readlines()

# Modify the list as needed (for example, replace the second line)
file_content[1] = 'numActions 5\n'
file_content[2] = 'end '+str(ind2)+'\n'



# Open the file in 'write' mode to write the modified content
with open('new_try.txt', 'w') as file:
    # Write the modified content to the file
    file.writelines(file_content)
with open('new_try.txt', 'r') as file:
    # Read the contents of the file into a list
    file_contents = file.readlines()

lines_to_delete = [i for i in range(4+(ind2)*24,28+(ind2)*24,1)]

# Remove the lines from the list
for index in sorted(lines_to_delete, reverse=True):
    del file_contents[index-1]

# Open the file in 'write' mode and write the modified contents back to it
with open('new_try.txt', 'w') as file:
    file.write(''.join(file_contents))



