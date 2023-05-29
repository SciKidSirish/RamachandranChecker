# Data
import pymol



Input = pymol.querying.phi_psi("all")
#print(Input)
dataListIntermediate = list(Input)
dataList = []

for i in range(0, len(dataListIntermediate)):
  dataList.append(Input[dataListIntermediate[i]])


def phipsi(n):
  s = n.find("(")
  p = n[s:]
  p = p.strip("()")
  p = p.strip()
  l = p.split(",")
  for i in range(0, len(l)):
    l[i] = l[i].strip()
    l[i] = float(l[i])

  return l
# phi_psi("SER-95:   (  -55.7,  128.8 )")

#@title
phi = []
psi = []
phi2 = []
psi2 = []
overallList = []
for i in range(0, len(dataList)):
  cList = dataList[i]
#  print(cList)
  overallList.append(cList)
  phi.append(cList[0])
  psi.append(cList[1])


# for i in range(0, 10):
#   cList = phipsi(dataList[i])
#   overallList.append(cList)
#   phi.append(cList[0])
#   psi.append(cList[1])

# sorted(overallList, key=operator.itemgetter(0))





#@title
import matplotlib.pyplot as plt
import numpy as np

x = np.array(phi)
y = np.array(psi)

plt.xlim(-180, 180)
plt.ylim(-180, 180)

plt.scatter(x, y, alpha=0.3)

plt.savefig('plot.png', dpi=300, bbox_inches='tight')
print("plot saved")
plt.show()
print("plot shown")





#@title

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("/Users/siri-nivimac/Downloads/converted_keras/keras_model.h5", compile=False)

# Load the labels
class_names = open("/Users/siri-nivimac/Downloads/converted_keras/labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open("plot.png").convert("RGB")
print("opening image")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
# image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
image = ImageOps.fit(image, size)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
# print("Class:", class_name[2:], end="")
# print("Confidence Score:", confidence_score)
if confidence_score > 0.6:
  print("The structure is {} with a confidence of {}%.".format(class_name[2:].lower(),round(confidence_score*100, 2)))
else:
  print("NOTE: These results are a bit unsure.")
  print("The structure is {} with a confidence of {}%.".format(class_name[2:].lower(),round(confidence_score*100, 2)))
