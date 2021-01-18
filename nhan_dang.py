import cv2
import numpy as np
import matplotlib.pyplot as plt
#read img
print("\t\t\tWelcome to ours project: \nBuild a solution that computer can learn and identify numbers and letters by Python")
print("Input your image")
url_img = input()
img =  cv2.imread(url_img,0)
cells=[np.hsplit(row,20) for row in np.vsplit(img, 20)]
nub= []
m = 0
for i in range (0,20):
    for x in range (0,20):
        if (cells[i][x] != 0):
            nub.append([i,x])
            m+=1
nub.sort()
arr_1 = []
array_2 = []
countD = 0
for i in nub:
    if i not in arr_1:
        arr = []
        k = 0
        for j in nub:
            if i[0] == j[0] and i[1]+k == j[1]:
                k+=1
                arr.append(j)
                arr_1.append(j)
        count = 0
        for i in arr:
            count +=1
        if count > 0:
            minn = min(arr)
            dox = minn[0]
            log = count
            up = 0
            down = 0
            left = 0
            right = 0
            if nub[0][0] < minn[0]:
                up+=1
            if nub[0][0] > minn[0]:
                down+=1
            if nub[0][1] > minn[1]:
                left+=1
            if nub[0][1] < minn[1]:
                right+=1
            array_2.append([up,down,left,right,dox,log,0])
            countD += 1

            



#saving 
print("Do you want to test or save your img?")
test_save= input()
if (test_save == 'yes'):
    print("urlsaving")
    url_saving= input()
    
    file = open(url_saving,'w+')
    for i in range(0,countD):
        file.write(str(array_2[i]))
        file.write('\n')
    file.close()
    print("saving secced")
    

#read
if(test_save == 'test'):
    def read(url,array,sln):
        kk = np.genfromtxt(url,delimiter=',', dtype = int)
        cound = 0
        for i in kk:
            cound+=1
        for i in range(0,cound):
            array.append([int(-kk[i][0]),int(kk[i][1]),int(kk[i][2]),int(kk[i][3]),int(kk[i][4]),int(kk[i][5])])
            sln.append(int(-kk[i][6]))
# sln là mảng chứa trọng số của từng điểm

    nub_1 = []
    sln_1 = []
    read('nub_1.txt',nub_1,sln_1)   
    nub_2 = []
    sln_2 = []
    read('nub_2.txt',nub_2,sln_2)
    nub_3 = []
    sln_3 = []
    read('nub_3.txt',nub_3,sln_3)
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in nub_1:
        count_1+=1
    for i in nub_2:
        count_2+=1
    for i in nub_3:
        count_3+=1
    #knn
    def knnf(a,b,c,d,e,f):
        trainData = np.array(data, dtype='float32')
        ketqua = np.array(kq, dtype='float32')               
        k=[[a,b,c,d,e,f]]                 
        newMember = np.array(k,dtype='float32')

        knn = cv2.ml.KNearest_create()
        knn.train(trainData, 0, ketqua)
        temp, result, nearest, distance = knn.findNearest(newMember, 1)
        global ioo
        ioo = result
    #test
    #những biến với mảng này là để lưu mảng với trọng số mới sau khi nhận dạng giá trị thay đổi là cái trọng số thôiu
    
    nb3 = 0
    nb1 = 0
    nb2 = 0
    nub_11 = []
    nub_22 = []
    nub_33 = []
    for i in range(0,12):
        global data
        global kq
        data=[]
        kq = []
        if count_1<=i:
            data.append(nub_1[count_1])
            kq.append(1)
        if count_1 > i:
            data.append(nub_1[i])
            kq.append(1)
        if count_2 <= i:
            data.append(nub_2[count_2])
            kq.append(2)
        if count_2 > i:
            data.append(nub_2[i])
            kq.append(2)
        if count_3 <= i:
            data.append(nub_3[count_3-1])
            kq.append(3)
        if count_3 > i:
            data.append(nub_3[i])
            kq.append(3)
        knnf(array_2[i][1],array_2[i][2],array_2[i][3],array_2[i][4],array_2[i][5],array_2[i][6])
        if(ioo==[[1.]]):
            nb1+=1
            sln_11 = sln_1[i]+1
            nub_11.append([nub_1[i][0],nub_1[i][1],nub_1[i][2],nub_1[i][3],nub_1[i][4],nub_1[i][5],sln_11])
            nub_22.append([nub_2[i][0],nub_2[i][1],nub_2[i][2],nub_2[i][3],nub_2[i][4],nub_2[i][5],sln_2[i]])
            nub_33.append([nub_3[i][0],nub_3[i][1],nub_3[i][2],nub_3[i][3],nub_3[i][4],nub_3[i][5],sln_3[i]])
        if(ioo==[[2.]]):
            nb2+=1
            sln_22 = sln_2[i]+1
            nub_22.append([nub_2[i][0],nub_2[i][1],nub_2[i][2],nub_2[i][3],nub_2[i][4],nub_2[i][5],sln_22])
            nub_11.append([nub_1[i][0],nub_1[i][1],nub_1[i][2],nub_1[i][3],nub_1[i][4],nub_1[i][5],sln_1[i]])
            nub_33.append([nub_3[i][0],nub_3[i][1],nub_3[i][2],nub_3[i][3],nub_3[i][4],nub_3[i][5],sln_3[i]])
        if(ioo == [[3.]]):
            nb3+=1
            sln_33 = sln_3[i]+1
            nub_33.append([nub_3[i][0],nub_3[i][1],nub_3[i][2],nub_3[i][3],nub_3[i][4],nub_3[i][5],sln_33])       
            nub_11.append([nub_1[i][0],nub_1[i][1],nub_1[i][2],nub_1[i][3],nub_1[i][4],nub_1[i][5],sln_1[i]])
            nub_22.append([nub_2[i][0],nub_2[i][1],nub_2[i][2],nub_2[i][3],nub_2[i][4],nub_2[i][5],sln_2[i]])

            
# lưu các file đã thay đổi trọng số 
    file1 = open('nub_1.txt','w+')
    for i in range(0,12):
        file1.write(str(nub_11[i]))
        file1.write('\n')
    file1.close()
    file2 = open('nub_2.txt','w+')
    for i in range(0,12):
        file2.write(str(nub_22[i]))
        file2.write('\n')
    file2.close()
    file3 = open('nub_3.txt','w+')
    for i in range(0,12):
        file3.write(str(nub_33[i]))
        file3.write('\n')
    file3.close()
  
#main control
    MAX = max(nb1,nb2,nb3)
    if MAX == nb1:
        print("Đó là số 4")
    elif MAX == nb2:
        print("Đó là số 3")    
    elif MAX == nb3:
        print("Đó là số 7")
    else:
        print("Loading...")
    print(nb1,nb2,nb3)
