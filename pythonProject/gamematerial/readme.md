#Description of Pygame module

## Init
class Enemy(pygame.sprite.Sprite)

    def __init__(self):
        super().__init__() 
## coordinates
Pygames uses rectangular coordinates to store them 
>rect(left, top, width, height)


## movement
If you want to position the sprite you have to use rectangular coordinates.  

## Group
Groups are used to sort sprites
> group(sprites)
>
Groups are usefull as because you can use them like in this example
> enemies = pygame.sprite.Group(enemy1,enemy2,enem.....)
> player = pygame.sprite.Group(player1, player2,playe.....)

## Event
Events are very important as they can detect if a key was pressed but also you can create your own events.  
To create your own events simply use 'USEREVENT' like in this example:  
>OwnCustomEventName = pygame.USEREVENT
> 
This will turn the variable into a custom event.

## color
Color is used as in rgb(red,green,blue) style.   
You can give each color value a number from 0 to 255.  
But all Values are a integer so you can't use any decimal numbers.   

Example:
>color = (50,70,90)

## image loading
To load images you need to know where your image is located.

Example:
>Placeholder/Images/Image.png
> 

After that you need to load it in.

Example:
>Image = pygame.image.load(Placeholder/Images/Image.png)
>
To adjust where the image will be look at line 4

## Make a window
When you want to make a game you need of course a window to see your game.  
By using display you will automatically make an window.
You determines the size by using two integers so you can't use any decimal numbers.  

Example:
>Screen = pygame.display.set_mode((Width, Height))
## Close window
When you want to close the game and not by automatically clicking on the "X" you can use just pygame.exit.    
pygame.exit makes it possible to close the window.

Example:
>pygame.exit()
## Draw objects
By using pygame.draw you can draw 9 different shapes.  

###rectangle
By using pygame.draw.rect() you can draw a rectangle
You've got 4 values to change
1. surface  
This is just on what surface to draw on
2. color  
This determines the color of the lines
3. rect  
There are 4 integers to change.

Example:
>pygame.draw.rect(screen, (50,7...), (left,top,width,height)
4. width  
This value is optional to change as the default is always 0.  
0 means it will fill the rectangle  
Everything over 0 is used for the line thickness and everything below will draw nothing
###polygon
By using pygame.draw.polygon() you can draw a polygon.  
Polygon got every value the rectangle(line 64) has except "rect"(line 71)  
Instead you have "points"  
A sequence of 3 or more coordinates that will make up the corners.  
Each coordnates must be a list/tuple that contain 2 ints/floats
###circle
By using pygame.draw.circle() you will draw a circle.  
For the values you've got surface(line 67), color(line 69) and width(line76).  
The special ones for the circle are center and radius.  

1.center  
This determines where the circle center aka the position of the circle will be.  
The Value is made out of 2 ints/floats  

Example:
(67,55.5)

2.radius  
This determines how big the radius/circle will be.
It is made of one Int/Float

###elipse
By using pygame.draw.elipse() you can draw an elipse.   
For the values it has got the same as a rectangle(line 64).

###arc
By using pygame.draw.arc() you can draw an elipse.   
For the values it has got surface(line 67),color(line 69), width(line 76) and rect(line 71) to indicate the position.  
Special ones are start_angle and stop_angle.  

1.start_angle  
This Value is a float and determines the start angle of the arc in radians
2.end_angle
This will simply stops the angle of the arc in radians

###line
By using pygame.draw.line() it will simply just draw a straight line.  
For the values it has got surface(line 64),color(line 69)) and width(line 76).  
Special ones are just the start_pos and end_pos wich each has one list/tuple with 2 ints/floats.




