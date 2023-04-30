
"""# New Section"""
import initiate
import sys
from io import StringIO
from amplpy import AMPL, tools
ampl = initiate.ampl
s = initiate.s
cont=initiate.cont
import tkinter as tk

import tkinter as tk

# Create the root window
root = tk.Tk()
root.geometry('300x200')

# Create the options for the first dropdown menu
# options_1 = ['Ghatkopar Railway Station', 'R-City Mall Ghatkopar', 'Vikhroli Railway Station', 'IIT Bombay', 'Kanjurmarg Railway station', 'Magnet Mall Bhandup', 'Bhandup Railway Station', 'Nahur Railway Station', 'Fortis Mulund', 'Mulund Railway Station', 'Thane railway Station', 'Ashok Cinema Thane']
options_1 = [ "Ghatkopar railway station", "Rcity mall ghatkopar", "Vikhroli railway station","IIT Bombay", "Kanjurmarg Railway station","Bhandup railway station", "Nahur railway station","Fortis mulund","Mulund railway station", "Lok Everest", "Malhar Cinema", "Thane railway station"]
# [ "Ghatkopar railway station", "Sujog Urology Centre", "Rcity mall ghatkopar", "91springboard Vikhroli", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Dreams Mall Bhandup", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "THC Thane Health Clinic", "Thane railway station"]
print(cont)
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
options_2 = [ "Ghatkopar railway station", "Rcity mall ghatkopar", "Vikhroli railway station","IIT Bombay", "Kanjurmarg Railway station","Bhandup railway station", "Nahur railway station","Fortis mulund","Mulund railway station", "Lok Everest", "Malhar Cinema", "Thane railway station"]
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

# Adding a STOP


# Create the options for the second dropdown menu
# options_2 = ['Ghatkopar Railway Station', 'R-City Mall Ghatkopar', 'Vikhroli Railway Station', 'IIT Bombay', 'Kanjurmarg Railway station', 'Magnet Mall Bhandup', 'Bhandup Railway Station', 'Nahur Railway Station', 'Fortis Mulund', 'Mulund Railway Station', 'Thane railway Station', 'Ashok Cinema Thane']
options_3 = [ "No Stop","Ghatkopar railway station", "Suyog Urology Centre", "Rcity mall ghatkopar", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "Malhar Cinema", "Thane railway station"]
# [ "Ghatkopar railway station", "Sujog Urology Centre", "Rcity mall ghatkopar", "91springboard Vikhroli", "Vikhroli railway station", "Hiranandani Garden", "IIT Bombay", "Kanjurmarg Railway station", "Runwal Forests", "Bhandup railway station", "Dreams Mall Bhandup", "Nadkarni Eye Care", "Lotus Multispeciality Hospital", "Nahur railway station", "Der Deutsche Park", "Ashford Royale", "Fortis mulund", "PVR Mulund", "Mulund railway station","Umiya Tower", "Lok Everest", "THC Thane Health Clinic", "Thane railway station"]
label_3 = tk.Label(root, text='Add a Stop')
label_3.pack()
# Create a variable to store the selected option for the second dropdown menu
selected_option_3 = tk.StringVar(root)
selected_option_3.set(options_3[0])  # Set the default value to the first option

# Create the second dropdown menu widget
dropdown_3 = tk.OptionMenu(root, selected_option_3, *options_3)
dropdown_3.pack()

# Create a function to handle the selection of an option in the second dropdown menu
stop = ""
def on_select_3(option):
    global stop
    selected_value_3 = selected_option_3.get()
    stop = selected_value_3
    print(f'You selected {selected_value_3} from the second dropdown menu')

# Bind the function to the second dropdown menu
selected_option_3.trace('w', lambda *args: on_select_3(selected_option_3.get()))

# Start the main event loop
root.mainloop()


# entr = input("Enter Source : ")
# exit = input("Enter Destination : ")
entry = entr[:3]
exity = exit[:3]
sto = stop[:3]
if(stop=="No Stop"):
        
    ampl.read('model_fix.mod')
    ampl.set['INTER'] = set(s.split())
else:
    ampl.read('model.mod')
    ampl.set['INTER'] = set(s.split())
# else:
#     # Open the file for reading
#     with open('model.mod', 'r') as f:
#         lines = f.readlines()

# # Replace the two lines with four new lines
#     lines[13:15] = ['subject to stop1: sum {(k,stop) in ROADS} Use[k,stop] = 1;\n', 'subject to stop2: sum {(stop,j) in ROADS} Use[stop,j] = 1;\n', 'sum {(i,k) in ROADS} Use[i,k] = sum {(k,j) in ROADS} Use[k,j];\n', 'data data.dat;\n']

#     # Open the file for writing
#     with open('model.mod', 'w') as f:
#         f.writelines(lines)
#     with open("model.mod", "r") as f:
#         lines = f.readlines()

#     with open("model.mod", "w") as f:
#         for i, line in enumerate(lines):
#             if i != 12:
#                 f.write(line)
#     subject to stop1: sum {(k,stop) in ROADS} Use[k,stop] = 1;
# subject to stop2: sum {(stop,j) in ROADS} USe[stop,j] = 1;
    # sum {(i,k) in ROADS} Use[i,k] = sum {(k,j) in ROADS} Use[k,j];
    # data data.dat;


    # ampl.read('model.mod')
    # ampl.set['INTER'] = set(s.split())
# ampl.set['LOCAL']= set(s6.split())


backup = sys.stdout

sys.stdout = StringIO()     # capture output


ampl.option["solver"] = "highs"
ampl.option["highs_options"] = "outlev=0"
ampl.param["entr"] = entry

ampl.param["exit"] = exity

if(stop=="No stop"):
    
    ampl.solve()
else:
    # ampl.param["stop"] = sto
    ampl.solve()
ampl.option["omit_zero_rows"]=1

ampl.display("Use")
out = sys.stdout.getvalue() # release output

sys.stdout.close()  # close the stream 
sys.stdout = backup # restore original stdout

# # RESTORING MODEL FILE
# with open('model_fix.mod', 'r') as file:
#     # Read the contents of the file into a list
#     file_contents = file.readlines()

# # Open the file in 'write' mode to write the modified content
# with open('model.mod', 'w') as file:
#     # Write the modified content to the file
#     file.writelines(file_contents)

# store the log likelihood data in a file
f = open("filename3.txt", "w") 
print(out, file=f)
f.close()
