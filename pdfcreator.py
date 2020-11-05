import os
from fpdf import FPDF
from PIL import Image



directory = input("Enter the directory path name: ")
files = os.listdir(directory)
pathList = []
imageList = []


for file in files:
    path = os.path.join(directory, file)
    pathList.append(path)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in [f for f in filenames if f.endswith(".jpg")]:
            full_path = os.path.join(dirpath, filename)
            imageList.append(full_path)
    pdf = FPDF()
    imageList.sort()
    for i in range(0, len(imageList)):
        lista = imageList[i]
    for image in imageList:
        x = Image.open(os.path.join(path, image))
        width, height = x.size
        width, height = float(width * 0.264583), float(height * 0.264583)
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
        orientation = 'P' if width < height else 'L'
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']
        pdf.add_page(orientation=orientation)
        pdf.image(image, 0, 0, width, height)
    pdf.output(os.path.join(path, file) + '.pdf', "F")
    imageList.clear()
    print("PDF: '{0}' generated!".format(file))