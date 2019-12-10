from commonfunctions import *
from scipy import ndimage


def findLetterContourArea(img):
    # This function finds the contours of a given image and returns it in the variable contours.
    # This function will not work correctly unless you preprocess the image properly as indicated.
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 #   ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
    #SE=np.ones((3,3))
    #img=Opening(img, SE)
    #show_images([img])
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    #print(contours[0])
    framearea = cv2.contourArea(contours[0])
    # TODO: Find the contour area of the given image (img) (~1 line)
    maxArea = 0
    index = 0
    for i in range(1, len(contours)):
        if (cv2.contourArea(contours[i]) > maxArea):
            maxArea = cv2.contourArea(contours[i])
            index = i
    # area = cv2.contourArea(contours[1])
    return maxArea, contours[index], framearea


def Count_connected_parts(img):  # this function returns the number of connected parts given the binary image of any letter
    labeled, nr_objects = ndimage.label(img < 1)  # 100 is the threshold but in case of binary image given (0,1) it will change
    # print(nr_objects)
    # print("Number of objects is {}".format(nr_objects))
    return nr_objects


def count_holes(img, num_connected_parts):  # count number of holes in each character
   # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = np.copy(img)
    #kernel = np.ones((3,3),np.float32)/9
   # dst = cv2.filter2D(gray,-1,kernel)
   # print(img)
   # ret,thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # print("y= ",len(contours)-1-num_connected_parts)
    return len(contours) - 1 - num_connected_parts  # -1 is the contour of the image frame


def Height_Width_Ratio(img):
    area, letter_contour, framearea = findLetterContourArea(img)
    whiteArea = framearea - area
    x, y, w, h = cv2.boundingRect(letter_contour)
    # print(x)
    # print(y)
    # print(h)
    # print(w)
    return h / w,  # area/whiteArea


def Max_transition_rows(img):
    #  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #  ret, img = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    MaxTransition = 0
    # MaxTransitionIndex = Base_INDEX
    for i in range(img.shape[0]):  # loop on Each row
        CurrTransitionRow = 0
        flag = 1
        for j in range(img.shape[1]):  # loop on coloumns for specific row
            if flag == 1 and img[i, j] == 0:
                flag = 0
                CurrTransitionRow += 1
            elif flag == 0 and img[i, j] == 1:
                flag = 1
                CurrTransitionRow += 1

        if CurrTransitionRow >= MaxTransition:
            # MaxTransitionIndex = i
            MaxTransition = CurrTransitionRow
    return MaxTransition


def Max_transition_colomns(img):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, img = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    MaxTransition = 0
    # MaxTransitionIndex = Base_INDEX
    for i in range(img.shape[1]):  # loop on each coloumn
        CurrTransitionCol = 0
        flag = 1
        for j in range(img.shape[0]):  # loop on rows for specific coloumn
            if flag == 1 and img[j, i] == 0:
                flag = 0
                CurrTransitionCol += 1
            elif flag == 0 and img[j, i] == 1:
                flag = 1
                CurrTransitionCol += 1

        if CurrTransitionCol >= MaxTransition:
            # MaxTransitionIndex = i
            MaxTransition = CurrTransitionCol
    return MaxTransition


def Extracting_features(img):
    num_parts = Count_connected_parts(img)
    holes = count_holes(img, num_parts)
    h_W = Height_Width_Ratio(img)
    vertical_trans = Max_transition_colomns(img)
    horizontal_trans = Max_transition_rows(img)
    return [num_parts, holes, h_W, vertical_trans, horizontal_trans]

# img=io.imread("test character letters/heh.png")
# h_w,r=Height_Width_Ratio(image)
# show_images([img])
# print (img)

# print (img)
# x = Max_transition_rows(img)
# y = Max_transition_colomns(img)

# print(x)
# print(y)
