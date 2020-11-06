import cv2
img = cv2.imread(r'D:\cvtest\wuhu.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier(r'D:\cvtest\haarcascade_frontalface_default.xml')
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=15)
eye_cascade=cv2.CascadeClassifier(r'D:\cvtest\xml\xml\haarcascade_eye.xml')
eyes=eye_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=15)
eye_glass_cascade=cv2.CascadeClassifier(r'D:\cvtest\xml\xml\haarcascade_eye_tree_eyeglasses.xml')
eyes_glass=eye_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=15)
for (x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
for (x,y,w,h) in eyes:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# for (x,y,w,h) in eyes_glass:
#     img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
resized=cv2.resize(img,(512,800))
cv2.imshow('wow',resized)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyWindow('wow')
if k==115:
    cv2.imwrite(r'D:\cvtest\wuhu_hhh.jpg',img)
    cv2.destroyWindow('wow')