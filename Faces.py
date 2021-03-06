import cv2

fc=cv2.CascadeClassifier('frontalface.xml')
img=cv2.imread('One.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=fc.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=2,minSize=(30,30))

print('Found ',len(faces),' faces')

for x,y,a,b in faces:
    cv2.rectangle(img,(x,y),(x+a,y+b),(0,0,255),2)
cv2.imshow('Faces',img)
