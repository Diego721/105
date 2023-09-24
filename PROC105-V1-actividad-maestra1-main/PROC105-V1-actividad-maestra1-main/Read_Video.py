import cv2
#usar 0 para la camara web

#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened() == False):
    print("No se puede leer la entrada")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out= cv2.VideoWriter("Boxing.mp4", cv2.VideoWritter_fourcc(*"DIVX"), 30, (width, height))

while(True):
    #Captura del video
    ret, frame = vid.read()
    cv2.imshow("camara web", frame)
    out.write(frame)
    if cv2.waitKey(25) == 32:
        break
vid.release()
out.release()
#Cierra todos los fotogramas
cv2.destroyAllWindows()