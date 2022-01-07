
import cv2
import time

#this is for me because i tend to loose track of time 
start_time = time.time()
timer =0
timer = input("Give the amount of time you want to spend  :")
timer = timer*216000   
def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            cv2.destroyAllWindows()

main()