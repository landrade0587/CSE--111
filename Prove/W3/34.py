"""
File: 34.py
Author: Luis Andrade
Date: 31 January 2023
Purpose: Prove that you can write functions with parameters and call those functions multiple times with arguments.
"""
# Import the funtion ramdom 
# Standard library imports
import random

# Import the functions from the Draw 2-D library
import draw2d 

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    # Width and height of the scene in pixels
    scene_width = 1100
    scene_height = 700

    # Call the start_drawing function in the draw2d.py 
    # library which will open a window and create a canvas.
    canvas = draw2d.start_drawing("Scene", scene_width, scene_height)
    
    # Call your drawing functions such as draw_sky 
    # and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_sun(canvas, "darkorange2")
    draw_clouds(canvas, "lightYellow1")
    draw_birds(canvas, "gray4")
               
    # Draw the ground and all the objects on the ground.
    draw_ground(canvas, scene_width, scene_height)
    draw_lake(canvas, "steelBlue2")
    draw_forest(canvas)  
  
    # Call the finish_drawing function in the draw2d.py library.
    draw2d.finish_drawing(canvas)

#class Sky    
def draw_sky(canvas, scene_width, scene_height):
    """Draw the cloud in the sky."""
    draw2d.draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="lightSkyBlue2")

#class Sun
def draw_sun(canvas, color):
   """Draw the sun in the sky""" 
   x = random.randrange(50, 900)
   y = random.randrange(400, 500)  
   draw2d.draw_oval(canvas, x, y, x + 100, y + 100, fill=color)


#Class Cloud
def draw_clouds(canvas, color):
    """Draw the clouds in the sky"""   
    draw_cloud(canvas, 30, color)
    draw_cloud(canvas, 20, color)
    draw_cloud(canvas, 10, color)
    draw_cloud(canvas, 80, color)
    draw_cloud(canvas, 40, color)
    draw_cloud(canvas, 60, color)

#Class Birds
def draw_birds(canvas, color):
    """Draw birds in the sky    """       
    draw_bird(canvas, -10, color)
    draw_bird(canvas, -20, color)
    draw_bird(canvas, -30, color)
    draw_bird(canvas, -40, color)
    draw_bird(canvas,-50, color)
    draw_bird(canvas, -60, color)
    draw_bird(canvas,60, color)
    draw_bird(canvas, 50, color)
    draw_bird(canvas, 40, color)
    draw_bird(canvas, 30, color)
    draw_bird(canvas, 20, color)
    draw_bird(canvas, 10, color)

#Class Ground
def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground."""
    draw2d.draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="oliveDrab4")

#Class Lake
def draw_lake(canvas, color):
    """Draw the lake."""
    draw2d.draw_oval(canvas, 850, 85, 750, 155, outline=color, fill=color)
    draw2d.draw_oval(canvas, 550, 55, 450, 135, outline=color, fill=color)
    draw2d.draw_oval(canvas, 750, 95, 950, 195, outline=color, fill=color)
    draw2d.draw_oval(canvas, 650, 85, 750, 145, outline=color, fill=color)
    draw2d.draw_oval(canvas, 450, 50, 850, 180, outline=color, fill=color)
    draw2d.draw_oval(canvas, 850, 55, 450, 125, outline=color, fill=color)

#Class Forest      
def draw_forest(canvas):
    """Draw the forest."""
    # Draw 15 small trees in a random location the scene end the ground
    # and with a high between 40 and 60 pixels
    for x in range(0, 500, 15):
        y = random.randrange(0, 80)
        z = random.randrange(40, 60)
        draw_pine_tree(canvas, x, y, z)
   
    # Draw 15 medium trees in a random location around the middle of the ground
    # and with a high between 70 and 80 pixels
    for x in range(0, 400, 15):
        y = random.randrange(80, 150)
        z = random.randrange(70, 80)
        draw_pine_tree(canvas, x, y, z)

    # Draw 15 big trees in a random location just in beging the ground 
    # and with a high between 90 and 100 pixels
    for x in range(0, 400, 15):
        y = random.randrange(150, 180)
        z = random.randrange(90, 100)
        draw_pine_tree(canvas, x, y, z)



#Class Pines tree
def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree."""
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw2d.draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray30", width=1, fill="orange4")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw2d.draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="tan4", width=1, fill="limegreen")


#Class Cloud aleatory in tne sky
def draw_cloud(canvas, startY, color):
    """Draw a cloud in a random location in the sky."""
    # The start x location where this function will start drawing the cloud.
    startX = random.randrange(100, 800) 
    draw2d.draw_oval(canvas, startX + 100, startY + 480, startX + 240, startY + 400, outline=color, fill=color)
    draw2d.draw_oval(canvas, startX + 130, startY + 430, startX + 280, startY + 400, outline=color, fill=color)
    draw2d.draw_oval(canvas, startX + 40, startY + 490, startX + 150, startY + 430, outline=color, fill=color)

#Class birds aleatory in the sky
def draw_bird(canvas, startY, color):
    """Draw a bird in a random location in the sky."""
    startX = random.randrange(0, 800)
    draw2d.draw_arc(canvas, 50 + startX, 450 + startY, 100 + startX, 550 + startY, start=50, extent=70, width=3, outline=color)  
    draw2d.draw_arc(canvas, 75 + startX, 450 + startY, 125 + startX, 550 + startY, start=50, extent=70, width=3, outline=color)

# Call the main function so that this program will start executing.
main()