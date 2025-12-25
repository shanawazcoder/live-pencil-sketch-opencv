import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("Pencil Sketch Effect")
sketch_mode = False

def create_pencil_sketch(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    inverted = 255 - gray
    
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    
    inverted_blurred = 255 - blurred
    
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    
    
    if sketch_mode:
        display_frame = create_pencil_sketch(frame)
        mode_text = "Sketch Mode (Press 's' to switch)"
    else:
        display_frame = frame
        mode_text = "Normal Mode (Press 's' to switch)"
    
    cv2.putText(display_frame, mode_text, (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(display_frame, "Press 'q' to quit", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    cv2.imshow("Pencil Sketch Effect", display_frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        sketch_mode = not sketch_mode
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
