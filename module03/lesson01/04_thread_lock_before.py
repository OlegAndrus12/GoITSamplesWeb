# Importing the threading module
# The final answer might be incorrect due to the race condition. 
# There may be cases where a thread is unable to write the updated value to 
# the shared variable deposit before the context switch, and the other thread 
# reads a non-updated value; thus, leading to an unpredictable result.


import threading
deposit = 100


# Function to add profit to the deposit
def add_profit(): 
    global deposit
    for i in range(100000):
        deposit = deposit + 10


# Function to deduct money from the deposit
def pay_bill(): 
    global deposit
    for i in range(100000):
        deposit = deposit - 10

if __name__ == "__main__":
    # Creating threads
    thread1 = threading.Thread(target = add_profit, args = ())
    thread2 = threading.Thread(target = pay_bill, args = ())
    # Starting the threads
    thread1.start() 
    thread2.start()
    # Waiting for both the threads to finish executing 
    thread1.join()
    thread2.join()
    # Displaying the final value of the deposit
    print(deposit)
