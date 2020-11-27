import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import os

#path : file path and its name
#num : how many kinds of data you need to read
def readfile(path,num):
    counters=1
    data=[[] for i in range (0,num)]

    #read the file
    f = open(path,'r') 
    for line in f.readlines():
        counters+=1
        line=line.strip('\n')
        if "," in line:
            doc=line.split(',')
            for i in range (0,num):
                data[i]+=[doc[i]]
    f.close()

    x=list(range(1,counters))
    return (x,data)

def draw(x_data,y_data,x_name,y_name,y_range=100,title=" "):

    #try 'ro-' 'bo-' to get different styles
    plt.plot(x_data,y_data,'bo-')
    plt.legend()

    #range
    plt.axis([0, x_data[-1]+1,0,y_range])  

    #scale
    x_major_locator=MultipleLocator(1) 
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    #names
    plt.title(title) #title
    plt.xlabel(x_name) #X label
    plt.ylabel(y_name) #Y label

    plt.show()

#ys contains all the data from the file
epoches,ys=readfile("train_data.txt",2)
draw(epoches,ys[0],"epoches","losses",2)
draw(epoches,ys[1],"epoches","accuracy")