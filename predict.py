import numpy as np
import utils
import cv2
from tensorflow.keras import backend as K
from model.AlexNet import AlexNet



K.image_data_format() == 'channels_first'

if __name__ == "__main__":
    model = AlexNet()
    model.load_weights("D:\BaiduNetdiskDownload\【讲座 】 最落地的图像识别实践案例\代码\AlexNet-Keras-master\logs\last1.h5")
    img = cv2.imread("1.jpg")
    img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_nor = img_RGB/255
    img_nor = np.expand_dims(img_nor,axis = 0)
    img_resize = utils.resize_image(img_nor,(224,224))
    #utils.print_answer(np.argmax(model.predict(img)))
    print(utils.print_answer(np.argmax(model.predict(img_resize))))
    cv2.imshow("ooo",img)
    cv2.waitKey(0)