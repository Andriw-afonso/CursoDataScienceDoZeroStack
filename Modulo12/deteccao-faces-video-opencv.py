import cv2
from cv2 import CascadeClassifier
from cv2 import rectangle,circle
from cv2 import imshow,waitKey,destroyAllWindows,VideoCapture

# Captura o video da camera
cap = VideoCapture(2)
 
# verifique se a captura esta aberta.
if (cap.isOpened() == False): 
  print("Nao foi possivel ler os dados da camera")

# carregando o modelo pre-treinado
classifier = CascadeClassifier('modelos/haarcascade_frontalface_default.xml')

# inicializa o loop para a leitura de frames
while(True):
  ret, frame = cap.read() 
  
  # se a leitura tiver sendo feita
  if ret == True: 
    # executa o detector de faces
    bboxes = classifier.detectMultiScale(frame)
    
    # extrai as bounding box
    if(len(bboxes)>0):
        for box in bboxes:
            x, y, width, height = box
            x2, y2 = x + width, y + height
            # desenhando o retangulo no frame
            rectangle(frame, (x, y), (x2, y2), (0,0,255), 3)


    # Exibe o frame processado    
    imshow('detecao de faces',frame)
 
    # se pressionar q para a captura e libera a camera
    if waitKey(1) & 0xFF == ord('q'):
      break
 
  else:
    break 
 
# libera o video
cap.release()
 
# fecha a janela da imagem
destroyAllWindows() 