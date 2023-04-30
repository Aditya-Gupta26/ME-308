import tkinter
from tkinter import Label, Button, Toplevel, Text
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk2 = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("Your Route")
frame = tkinter.Frame(root_tk)
frame2 = tkinter.Frame(root_tk2)
frame.pack(fill=tkinter.BOTH, expand=True)
frame2.pack(fill=tkinter.BOTH, expand=True)

# Create the text widget and pack it into the left side of the frame
text_widget = tkinter.Text(frame2)
text_widget.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)


# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# welcome = Label(root_tk, text="Here is your route", background="black", foreground="white")
# welcome.grid(row=0, column=1, columnspan=1)

# text = Text(root_tk, height=8)
# text.pack(side = tkinter.TOP())

# text_widget = tkinter.Text(root_tk)
# text_widget.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

# text.insert('1.0', 'This is a Text widget demo')
# text['state']='disabled'



# root.mainloop()

# def Rules():
#    rule_window = Toplevel(root_tk)
#    rule_window.title("The Rules")
#    the_rules = Label(rule_window, text="Here are the rules...", foreground="black")
#    the_rules.grid(row=0, column=0, columnspan=3)

# rules = Button(root_tk, text="Rules", command=Rules)
# rules.grid(row=1, column=0, columnspan=1)
# set current widget position and zoom
map_widget.set_position(19.126270,72.917427)
map_widget.set_zoom(15)
a1 = []
a2=[]
a3=[]
with open('output.txt') as f:
    lines = f.readlines()
    a1=lines[0].split(' ')

with open('output2.txt') as f:
    lines = f.readlines()
    a2=lines[0].split(', ')
with open('filename3.txt') as f:
    lines = f.readlines()
    a3 = lines
print(a3)

# 6 se lena hai -3 tak
text_widget.insert("1.0", "This is your route ->" + "\n")
end = ''
for i in range(6,len(a3)-3):
    start = a3[i][:-1]
    print(start)
    print(type(start))
    " ".join(start.split())
    print(start)
    final = start.split(' ')
    print(final)
    x = a1.index(final[0][:3])
    if(final[1]==''):
        end = final[2]
    else:
        end = final[1]
    y = a1.index(end[:3])
    val = str(i)+".0"
    print(val)
    if(len(final[0])==4 and final[0][-1]=="l") and (len(final[1])==4 and final[1][-1]=="l"):
         value = "Via Local " + str(a2[x][1:-1]) + " To " + str(a2[y][1:-1] + "\n")
         text_widget.insert("end",value)
    elif ((len(final[0])==3) and (len(final[1])==4 and final[1][-1]=="l")) or ((len(final[0])==4 and final[0][-1]=="l") and (len(final[1])==3)):
         value = "Change Local at " + str(a2[x][1:-1])  + "\n"
         text_widget.insert("end",value)

         ##############################################
    elif ((len(final[0])==3) and (len(final[1])==4 and final[1][-1]=="b")) or ((len(final[0])==4 and final[0][-1]=="b") and (len(final[1])==3)):
        value = "Change Bus at " + str(a2[x][1:-1])  + "\n"
        text_widget.insert("end",value)
    elif(len(final[0])==4 and final[0][-1]=="b") and (len(final[1])==4 and final[1][-1]=="b"):
         value = "Via Bus " + str(a2[x][1:-1]) + " To " + str(a2[y][1:-1] + "\n")
         text_widget.insert("end",value)
    elif((len(final[0])==4 and final[0][-1]=="l") and (len(final[1])==4 and final[1][-1]=="b")) or ((len(final[0])==4 and final[0][-1]=="b") and (len(final[1])==4 and final[1][-1]=="l")):
         value = "Change Train to Bus "+ str(a2[x][1:-1]) + " To " + str(a2[y][1:-1] + "\n")
         text_widget.insert("end",value)
        #################################################
    else:
         value = "Via Road " + str(a2[x][1:-1]) + " To " + str(a2[y][1:-1] + "\n")
         text_widget.insert("end",value)


   


text_widget['state']='disabled'
# print(a1)
for i in range(12):
    print(a2[i])
print(a2[1])
# marker = [None]*12
w=len(a2)
markers = []
for i in range(w):
    # marker = map_widget.set_address(cont[i], marker=True)
    # marker.set_text(s[i])
    if i==0:
        var1=a2[i][1:]
        a2[i]=var1
    if i==w-1:
        var2=a2[i][:-1]
        a2[i]=var2
    print(a2[i])
    markers.append(map_widget.set_address(a2[i], marker=True))
    # markers[i].set_text(a1[i])
    #marker_2=map_widget.set_address(a2[1][1:], marker=True)
    #marker[i]= map_widget.set_address(a1[i], marker=True)
# marker_1=map_widget.set_address(a2[0][1:], marker=True)
# marker_1.set_text(a1[0])
# print(marker_1.position)
# marker_2=map_widget.set_address("R-City Mall Ghatkopar, Mumbai", marker=True)
# # print(marker_2.position)
# marker_3=map_widget.set_address("IIT Bombay", marker=True)
# # set a path
# path_1 = map_widget.set_path([markers[0].position,marker_2.position])
# path_2 = map_widget.set_path([marker_2.position,marker_3.position])
end = ''
# 
for i in range(6,len(a3)-3):
    start = a3[i][:-1]
    print(start)
    print(type(start))
    " ".join(start.split())
    print(start)
    final = start.split(' ')
    print(final)
    x = a1.index(final[0][:3])
    
    if(final[1]==''):
        end = final[2]
    else:
        end = final[1]
    y = a1.index(end[:3])
    print(x,y)
    path_1 = map_widget.set_path([markers[x].position,markers[y].position])

print(a3)



# # methods
# path_1.set_position_list(new_position_list)
# path_1.add_position(position)
# path_1.remove_position(position)
# path_1.delete()
    
    


# print(marker_1.position, marker_1.text)  # get position and text

  # set new text
# marker_1.set_position(48.860381, 2.338594)  # change position
# marker_1.delete()
root_tk.mainloop()