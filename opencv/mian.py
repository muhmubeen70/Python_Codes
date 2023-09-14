import os
import cv2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelBinarizer
from keras.utils import to_categorical
from keras.layers import AveragePooling2D, Dropout, Flatten, Dense, Input
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.models import Model
from keras.optimizers import Adam
import numpy as np
# from imutils import path
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

#initialize the initial learning rate, number of epochs to train for and batch size

initial_learning_rate = 1e-4
EPOCHS = 20
bs = 32

Directory = r"C:\Users\Muhammad Mubeen\Desktop\opencv\Face Mask Dataset\Train"
CATEGORIES = ["WithMask", "WithoutMask"]

# grab the list of images in our dataset director, then initialize the list of data i.e images and class images
print("[INFO] Loading Image")

data = []
labels = []

for category in CATEGORIES:
    path = os.path.join(Directory, category)
    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        image = load_img(img_path, target_size=(224, 224))
        image = img_to_array(image)
        image = preprocess_input(image)
        data.append(image)
        labels.append(category)
print(category)


lb = LabelBinarizer()
labels = lb.fit_transform(labels)
labels = to_categorical(labels)

data = np.array(data, dtype="float32")
labels = np.array(labels)


(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.20, stratify=labels, random_state=42)

#contruct the training inage generator for data augmentation
aug = ImageDataGenerator(
    rotation_range = 20,
    zoom_range = 0.15,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.15,
    horizontal_flip = True,
    fill_mode = 'nearest'
)

#load the mobilenetV2 network, ensuring the head FC layers sets are keft off

baseModel = MobileNetV2(weights='imagenet', include_top=False, input_tensor=Input(shape=(224, 224, 3)))


#contruct the head of the model that will be placed on the top of the model
headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(2, 2))(headModel)
headModel = Flatten(name='flatten')(headModel)
headModel = Dense(120, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(2, activation="softmax")(headModel)

#place the head fc model on top of the base model (this will become the actual model we will train
model = Model(inputs=baseModel.input, outputs=headModel)

#loop over all the layers in the base model and freeze them so they will not be updated during the first training process
for layer in baseModel.layers:
    layer.trainable = False

#compile our model
print("[Info] compiling model...")
opt = Adam(learning_rate= initial_learning_rate, weight_decay=initial_learning_rate / EPOCHS)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])


#train the head of the network
print('[INFO] training head ')
h = model.fit(
    aug.flow(trainX, trainY, batch_size=bs),
    steps_per_epoch=len(trainX) // bs,
    validation_data=(testX, testY),
    validation_steps=len(testX) // bs,
    epochs=EPOCHS
)

#make predictions on the testing set
print('[INFO] evaluating network')
prediction = model.predict(testX, batch_size=bs)

#for each image in the testing set we need to find the index of the label with corresponding largest predicted probability
prediction = np.argmax(prediction, axis=1)

#show a nice formatted classification report
print(classification_report(testY.argmax(axis=1), prediction, target_names=lb.classes_))

#serialize the model to disk
print("Info saving mask detector model.....")
model.save('mask_detector.model', save_format='h5')


N = EPOCHS
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, N), h.history['loss'], label='train_loss' )
plt.plot(np.arange(0, N), h.history['val_loss'], label='val_loss' )
plt.plot(np.arange(0, N), h.history['accracy'], label='train_acc' )
plt.plot(np.arange(0, N), h.history['val_accracy'], label='val_acc' )
plt.title('Training Loss and Accuracy')
plt.xlabel('#Epoch #')
plt.ylabel('Loss/Accuracy')
plt.legend(loc="Lower Left")
plt.savefig("plot.png")

