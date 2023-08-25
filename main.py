import tkinter as tk
from extract.text_extract import detect_and_extract_text, handle_response
from service.services import aws_config, text_extract_client
from util.image import image_handler
from util.label import label_wind, spacer

my_wind= tk.Tk()
my_wind.geometry("500x500")
my_wind.title("Extract Text from Scanned PDF")

label_wind(my_wind=my_wind,tk=tk)
spacer(my_wind=my_wind,tk=tk)

def upload_file():
    aws_mang_config = aws_config()
    textract_client = text_extract_client(aws_mang_config)
    global img
    img_byte = image_handler(tk,my_wind)
    spacer(my_wind=my_wind,tk=tk)
    response = detect_and_extract_text(textract_client,img_byte)
    handle_response(response,text_widget,tk)

extract_text_button = tk.Button(my_wind, text="Extract text", width=30, command=upload_file, padx=10)
extract_text_button.pack()
spacer(my_wind=my_wind,tk=tk)
text_widget = tk.Text(my_wind, wrap=tk.WORD, width=50, height=10)
spacer(my_wind=my_wind,tk=tk)
text_widget.pack()
my_wind.mainloop()
