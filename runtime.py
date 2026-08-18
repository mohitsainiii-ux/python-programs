import timeit

def measure_runtime():
    execution_time = timeit.timeit("1+1", number=100)
    print("Running time for 100 execution : ", execution_time , "seconds")

measure_runtime()