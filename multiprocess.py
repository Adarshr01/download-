# import concurrent.futures
import multiprocessing as mp
import requests 
import os

def download (url , name ):
    
    dirname="Images"
    if(os.path.exists(dirname)):
        dirname=dirname + "1"
    else:
        os.mkdir(dirname)
    print(f"Downloading file_{name}.jpg  ...")
    image = requests.get(url)
    file=open(f"{dirname}/file_{name}.jpg","wb")
    file.write(image.content )
    print(f"Downloaded file_{name}.jpg")
    
    
    
    # return 1 
if __name__== "__main__":
    list =[]
    url=input("Enter the url\n:")
    number =int(input("Enter the number of images to download\t:"))
    for i in range(number):
        process = mp.Process(target=download,args=[url,i])
        process.start()
        list.append(process)

    for process in list :
        process.join()