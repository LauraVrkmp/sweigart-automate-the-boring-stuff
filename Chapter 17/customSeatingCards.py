from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('invitations', exist_ok=True)
fontsFolder = 'C:\\Windows\\Fonts\\Cambria'
cambriaFont = ImageFont.truetype(os.path.join(fontsFolder, 'cambria.ttc'), 12)
cambriaFontLarge = ImageFont.truetype(os.path.join(fontsFolder, 'cambria.ttc'), 36)

CARD_WIDTH = 288
CARD_HEIGHT = 360

flower_img = Image.open('flower.png')

width, height = flower_img.size
flower_resized = flower_img.resize((int((CARD_WIDTH / (width * 1.5)) * width), 
                                    int((CARD_WIDTH / (width * 1.5)) * height)))
width_resized, height_resized = flower_resized.size

guests_file = open('guests.txt')
guests = guests_file.readlines()

max_name_length = 0

for guest in guests:
    if len(guest) > max_name_length:
        max_name_length = len(guest)

for guest in guests:
    im = Image.new('RGBA', (CARD_WIDTH, CARD_HEIGHT), 'white')
    im.paste(flower_resized, (CARD_WIDTH - width_resized, 
                              0), flower_resized)
    draw = ImageDraw.Draw(im)
    draw.line([(0, 0), (CARD_WIDTH - 1, 0), (CARD_WIDTH - 1, CARD_HEIGHT - 1), 
               (0, CARD_HEIGHT - 1)], fill='black')
    draw.text((20, 100), 'It would be a pleasure', fill='red', font=cambriaFont)
    draw.text((20, 120), 'to have the company of', fill='red', font=cambriaFont)
    draw.text((20, 145), guest[:-1], fill='purple', font=cambriaFontLarge)
    draw.text((20, 200), 'at 11010 Memory Lane on the Evening of', fill='red', font=cambriaFont)
    draw.text((20, 220), 'April 1st', fill='red', font=cambriaFont)
    draw.text((20, 240), 'at 7 o\'clock', fill='red', font=cambriaFont)

    
    im.save(os.path.join('invitations', 'invite %s.png' % (guest[:-1])))


# paragraph1 = doc.add_paragraph('It would be a pleasure to have the company of')
#     paragraph1.style = doc.styles['invitation1']
#     paragraph2 = doc.add_paragraph(guest[:-1])
#     paragraph2.style = doc.styles['invitation2']
#     paragraph3 = doc.add_paragraph('at 11010 Memory Lane on the Evening of')
#     paragraph3.style = doc.styles['invitation1']
#     paragraph4 = doc.add_paragraph('April 1st')
#     paragraph4.style = doc.styles['invitation3']
#     paragraph5 = doc.add_paragraph('at 7 o\'clock')