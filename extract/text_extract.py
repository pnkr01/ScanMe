def detect_and_extract_text(textract_client,img_byte):
    return textract_client.detect_document_text(Document={'Bytes': img_byte})
def handle_response(response,text_widget,tk):
    extracted_text = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "WORD":
            extracted_text += item["Text"] + " "
    text_widget.delete('1.0', tk.END) 
    text_widget.insert(tk.END, extracted_text)