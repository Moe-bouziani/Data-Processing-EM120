import tkinter
from tkinter import filedialog
import testedechargement
import guitest
from tkinter import ttk
from ttkthemes import themed_tk as tk
import tkinter.font as tkfont

root = tk.ThemedTk()
root.get_themes()
root.set_theme("clam")
root.title("Convertisseur des données de l'EM120")
root.iconbitmap("Logo-oncf.ico")
root.geometry("1200x600")
root.configure(bg="#ff4500")
canvas1 = tkinter.Canvas(root, width=500, height=600,highlightthickness=0)
canvas1.pack()
canvas1.configure(bg="#ff4500")
entry1 = ttk.Entry(root)
canvas1.create_window(250, 225, window=entry1)

# filename = PhotoImage(file = "OSE-EM120.png")
# background_label = Label(root, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
fontStyle = tkfont.Font(family="times new roman", size=10)
entry2 = ttk.Entry(root)
canvas1.create_window(250, 250, window=entry2)

fontStyle_2 = tkfont.Font(family="times new roman", size=30)

entry3 = ttk.Entry(root)
canvas1.create_window(250, 275, window=entry3)

#label1 = tkinter.Label(root, text="Entrez les valeurs de divisions", font=fontStyle)
#canvas1.create_window(250, 150, window=label1)
#label1.configure(bg="#ff4500")

label2 = tkinter.Label(root, text="de",font=fontStyle)
canvas1.create_window(170, 225, window=label2)
label2.configure(bg="#ff4500")

label3 = tkinter.Label(root, text="à",font=fontStyle)
canvas1.create_window(170, 250, window=label3)
label3.configure(bg="#ff4500")

label4 = tkinter.Label(root, text="Nom du fichier à créer",font=fontStyle)
canvas1.create_window(120, 275, window=label4)
label4.configure(bg="#ff4500")


def txt_path():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
        ("all files", "*.*"), ("txt files", "*.txt"), ("prn files","*.prn")))
    global pathing
    pathing = root.filename


def txt_path_2():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(
        ("all files", "*.*"), ("txt files", "*.txt"), ("prn files","*.prn")))
    global pathing_2
    pathing_2 = root.filename


button2 = ttk.Button(text="Selectionner votre fichier", command=txt_path)
canvas1.create_window(250, 170, window=button2)


def get_values():
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    try:
        y = float(x1)
        testedechargement.line_start_end(float(x1), float(x2), x3, pathing)
    except ValueError:
        root2 = tk.ThemedTk()
        root2.get_themes()
        root2.set_theme("radiance")
        root2.title("Echec")
        canvas2 = tkinter.Canvas(root2, width=450, height=40)
        canvas2.pack()
        label = ttk.Label(root2, text="Vérifiez les viariables entrez ou le type de fichier entrer !  ")
        canvas2.create_window(200, 20, window=label)
        root2.mainloop()


button1 = ttk.Button(text='Créer votre fichier excel', command=get_values)
canvas1.create_window(250, 315, window=button1)
label6 = tkinter.Label(root, text="Fichier Excel",font=fontStyle_2)
canvas1.create_window(250, 60, window=label6)
label6.configure(bg="#ff4500")



root.mainloop()
