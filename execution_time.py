import timeit

def measure_time():
    time_taken = timeit.timeit("1 + 1", number= 100)
    print("Running time : ", time_taken)

measure_time()