import cv2
from object_finder import CarFinder, BallFinder

# author: Hendrik Werner s4549775

capture_path = "../capture.png"

image = cv2.imread(capture_path)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
imageHSV = cv2.medianBlur(imageHSV, 3)

finder = BallFinder(imageHSV, [[15, 128, 50]], [[25, 255, 255]])
finder.find_ball()

finder = CarFinder(imageHSV, [[90, 128, 10]], [[120, 255, 255]])
finder.find_car()

finder = CarFinder(
    imageHSV,
    [[170, 128, 50], [0, 128, 50]],
    [[180, 255, 255], [10, 255, 255]],
)
finder.find_car()
