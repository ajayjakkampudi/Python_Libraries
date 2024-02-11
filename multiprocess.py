from multiprocessing import Process,Pool


X=[1,2,3]
print("X")
def func(x):
    for i in range(x):
        pass
    print(f"Func {x}")
    
if __name__=="__main__":
    p=Pool(processes=3)
    p.map(func,[40,400000,4])