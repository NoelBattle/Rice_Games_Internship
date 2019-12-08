
import os
import sys
from PIL import Image, ImageDraw
import numpy as np
import face_recognition

#opens the directory  
os.getcwd()
currentDirectory = os.getcwd()
path = "images"
dirs = os.listdir(path)
print(dirs)
# Given an image, return the 128-dimension face encoding for each face in the image.
person1 = face_recognition.load_image_file("images/person1.jpg")
person2 = face_recognition.load_image_file("images/person2.jpg")
person3 = face_recognition.load_image_file("images/person3.jpg")
image = face_recognition.load_image_file("images/friends.jpg")

#enocdes all faces in the emiage
array = face_recognition.face_encodings(image)

#encodes the first face in the image
person1encode = face_recognition.face_encodings(person1)[0]
person2encode = face_recognition.face_encodings(person2)[0]
person3encode = face_recognition.face_encodings(person3)[0]

#makes a list of the encoded faces
encodeList = [person1encode, person2encode, person3encode]

#saves the locations of all the faces in 'image' into the list location. 
locations = face_recognition.face_locations(image)
count = len(locations)
#makes a copy of the image
image_copy = Image.open("images/friends.jpg")
 
# Draw Box Code
draw2 = ImageDraw.Draw(image_copy)
for locatio in locations:
    top, right, bottom, left = locatio
    draw2.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0))
    
# Remove the drawing library from memory as per the Pillow docs
del(draw2)
#Shows the draw box
image_copy.show()

#list of known faces
listknown = face_recognition.face_encodings(image, known_face_locations=locations, num_jitters=1)

#Prints out who is in the pitcture and how many people are in the picture
for i in encodeList:
    #If result is true then the face encodings on the pictures match
    results = face_recognition.compare_faces(listknown, i, tolerance=0.8)
    if results[0] == True:
        if (person1encode == i).any():
            print("clay is in this pic")
        if (person2encode == i).any():
            print("noel is in this pic")
        if (person3encode == i).any():
            print("hugh is in this pic")
    if results[0] == False:
            print("Unknown face")
if count > 0:
    print(f'There are {len(locations)} people in this image')
else:
    print("no faces were found")
       

