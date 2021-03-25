import cv2 
from pyzbar import pyzbar

img = cv2.imread('dumm1.png')

cv2.imshow("barcode",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

barcodes = pyzbar.decode(img)

for barcode in barcodes:
	x,y,w,h = barcode.rect
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
	bdata = barcode.data.decode("utf-8")
	btype = barcode.type
	text = f'{bdata},{btype}'

	cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)


cv2.imshow("scanned",img)
cv2.waitKey(0)
cv2.destroyAllWindows()