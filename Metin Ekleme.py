import cv2
import numpy as np

resim = np.zeros((400,400,3),dtype='uint8')
cv2.rectangle(resim,(10,10),(390,210),(0,255,255))
cv2.line(resim,(10,10),(390,210),(0,0,255),3)#1. noktadan 2 . noktaya çizgi çizer
cv2.line(resim,(10,230),(390,230),(123,55,78),3)
cv2.circle(resim,(200,350),25,(148,0,4),3)#burdada daire çiziyoruz ilki orta kordinatı 2..siyarıçap 3 renk dört kalınlık

cv2.putText(resim,'Erkam Cengiz',(15,315),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,255,255),1,cv2.LINE_4)
#yaazı yazmamızı sağlar kordinat verdiğimizde sol alt kordinat verimiş oluyoruz ona göre
cv2.imshow('siyah',resim)


cv2.waitKey(0)
cv2.destroyAllWindows()