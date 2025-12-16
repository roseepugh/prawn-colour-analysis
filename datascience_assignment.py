#imports necessary modules
import prawncolour
import os

#finds number of photos for analysis
foldermax = len(os.listdir("./data/photos"))
folder = 1

#identifies colour of prawn in each image
while folder <= foldermax:
    prawncolour.prawncolour(folder)
    folder = folder + 1