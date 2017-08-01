'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'lj.jpg')
student_original = PIL.Image.open(student_file)
student_img = PIL.Image.open(student_file)
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)

earth_small = earth_img.resize((100, 100)) #eye width and height measured in plt
# Paste earth into right eye and display
# Uses alpha from mask
plt.axis('off')
student_earth = student_img.paste(earth_small, (20,12), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1,3)

axes3[0].imshow(student_original, interpolation='none')
axes3[0].set_yticklabels([])
axes3[0].set_xticklabels([])
axes3[0].set_yticks([])
axes3[0].set_xticks([])
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_yticklabels([])
axes3[1].set_xticklabels([])
axes3[1].set_yticks([])
axes3[1].set_xticks([])
axes3[2].imshow(student_img, interpolation='none')
plt.axis('off')
axes3[2].set_ylim(150, 0)
axes3[2].set_xlim(0, 150)

fig3.show()
