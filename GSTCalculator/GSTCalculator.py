from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as m_box
import webbrowser

win = tk.Tk()
win.title("GST Calculator")
win.geometry("600x400")
win.minsize(600, 400)
win.maxsize(600, 400)
menubar = tk.Menu(win)


def onTouch():
    webbrowser.open_new_tab(r'https://www.linkedin.com/in/raj-bhatia-1790901a8/')


filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="About Developer", command=onTouch)

menubar.add_cascade(label="Help", menu=filemenu)
win.config(menu=menubar)

label_frame = ttk.LabelFrame(win, width=90)
label_frame.grid(row=0, column=0, padx=70, pady=80)
gst_label = ttk.Label(label_frame, text="Enter Your Amount : ")
gst_label.grid(row=0, column=0, padx=0, pady=15, sticky=tk.W)
gst_persent = ttk.Label(label_frame, text="Select Your GST Percent (%) : ")
gst_persent.grid(row=1, column=0, sticky=tk.W)
gst_amount = tk.StringVar()
gst_entry = ttk.Entry(label_frame, width=50, textvariable=gst_amount)
gst_entry.grid(row=0, column=1, padx=0, pady=5)
gst_entry.focus()
get_percentcomo = ttk.Combobox(label_frame, width=47, state='readonly')
get_percentcomo.grid(row=1, column=1)
get_percentcomo['values'] = (5, 12, 18, 28)
get_percentcomo.current(0)


def onClick():
    user_amount = gst_amount.get()
    user_gst = get_percentcomo.get()
    if user_amount != "":
        try:
            gst = int(user_amount)
        except ValueError:
            wrong = m_box.showerror(
                "Warning !", "Amounts are only in Digits !")
            gst_entry.delete(first=0, last=100)
            return wrong
        else:
            if int(user_amount) != 0:
                got_result = (gst / 100) * int(user_gst)
                right = m_box.showinfo(
                    "Successfully Calculated", f"Your GST Charge is {got_result}")
                gst_entry.delete(first=0, last=100)
                return right
            else:
                wrong2 = m_box.showerror(
                    "Warning !", "GST Amount is Can't be Zero !")
                gst_entry.delete(first=0, last=100)
                return wrong2
    else:
        wrong3 = m_box.showerror("Warning !", "GST Amount Can't be Blank")
        gst_entry.delete(first=0, last=100)
        return wrong3


cal_percent = ttk.Button(label_frame, text="Calculate GST", command=onClick)
cal_percent.grid(row=6, columnspan=6, padx=0, pady=20)
win.mainloop()
