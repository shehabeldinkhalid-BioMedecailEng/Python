# Mainipulation with Image
from PIL import Image
# OPEN Image
myimage = Image.open(r"D:\SHOUSH\hero of war and peace 3\927.jpg")
print(myimage)  # print data just Mode : RGB
# Show Image
myimage.show()
# crop Image
cutedpart = (0,0,100,150) 
NImage = myimage.crop(cutedpart)
NImage.show()
myimage.close()

# Doc string ====> Documentin
def Function(NAME):
    """ Print HI to the { " agrument " }  """
    print(f"Hi {NAME}")
 # To call the (Doc string) of def function()
help(Function)
print(Function.__doc__) 



