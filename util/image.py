from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from tkinter import filedialog

from util.label import spacer

def get_image_byte(filename):
    with open(filename,'rb') as imgfile:
        return imgfile.read()
    
def image_handler(tk,my_wind):
    f_types = [("JPG File", "*.jpg")]
    file_name = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(file_name)
    img_reize = img.resize((400, 250))
    img = ImageTk.PhotoImage(img_reize)
    img_byte = get_image_byte(file_name)
    b2 = tk.Label(my_wind, image=img, pady=10)
    b2.image = img 
    b2.pack()
    spacer(my_wind=my_wind,tk=tk)
    return img_byte