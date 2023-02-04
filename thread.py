import threading
 
 
def print_cube(num):
    # function to print cube of given num
    while True:
        print("Cube: {}" .format(num * num * num))
 
 
def print_square(num):
    while True:
        # function to print square of given num
        
        print("Square: {}" .format(num * num))
 
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
 
    # both threads completely executed
    print("Done!")