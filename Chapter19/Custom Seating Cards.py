from PIL import Image,ImageDraw,ImageFont
import os

card=Image.open('/home/anshuman/Desktop/Anshuman/Automate_the_boring_stuff/Chapter19/inv.jpg')
name=input("Enter your friends name: ")

card=card.resize((288,360))
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

draw=ImageDraw.Draw(card)
draw.line([(0,0),(288,0),(288,360),(0,360),(0,0)],fill='black')
draw.text((20,20),'Hello '+name,fill='Green')

draw.text((25,50),'Welcome to the playground',fill='Black',)
draw.text((25,60),'I welcome you to watch Arcane with me',fill='Black',)

card.save('./invite.png')