import multiprocessing
from MAX_AI import ClapDetect
from gui11 import preview_gif

if __name__ == "__main__":
    # Create processes for both functions
    process2 = multiprocessing.Process(target=preview_gif)

    process1 = multiprocessing.Process(target=ClapDetect)
    
    # Start the processes
    process2.start()
    #process1.start()
    

    # Wait for both processes to finish
    process2.join()
   # process1.join()
    

   