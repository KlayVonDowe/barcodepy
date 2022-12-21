from barcode import Code128
from PIL import Image
from barcode.writer import ImageWriter
import os

desk = os.environ['USERPROFILE'] + "\\Desktop"

number = input(("Enter Barcode Number: "))
barcode = Code128(number, writer=ImageWriter())
newfilename = input(("Enter new file name: "))

image = barcode.save((desk + "\\" + newfilename))
Image.open(f'{image}').show()
print(image)
