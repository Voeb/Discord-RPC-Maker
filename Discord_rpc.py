from pypresence import Presence
from tkinter import *
import validators

def DiscordRPC():
    client_id = client_id_input.get(1.0, "end-1c")
    if bool(client_id) == False:
        return None
    description_1 = description_1_input.get(1.0, "end-1c")
    if bool(description_1) == False:
        description_1 = "  "
    description_2 = description_2_input.get(1.0, "end-1c")
    if bool(description_2) == False:
        description_2 = "  "
    button_1 = button_1_label_input.get(1.0, "end-1c")
    if bool(button_1) == False:
        description_2 = "  "
    button_1_url = button_1_url_input.get(1.0, "end-1c")
    if bool(button_1_url) == True:
        if validators.url(button_1_url) != True:
            return None
    button_2 = button_2_label_input.get(1.0, "end-1c")
    if bool(button_2) == False:
        description_2 = "  "
    button_2_url = button_2_url_input.get(1.0, "end-1c")
    if bool(button_2_url) == True:
        if validators.url(button_2_url) != True:
            return None
    rpc = Presence(client_id)
    rpc.connect()
    rpc.update(details=description_1,
               state=description_2,
               large_image="sink_is_cool",
               large_text="Yes",
               small_image="sink_is_cool",
               small_text="Made by me, Sink",
               buttons=[{"label": button_1, "url": button_1_url}, {"label": button_2, "url": button_2_url}])
    print("Precense Updated")


window = Tk()
window.geometry("500x500")
window.title("Discord RPC")

# title
label1 = Label(window, text="Discord RPC maker", relief="solid", width=20, font=("arial",19,"bold"))
label1.place(x=250, y=53, anchor="center")

# client id input
client_id_text = Label(window, text="Client ID: (required)", font=("arial",10,"bold"))
client_id_text.place(x=250, y=100, anchor="center")

client_id_input = Text(window, height=1, width=25)
client_id_input.place(x=250, y=120, anchor='center')

# description line 1
description_1_text = Label(window, text="Description line 1:", font=("arial",10,"bold"))
description_1_text.place(x=250, y=140, anchor="center")

description_1_input = Text(window, height=1, width=25)
description_1_input.place(x=250, y=160, anchor='center')

# description line 2
description_2_text = Label(window, text="Description line 2:", font=("arial",10,"bold"))
description_2_text.place(x=250, y=180, anchor="center")

description_2_input = Text(window, height=1, width=25)
description_2_input.place(x=250, y=200, anchor='center')

# button 1 label
button_1_label = Label(window, text="Button 1 label:", font=("arial",10,"bold"))
button_1_label.place(x=250, y=220, anchor="center")

button_1_label_input = Text(window, height=1, width=25)
button_1_label_input.place(x=250, y=240, anchor='center')

# button 1 url
button_1_url_text = Label(window, text="Button 1 url: (required)", font=("arial",10,"bold"))
button_1_url_text.place(x=250, y=260, anchor="center")

button_1_url_input = Text(window, height=1, width=25)
button_1_url_input.place(x=250, y=280, anchor='center')

# button 2 label
button_2_label = Label(window, text="Button 2 label:", font=("arial",10,"bold"))
button_2_label.place(x=250, y=300, anchor="center")

button_2_label_input = Text(window, height=1, width=25)
button_2_label_input.place(x=250, y=320, anchor='center')

# button 1 url
button_2_url_text = Label(window, text="Button 2 url: (required)", font=("arial",10,"bold"))
button_2_url_text.place(x=250, y=340, anchor="center")

button_2_url_input = Text(window, height=1, width=25)
button_2_url_input.place(x=250, y=360, anchor='center')

launch_button = Button(window,
                 text="Launch",
                 width=12,
                 bg='green',
                 fg='white',
                 command= DiscordRPC)
launch_button.place(x=250, y=400, anchor="center")

window.mainloop()

