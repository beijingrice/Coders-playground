import random
import threading
def main():
    li = []
    for y in range(3000):
        for x in range(3000):
            li.append((x,y,random.choice([1,2,3]),random.choice([1,2,3])))
mainThreading = threading.Thread(target=main)
mainThreading.start()
