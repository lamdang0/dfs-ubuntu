from collections import defaultdict 
from random import *
colU = []
colV = []
colT = []
import time
import threading
from multiprocessing import Process
import sys
import os
sys.setrecursionlimit(3000)

# Multi threading
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        time.sleep(.01)
        # Get lock to synchronize threads
        threadLock.acquire()
        #Run 4 threads
        print ("Starting " + self.name)
        if '1' in self.name:
            g.randomN(colU,s)
        if '2' in self.name:
            g.randomN(colV,d)
        if '3' in self.name:
            g.randomK(colU,colV)
        if '4' in self.name:
            g.randomK(colV,colU)
        # Free lock to release next thread
        threadLock.release()
        
#main graph
class Graph: 
    pathTotal = 0 #bien dem so luong path
    def __init__(self,nodes):        
        self.N= nodes  
        self.graph = defaultdict(list)       
    # them ket noi
    def addEdge(self,u,v): 
        self.graph[u].append(v)
    #visited[]:l
    #path[]: l
        
    def printAllPathsUtil(self, u, d, visited, path): 
        #   
        visited[u]= True
        path.append(u)
        #In 
        if u == d: 
            print (path)
            Graph.pathTotal+=1
        else: 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i,d,visited,path) 
        # Tra ve vi tri hien tai va bo danh dau visited
        path.pop()
        visited[u] = False
    #
    def printAllPaths(self,s,d):
        # danh dau node
        visited =[False]*(self.N)
        path = []
        # goi ham in
        self.printAllPathsUtil(s,d,visited,path)

    def randomK(self,arr1,arr2): ##random ket noi giua 2 cot
        print("")
        for i in arr1:
            mang1=[3.14]  ##array luu node random
            no=randint(1,len(arr2))  
            print "So ket noi random tu node",i,":",no  #random node
            for j in range(0,no):
                temp = randint(arr2[0],arr2[len(arr2)-1])
                while temp in mang1:  
                    temp = randint(arr2[0],arr2[len(arr2)-1]) ##
                else:
                    mang1.append(temp)
                g.addEdge(i,temp)    ##them ket noi
                print i,"-->",temp

    def randomN(self,arr1,k):  ##random ket noi tu/den node 0/1
        no=randint(1,len(arr1))
        print "\nSo ket noi random tu/den node",k," :",no
        mang2 = [3.14]   ## array luu node random
        for j in range(0,no):
            temp = randint(arr1[0],arr1[len(arr1)-1])
            while temp in mang2:
                temp = randint(arr1[0],arr1[len(arr1)-1]) #ki
            else:
                mang2.append(temp)
            if (k == 0):           ##ket noi tu node 0 -> colU
                g.addEdge(k,temp)
                print k,"-->",temp
            if (k == 1):
                g.addEdge(temp,k) ##ket noi tu colV -> node 1
                print temp,"-->",k

#Input node
#n = int(input("Nhap so nodes: "))

u1 = int(input("So node cot U: "))
v1 = int(input("So node cot V: "))
temp = u1+v1+2
g = Graph(temp)
#setup column
for p in range(2,u1+2):
    colU.append(p)
p+=1
for q in range(0,v1):
    colV.append(p)
    p+=1
print(colU)
print(colV)
s = 0
d = 1

#Bat dau tinh thoi gian them ket noi
start1 = time.time()
print("")
#target =  open('result.txt', 'a')

##Threading
threadLock = threading.Lock()
threads = []
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
for t in threads:
    t.join()

end1 = time.time()
elapsed1 = end1 - start1
print "\nThoi gian random ket noi: ", str(round(elapsed1,2)),"s"
#target.write("\nSo node = " + str(u1) +"\nThoi gian random ket noi: " + str(round(elapsed1,2)) +"s")

#Tinh thoi gian tim path
start2 = time.time()
g.printAllPaths(s,d)  #In path
print "Tong so path tu S-->D: ",Graph.pathTotal #Tinh tong so path tim duoc
#target.write("\nTong so path tu S(0)->D(1): " + str(Graph.pathTotal) )
end2 = time.time()
elapsed2 = end2 - start2
#target.write("\nThoi gian tim path: " + str(round(elapsed2,2)) +"s\n")

#ghi file
target =  open('result.txt', 'a')
target.write("\nSo node = " + str(u1) +"\nThoi gian random ket noi: " + str(round(elapsed1,2)) +"s")
target.write("\nTong so path tu S(0)->D(1): " + str(Graph.pathTotal) )
target.write("\nThoi gian tim path: " + str(round(elapsed2,2)) +"s\n")
target.close()

input("Done !")




        
                    
