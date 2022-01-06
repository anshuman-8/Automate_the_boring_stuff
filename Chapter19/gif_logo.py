
import os
from PIL import Image
from pathlib import Path

a=os.getcwd()+'/Chapter19'
type=input("Enterthe typeof the fule like png, jpg, gif.. : ")

for files in os.listdir(a):
    if not files.endswith("."+type.lower()):
        print(files)
        continue
    main=Image.open(Path(a,files))
    main=main.resize((600,500))
    logo=Image.open('Chapter19/cat.jpg').convert("RGBA")
    logo=logo.resize((65,55))
    main.paste(logo, (600-65,500-55),logo)
    # a=Path('Chapter19',)
    print("donekk")
    # main.save(os.path.join('withLogo', "."+type))
    main.save('Chapter19/doneLogo.png')





# gifi=Image.open('Chapter19/cat-computer.gif')
# gifisized=gifi.resize((500,500))


# gifisized.save("Chapter19/madeit.gif")