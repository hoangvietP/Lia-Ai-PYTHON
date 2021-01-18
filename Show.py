import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


# ham test tra ve cac diem tao thanh cua 1 so 3
def test():
    #hàm read lấy dữ liệu từ file
    def read(url,array,sln):
        kk = np.genfromtxt(url,delimiter=',', dtype = int)
        cound = 0
        for i in kk:
            cound+=1
        for i in range(0,cound):
            array.append([int(-kk[i][0]),int(kk[i][1]),int(kk[i][2]),int(kk[i][3]),int(kk[i][4]),int(kk[i][5])])
            sln.append(int(-kk[i][6]))   
    nub_2 = []
    sln_2 = []
    read('nub_2.txt',nub_2,sln_2)
    nub_3 = []
    sln_3 = []
    read('nub_3.txt',nub_3,sln_3)
    count_2 = 0
    count_3 = 0
    #đếm các phần tử trong file và nạp các điểm có trọng số lớn nhất vào 1 mảng
    new = []
    dnew = []
    for i in nub_2:
        count_2+=1
    for i in nub_3:
        count_3+=1
    for i in range(0,count_2):
        maxx= max(sln_2[i],sln_3[i])
        if(sln_2[i] == maxx):
            new.append(nub_2[i])        
        if(sln_3[i] == maxx):
            new.append(nub_3[i])
    d = [10,10]# điểm ban đầu có thể để random
    #từ điều kiện của dữ liệu lấy ra từ file tính toán đưa ra tọa độ điểm tương ứng
    for i in range (0,count_2):
        a= 10
        b = 10
        # điểm tiếp theo nằm bên phải và bên trên
        if(new[i][0] == 1 and new[i][2]== 1):
            a+= new[i][4]
            b+= new[i][5]
        # điểm tiếp theo nằm bên phải và ngang bằng(chung oy)
        if(new[i][0] == 1 and new[i][2]== 0 and new[i][1] == 0 and new[i][3]== 0):
            a+= new[i][4]
        #điểm tiếp theo nằm bên phải và bên dưới
        if(new[i][0] == 1 and new[i][3]== 1):
            a+= new[i][4]
            b-= new[i][5]
        #điểm tiếp theo nằm bên trái và bên trên
        if(new[i][1] == 1 and new[i][2]== 1):
            a+= new[i][4]
            b+= new[i][5]
        # điểm tiếp theo nằm bên trái chung oy
        if(new[i][1] == 1 and new[i][2]== 0 and new[i][0] == 0 and new[i][2]== 0):
            a-= new[i][5]
        # điểm tiếp theo bên trái và bên dưới
        if(new[i][1] == 1 and new[i][3]== 1):
            a-= new[i][4]
            b+= new[i][5]
        # điểm tiếp theo nằm bên trên chung ox
        if(new[i][1] == 0 and new[i][2]== 1 and new[i][0] == 0 and new[i][3]== 0):
            b+= new[i][5]
        # điểm tiếp theo nằm bên dưới chung ox
        if(new[i][1] == 0 and new[i][2]== 0 and new[i][0] == 0 and new[i][3]== 1):
            b-= new[i][5]
        dnew.append([a,b])
    print("Show các điểm đặc trưng: ")
    print(dnew)

test()


















