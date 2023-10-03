import cv2
import numpy as np

drawing = False
current_shape = 'Line'
ix, iy = -1, -1

def draw_event(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if current_shape == 'Line':
            cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 2)
        elif current_shape == 'Rectangle':
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        elif current_shape == 'Circle':
            radius = int(((ix-x)**2 + (iy-y)**2)**0.5)
            cv2.circle(img, (ix, iy), radius, (0, 0, 255), 2)
        elif current_shape == 'Ellipse':
            cv2.ellipse(img, (ix, iy), (abs(ix-x)//2, abs(iy-y)//2), 0, 0, 360, (127, 127, 255), 2)

img = np.zeros((600, 800, 3), np.uint8)
cv2.namedWindow('Drawing Board')
cv2.setMouseCallback('Drawing Board', draw_event)

while True:
    cv2.imshow('Drawing Board', img)
    k = cv2.waitKey(1) & 0xFF

    if k == ord('l'):
        current_shape = 'Line'
    elif k == ord('r'):
        current_shape = 'Rectangle'
    elif k == ord('c'):
        current_shape = 'Circle'
    elif k == ord('e'):
        current_shape = 'Ellipse'
    elif k == 27:  # ESC key
        break

cv2.destroyAllWindows()
