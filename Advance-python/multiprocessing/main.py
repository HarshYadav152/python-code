import multiprocessing
import multiprocessing.process
import concurrent.futures
import requests
 
def downloadFile(url,name):
    print(f"Start downloading {name}")
    resoponse = requests.get(url)
    open (f"downlload/photo{name}.jpg","wb").write(resoponse.content)
    print(f"Finish downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(50):
        #downloadFile(url,i)
        p = multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadFile,l1,l2)
    for r in results:
        print(r)