from tkinter import *
from Pemecah_Bacaan_Misa import main

def process():
    text_input = text_box_input.get(1.0, 'end')

    result = main(text_input)

    text_box_output.delete(1.0, 'end')

    text_box_output.insert('end', result)

ws = Tk()
ws.title('Pemecah Bacaan Misa v1.0')
ws.geometry('900x600')
ws.config(bg='#EEEEEE')

# strvar = StringVar(ws, name='str')

frame_top = Frame(ws)
frame_top.pack(pady=(15,15))
frame_bottom = Frame(ws)
frame_bottom.pack(pady=(0,15))

message_input ='masukan'
message_output ='luaran'

text_box_input = Text(frame_bottom, height=30, width=50)
text_box_input.pack(expand=True, side=LEFT, padx=(15,15))
text_box_input.insert('end', message_input)
text_box_input.config(state='normal')

sb_input = Scrollbar(frame_bottom)
sb_input.pack(fill=BOTH, side=LEFT)

text_box_input.config(yscrollcommand=sb_input.set)
sb_input.config(command=text_box_input.yview)

text_box_output = Text(frame_bottom, height=30, width=50)
text_box_output.pack(expand=True, side=LEFT, padx=(0,15))
text_box_output.insert('end', message_output)
text_box_output.config(state='normal')

button = Button(frame_top, text='Proses Bacaan', command=process)
button.pack(side=TOP)

sb_output = Scrollbar(frame_bottom)
sb_output.pack(fill=BOTH, side=LEFT)

text_box_output.config(yscrollcommand=sb_output.set)
sb_output.config(command=text_box_output.yview)

ws.mainloop()