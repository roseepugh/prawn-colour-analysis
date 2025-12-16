PRAWN COLOUR ANALYSIS

Rose Pugh - rp804@exeter.ac.uk

An attempt to code a python script which analyses the colour of a chameleon prawn (Hippolyte varians) from an image. Created for the South-West Biosciences Doctoral Training Partnership's Data Science and Machine Learning Module.


Required Modules:
- PIL
- numpy
- skimage
- matplotlib
- os
- pandas


How To Use:
1) Download both of the python scripts to your working directory.
2) Ensure required modules are installed
3) Either
   a) download the prawns.zip file and extract this inside a folder named "data" inside your working directory, such that the photos are in ./data/prawns . If your folder structure is different, you can change line 20 of prawncolour.py to ensure that the script can find your photos. Or
   b) move your own photos of chameleon prawns to a folder called "prawns" inside a folder called "data" in your working directory such that the photos are in ./data/prawns . If your folder structure is different, you can change line 20 of prawncolour.py to ensure that the script can find your photos. Either name your photos hipvar[number] or change line 11 of prawncolour.py to reflect your naming convention
4) Ensure all photos are the same filetype, and line 20 of prawncolour.py reflects this. If not, convert your photos and edit line 20 of prawncolour.py to match your chosen filetype (png reccomended)
5) Run datascience_assignment.py to analyse your photos.
6) The code will go through your photos one at a time, with messages, tables, and graphs showing the progress, which can help with identifying where the process went wrong if the colour is incorrectly identified.


Credits for the photos in the example dataset:
Bay-Nouailhat, W., n.d. Chameleon Prawn. Photograph. (hipvar7.png);
Chameleon prawns - Devon, 2018. (hipvar6.png);
Green, S., 2019. My Exeter PhD: Camouflage helps brightly coloured chameleon prawns to survive in the rock pools. Exeter Marine. (hipvar5.png, hipvar11.png, hipvar12.png, hipvar13.png, hipvar14.png);
Green, S., Duarte, R., Kellett, E., Alagaratnam, N., and Stevens, M., 2019. Colour change and behavioural choice facilitate chameleon prawn camouflage against different seaweed backgrounds. Communications Biology, 2. (hipvar1.png, hipvar2.png, hipvar4.png, hipvar8.png, hipvar9.png, hipvar10.png);
Oakley, J., n.d. Green Hippolyte varians in a sandy rockpool. Photograph. (hipvar3.png);
