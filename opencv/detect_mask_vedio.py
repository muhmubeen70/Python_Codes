import cv2
import numpy as np
import tensorflow as tf
import imutils




def detect_and_predict_mask(frame, face_net, mask_net):
    # grab the dimension of the frame and then construct a blob from it
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224), (104.0, 117.0, 123.0))
    face_net.setInput(blob)
    detection = face_net.forward()
    print(detection.shape)

    # initialize the list of faces, their corresponding locations, and the list of predictions from our face mask
    # network
    faces = []
    location = []
    prediction = []

    # loop over through detections
    for i in range(0, detection.shape[2]):

        confidence = detection[0, 0, i, 2]
        # filter out the weak detections by ensuring the confidence is greater than the minimum confidence
        if confidence > 0.5:
            # compute the x,y -coordinates of the bounding box for the object
            box = detection[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_X, start_Y, end_X, end_Y) = box.astype('int')

            # ensure the bounding boxes fall within the dimensions of the frame
            (start_X, start_Y) = (max(0, start_X), max(0, start_Y))
            (end_X, end_Y) = (min(w - 1, end_X), min(w - 1, end_Y))

            # extract the ROI, convert it from BGR to RGB channel ordering, resize it to 224x224 and preprocess it
            face = frame[start_Y:end_Y, start_X:end_X]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = tf.keras.preprocessing.image.img_to_array(face)
            face = tf.keras.applications.mobilenet_v2.preprocess_input(face)

            # add the face and bounding boxes to their respective lists
            faces.append(face)
            location.append((start_X, start_Y, end_X, end_Y))

    # only make prediction when at least one face is detected
    if len(faces) > 0:
        faces = np.array(faces, dtype="float32")
        prediction = mask_net.predict(faces, batch_size=20)
    return location, prediction


# load our serialized  face detector model from the disk
proto_txt_path = r'face_detector\deploy.prototxt'
weighs_path = r'face_detector\res10_300x300_ssd_iter_140000.caffemodel'
face_net = cv2.dnn.readNet(proto_txt_path, weighs_path)

# load the face mask detector model from the desk
mask_net = tf.keras.models.load_model('mask_detector.model')

# initialize the video stream
print('[Info] starting video stream')
video_stream = cv2.VideoCapture(0)

# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize to have a maximum width of 400 px
    grabbed, frame = video_stream.read()
    if not grabbed:
        break
    frame = imutils.resize(frame, width=600)
    (locations, predictions) = detect_and_predict_mask(frame, face_net, mask_net)

    for (box, predictions) in zip(locations, predictions):
        # unpack the bounding box and predictions
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = predictions

        # determine the class label and colour we will use to draw the bounding box and text
        label = 'Mask' if mask > withoutMask else 'No Mask'
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        # include the probability in the label
        label = '{}: {:.2f}'.format(label, max(mask, withoutMask) * 100)

        # display the label and bounding box rectangle on the output frame
        cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    # if the q key was pressed break from the loop

    if key == ord('q'):
        break

# do a bit of cleanup
video_stream.release()
cv2.destroyWindow("Frame")
