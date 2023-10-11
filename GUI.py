from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('900x600')
ws.config(bg='#EEEEEE')

frame_top = Frame(ws)
frame_top.pack(pady=(15,15))
frame_bottom = Frame(ws)
frame_bottom.pack(pady=(0,15))

message_input ='''input'''
message_output ='''output'''

text_box_input = Text(frame_bottom, height=30, width=50)
text_box_input.pack(expand=True, side=LEFT)
text_box_input.insert('end', message_input)
text_box_input.config(state='normal')

text_box_output = Text(frame_bottom, height=30, width=50)
text_box_output.pack(expand=True, side=LEFT)
text_box_output.insert('end', message_output)
text_box_output.config(state='disabled')

button = Button(frame_top, text='Sample')
button.pack(side=TOP)

ws.mainloop()