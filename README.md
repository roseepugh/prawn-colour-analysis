PRAWN COLOUR ANALYSIS

Rose Pugh - rp804@exeter.ac.uk

An attempt to code a python script which analyses the colour of a chameleon prawn (Hippolyte varians) from an image. Created for the South-West Biosciences Doctoral Training Partnership's Data Science and Machine Learning Module.


How To Use:
1) Download both of the python scripts to your working directory.
2) Either
   a) download the prawns.zip file and extract this inside a folder named "data" inside your working directory, such that the photos are in ./data/prawns . If your folder structure is different, you can change line 11 of prawncolour.py to ensure that the script can find your photos. Or
   b) move your own photos of chameleon prawns to a folder called "prawns" inside a folder called "data" in your working directory such that the photos are in ./data/prawns . If your folder structure is different, you can change line 11 of prawncolour.py to ensure that the script can find your photos. Either name your photos hipvar[number] or change line 11 of prawncolour.py to reflect your naming convention
3) Ensure all photos are the same filetype, and line 11 of prawncolour.py reflects this. If not, convert your photos and edit line 11 of prawncolour.py to match your chosen filetype (png reccomended)
4) Run datascience_assignment.py to analyse your photos.
