#main.py
from HCap import handicap
import tkinter as tk
from Format_Conversions import convert_strings_to_floats
from pandastable import Table, config

root = tk.Tk()

root.geometry("1600x950")
root.title('GSCC Handicap Calculator')


label6 = tk.Label(root, text="There MUST be an equal number of grades and speeds", font=('Arial', 18), justify='center')
label6.pack(padx=10, pady=10)

label1 = tk.Label(root, text="Enter your grades in single space format - Limit E D C B Scratch", font=('Arial', 16))
label1.pack(padx=10, pady=10)
textbox1 = tk.Entry(root, width=40, justify='center', font=('Arial', 18))
textbox1.insert(tk.END, 'Limit E D C B Scratch')
textbox1.pack(padx=10, pady=10)

label2 = tk.Label(root, text="Enter your grades speed in single space format 29.5 32.0 33.5 35.5 37.0 39.0"
                  , font=('Arial', 16))
label2.pack(padx=20, pady=20)
textbox2 = tk.Entry(root, width=40, justify='center', font=('Arial', 18))
textbox2.insert(tk.END, '29.5 32.0 33.5 35.5 37.0 39.0')
textbox2.pack(padx=10, pady=10)


label3 = tk.Label(root, text='Enter your race start time in H:M:S format ', font=('Arial', 16))
label3.pack(padx=20, pady=20)
textbox3 = tk.Entry(root, width=10, justify='center', font=('Arial', 18))
textbox3.insert(tk.END, "10:00:00")
textbox3.pack(padx=20, pady=10)

label4 = tk.Label(root, text='Enter your race distance, in km, and in this format ', font=('Arial', 16))
label4.pack(padx=20, pady=20)
textbox4 = tk.Entry(root, width=10, justify='center', font=('Arial', 18))
textbox4.insert(tk.END,  37.7)
textbox4.pack(padx=20, pady=10)

label5 = tk.Label(root, text='Enter your merge point, in km before the finish, and in this format ', font=('Arial', 16))
label5.pack(padx=20, pady=20)
textbox5 = tk.Entry(root, width=6, justify='center', font=('Arial', 18))
textbox5.insert(tk.END,  1.5)
textbox5.pack(padx=20, pady=10)


def callback():

    a = textbox1.get().split()
    b = convert_strings_to_floats(textbox2.get().split())
    c = str(textbox3.get()).strip()
    d = float(textbox4.get())
    e = float(textbox5.get())

    df = handicap(a,b,c,d,e)

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

Enter.pack(padx=10, pady=10)

a = textbox1.get().split()
b = convert_strings_to_floats(textbox2.get().split())
c = str(textbox3.get()).strip()
d = float(textbox4.get())
e = float(textbox5.get())

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

df = handicap(a,b,c,d,e)


# print(isinstance(df, pd.DataFrame))
# print(df)


pt = Table(frame, dataframe=df, showtoolbar=False, showstatusbar=False)


options = {'fontsize': 12, 'cellwidth': 150, 'align': 'center'}
config.apply_options(options, pt)


pt.model.df = df

pt.show()
pt.update()


root.mainloop()





