import app_func
from HCap import handicap
import tkinter as tk
from tkinter import messagebox
from app_func import convert_strings_to_floats, save_me
from pandastable import Table, config
import pandas as pd

root = tk.Tk()

root.geometry("1400x1000")
root.title('GSCC Handicap Calculator')

global z
z = pd.DataFrame


label6 = tk.Label(root, text="There MUST be an equal number of grades and speeds", font=('Arial', 18), justify='center')
label6.grid(row=0, column=2, padx=10, pady=10)

label1 = tk.Label(root, text="Enter your grades in single space format - Limit E D C B Scratch", font=('Arial', 16))
label1.grid(row=1, column=2,padx=10, pady=10)
textbox1 = tk.Entry(root, width=40, justify='center', font=('Arial', 18))
textbox1.insert(tk.END, 'Limit E D C B Scratch')
textbox1.grid(row=2, column=2,padx=10, pady=10)

label2 = tk.Label(root, text="Enter your grades speed in single space format 29.5 32.0 33.5 35.5 37.0 39.0"
                  , font=('Arial', 16))
label2.grid(row=3, column=2,padx=20, pady=20)
textbox2 = tk.Entry(root, width=40, justify='center', font=('Arial', 18))
textbox2.insert(tk.END, '29.5 32.0 33.5 35.5 37.0 39.0')
textbox2.grid(row=4, column=2,padx=10, pady=10)


label3 = tk.Label(root, text='Enter your race start time in H:M:S format ', font=('Arial', 16))
label3.grid(row=5, column=2,padx=20, pady=20)
textbox3 = tk.Entry(root, width=10, justify='center', font=('Arial', 18))
textbox3.insert(tk.END, "10:00:00")
textbox3.grid(row=6, column=2,padx=20, pady=10)

label4 = tk.Label(root, text='Enter your race distance, in km, and in this format ', font=('Arial', 16))
label4.grid(row=7, column=2,padx=20, pady=20)
textbox4 = tk.Entry(root, width=10, justify='center', font=('Arial', 18))
textbox4.insert(tk.END,  37.7)
textbox4.grid(row=8, column=2,padx=20, pady=10)

label5 = tk.Label(root, text='Enter your merge point, in km before the finish, and in this format ', font=('Arial', 16))
label5.grid(row=9, column=2,padx=20, pady=20)
textbox5 = tk.Entry(root, width=6, justify='center', font=('Arial', 18))
textbox5.insert(tk.END,  1.5)
textbox5.grid(row=10, column=2,padx=20, pady=10)


def callback():

    a = textbox1.get().split()
    b = convert_strings_to_floats(textbox2.get().split())
    c = str(textbox3.get()).strip()
    d = textbox4.get()
    e = textbox5.get()

    # RUN the handicap function and return a dataframe this happens on clicking the update button ###############


# ERROR Handling

    def test_grade(num_grades):
        if len(num_grades) < 2:
            raise ValueError("You must have at least 2 grades")

    def test_grade_speed(grd, spd):
        if len(grd) != len(spd):
            raise ValueError("The number of grades MUST equal the number of speeds")

    def test_data_entry(tim, rdist, mdist):
        if tim == "" or rdist == "" or mdist == "":
            raise ValueError("Time, Race Distance or Merge Distance cannot be empty")

    def merge_gap (rd, gd):
        if (rd - gd) < (rd - 10):
            raise ValueError("The merge point of all the groups should be within 5km (max) of the finish.")

    try:
        test_grade(a)
        test_grade_speed(a, b)
        test_data_entry(c, d, e)
        merge_gap(float(d), float(e))
    except ValueError as m:
        # print (m)
        messagebox.showerror(m,m)

    else:
        df = handicap(a, b, c, float(d), float(e))

        global z
        z = df

        # print(df)
        pt.model.df = df
        pt.redraw()


Enter = tk.Button(
    root,

    text='Update Handicap Table',
    font=('Arial', 18, 'bold'),
    fg='white',
    bg="#3498db",
    command=callback

)

Enter.grid(row=11, column=0, padx=10, pady=10)


a = textbox1.get().split()
b = convert_strings_to_floats(textbox2.get().split())
c = str(textbox3.get()).strip()
d = float(textbox4.get())
e = float(textbox5.get())

frame = tk.Frame(root)
frame.grid(row=12, column=0, columnspan=5, sticky='EW')

# RUN the handicap function and return a dataframe this happens at start up and uses teh default values ###############

df = handicap(a, b, c, d, e)


z = df
# print(z)


pt = Table(frame, dataframe=df, showtoolbar=False, showstatusbar=False, height=200)


options = {'fontsize': 12, 'cellwidth': 120, 'align': 'center'}
config.apply_options(options, pt)


pt.model.df = df

pt.show()
pt.update()


def save_table():
    save_me(z)
    messagebox.showinfo("File Saved To:----", app_func.file_name)


save_table = tk.Button(
    root,

    text='Save Table to file',
    font=('Arial', 18, 'bold'),
    fg='white',
    bg="#3498db",
    command=save_table

)

save_table.grid(row=11, column=4, padx=5, pady=5)

root.mainloop()










