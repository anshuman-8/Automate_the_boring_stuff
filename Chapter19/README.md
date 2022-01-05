
# Chapter 19

## Manipulating Images

## Solutions
-----
1. What is an RGBA value?

    ***A***. RGBA stands for colours for each pixel i.e. Red Green Blue Alpha. modifying this we can make many different colours.
------

2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?

    ***A***. ImageColor.getcolor('CornflowerBlue','RGBA')
------

3. What is a box tuple?

    ***A***. A box tuple contains following values in a tuple (Left, Top, Right, Bottom) representing an rectangular region of an image.
------

4. What function returns an Image object for, say, an image file named zophie.png?

    ***A***. Image.open('image.png'); th open() function returns the image object.
------

5. How can you find out the width and height of an Image object’s image?

    ***A***. img=Image.open('image.png').size
------

6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?

    ***A***. 
------

7. After making changes to an Image object, how could you save it as an image file?

    ***A***. image.save('name.png')
------

8. What module contains Pillow’s shape-drawing code?

    ***A***. ImageDraw module
------

9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

    ***A***. ImageDraw.Draw() objects have drawing methods.
------