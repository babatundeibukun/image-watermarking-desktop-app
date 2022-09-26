from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='Users\Hp EliteBook\Downloads', title='Select an image:')


# print('filename')

# create a function to perform our watermark work
def add_watermark(image, wm_text):
    # Create the image object
    opened_image = Image.open(image)
    # get image size
    image_width, image_height = opened_image.size
    # to draw on the opened image
    draw = ImageDraw.Draw(opened_image)
    # specify a font size
    font_size = int(image_width / 15)
    font = ImageFont.truetype('arial.ttf', font_size)

    # coordinates where we want to place the text
    x, y = int(image_width / 2), int(image_height / 2)

    # add a watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    # show the image
    opened_image.show()


add_watermark(filename, 'babatundeibukun.com')
