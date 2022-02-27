from tkinter import *
import constants

def apply():
    min_time_from = min_time_from_tf.get()
    min_time_to = int(min_time_to_tf.get())
    max_time_from = int(max_time_from_tf.get())
    max_time_to = int(max_time_to_tf.get())

    disp_tf.insert(0,'New values applied')

ws = Tk()
ws.title('Param')
ws.geometry('400x300')
ws.config(bg='#0f4b6e')

min_time_from_tf = Entry(ws)
min_time_from_tf.insert(END,constants.MIN_TIME_IN_STORE_FROM)
min_time_to_tf = Entry(ws)
min_time_to_tf.insert(END,constants.MIN_TIME_IN_STORE_TO)
max_time_from_tf = Entry(ws)
max_time_from_tf.insert(END,constants.MAX_TIME_IN_STORE_FROM)
max_time_to_tf = Entry(ws)
max_time_to_tf.insert(END,constants.MAX_TIME_IN_STORE_TO)
nb_client_per_checkout_tf = Entry(ws)
nb_client_per_checkout_tf.insert(END,constants.NB_CLIENT_PER_CHECKOUT)
max_waiting_time_before_checkout_tf = Entry(ws)
max_waiting_time_before_checkout_tf.insert(END,constants.MAX_WAITING_TIME_BEFORE_CHECKOUT)

min_time_from_lbl = Label(
    ws,
    text='Minimum time in store from (>5):',
    bg='#0f4b6e',
    fg='white'
)
min_time_to_lbl = Label(
    ws,
    text='Minimum time in store to (<10):',
    bg='#0f4b6e',
    fg='white'
)
max_time_from_lbl = Label(
    ws,
    text='Maximum time in store from (>20):',
    bg='#0f4b6e',
    fg='white'
)
max_time_to_lbl = Label(
    ws,
    text='Maximum time in store to (<120):',
    bg='#0f4b6e',
    fg='white'
)
nb_client_per_checkout_lbl = Label(
    ws,
    text='Max number of client per checkout (1-5):',
    bg='#0f4b6e',
    fg='white'
)
max_waiting_time_before_checkout_lbl = Label(
    ws,
    text='Max waiting time before checkout (1-10):',
    bg='#0f4b6e',
    fg='white'
)

min_time_from_lbl.pack()
min_time_from_tf.pack()
min_time_to_lbl.pack()
min_time_to_tf.pack()
max_time_from_lbl.pack()
max_time_from_tf.pack()
max_time_to_lbl.pack()
max_time_to_tf.pack()
nb_client_per_checkout_lbl.pack()
nb_client_per_checkout_tf.pack()
max_waiting_time_before_checkout_lbl.pack()
max_waiting_time_before_checkout_tf.pack()

btn = Button(
    ws,
    text='Apply',
    relief=SOLID,
    command=apply
)
btn.pack(pady=10)

disp_tf = Entry(
    ws, 
    width=38,
    font=('Arial', 14)
    )

disp_tf.pack(pady=5)


ws.mainloop()