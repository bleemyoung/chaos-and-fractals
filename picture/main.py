import cv2
import numpy as np
from PIL import Image

def logistic(Img, x, u,times):
    M = Img.shape[0]
    N = Img.shape[1]
    for i in range(1, times):
        x = u * x * (1 - x)
    array = np.zeros(M * N)
    array[1] = x
    for i in range(1, M * N - 1):
        array[i + 1] = u * array[i] * (1 - array[i])
    array = np.array(array * 255, dtype='uint8')
    code = np.reshape(array, (M, N))
    xor = Img ^ code
    v = xor
    return v

def transfer(Img_from,Img_to):
    print("图片原始地址"+Img_from)
    print("图片保存地址"+Img_to)
    Img = cv2.imread(Img_from)
    Img = Img[:, :, [2, 1, 0]]
    (r, g, b) = cv2.split(Img)
    R = logistic(r, x, u, times)
    G = logistic(g, x, u, times)
    B = logistic(b, x, u, times)
    merged = np.ones(Img.shape, dtype=np.uint8)
    merged[:, :, 2] = B
    merged[:, :, 1] = G
    merged[:, :, 0] = R
    Img = Image.fromarray(merged)
    Img.save(Img_to)
    
    return

# 0<x<1
x = 0.1
# 3.5699456...<u<=4
u = 4
times = 500

# encryption
print("对图片加密")
transfer('./picture/origin.png','./picture/encryption.png')


# decryption
print("对加密后的图片解密")
transfer('./picture/encryption.png','./picture/decryption.png')


# 摘自https://www.cnblogs.com/hortz/p/16000934.html，有修改