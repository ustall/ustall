import cv2
import pytesseract
# import easyocr

pytesseract.pytesseract.tesseract_cmd = 'F:\\max\\Programs2\\moduls\\tesseract\\tesseract.exe'
# es=easyocr.Reader(['en','ru'])


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgTxt(img):
    result = ''
    try:
        img = cv2.imread(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # img = cv2.Canny(img, 150, 150)
            # kernel = np.ones((2,2), np.uint8)
            # img = cv2.dilate(img, kernel,iterations=1)
            # img = cv2.erode(img, kernel,iterations=1)
            # viewImage(img, "fixed")
        config = r'--oem 3 --psm 6'
        result = pytesseract.image_to_string(gray, config=config, lang='eng+rus')+'\n текст полученный при помощи google ' \
                                                                                 'tesseract'
    except:
        result="Текст найти не удалось"
    # result += es.readtext(gray) + '\nТекст получен при помощи easy ocr tesseract\n'
    if len(result)==0:
        result = "Текст найти не удалось"
    return result


if __name__ == "__main__":
     img = cv2.imread("F:/max/Programs2/Myfiles/tgbot2/data/img.jpg")
     print(imgTxt("F:/max/Programs2/Myfiles/tgbot2/data/img.jpg"))
     viewImage(img, "Image")
