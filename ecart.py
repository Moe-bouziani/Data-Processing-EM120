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

fontStyle = tkfont.Font(family="times new roman", size=10)
fontStyle_2 = tkfont.Font(family="times new roman", size=30)

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



entry4 = ttk.Entry(root)
canvas1.create_window(255, 200, window=entry4)

entry5 = ttk.Entry(root)
canvas1.create_window(255, 250, window=entry5)

button3 = ttk.Button(text="Fichier REV", command=txt_path)
canvas1.create_window(210, 290, window=button3)

button4 = ttk.Button(text="Fichier FOR", command=txt_path_2)
canvas1.create_window(300, 290, window=button4)
def get_values_2():
    b = entry4.get()
    a = entry5.get()
    try:
        y = float(b)
        x = int(a)
        guitest.ecart_type_function(float(b), pathing, pathing_2,int(a))
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

label5 = tkinter.Label(root, text="Valeur de début",font=fontStyle)
canvas1.create_window(130, 200, window=label5)
label5.configure(bg="#ff4500")

label7 = tkinter.Label(root, text="division",font=fontStyle)
canvas1.create_window(130, 250, window=label7)
label7.configure(bg="#ff4500")

label6 = tkinter.Label(root, text="Fichier Ecart Type",font=fontStyle_2)
canvas1.create_window(260, 60, window=label6)
label6.configure(bg="#ff4500")


button5 = ttk.Button(text="Créer votre Fichier Ecart-type", command=get_values_2)
canvas1.create_window(255, 330, window=button5)
root.mainloop()
