from PIL import Image

#RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

#Import image.
my_image = Image.open("profile_picture.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

for pixel in image_list:
	sum_pixel = pixel[0] + pixel[1] + pixel[2]
	if sum_pixel < 182:
		recolored.append(darkBlue)
	elif sum_pixel >= 182 and sum_pixel < 364:
		recolored.append(red)
	elif sum_pixel >= 364 and sum_pixel< 546:
		recolored.append(lightBlue)
	else:
		recolored.append(yellow)
#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.


# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored2.jpg", "jpeg") #save the new image as "recolored.jpg"
