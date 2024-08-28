import time

def measure_time(func, text, iterations=1000):
    total_time = 0
    for _ in range(iterations):
        _, exec_time = func(text)
        total_time += exec_time
    return total_time / iterations

def master_yoda(text):
    start_time = time.time()
    result = ' '.join(text.split()[::-1])
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def master_rada(text):
    start_time = time.time()
    x = text.split()
    y = " ".join(x[::-1])
    end_time = time.time()
    execution_time = end_time - start_time
    return y, execution_time

text = 'We are ready'
iterations = 1000

avg_time_yoda = measure_time(master_yoda, text, iterations)
avg_time_rada = measure_time(master_rada, text, iterations)

print(f"Average execution time for master_yoda: {avg_time_yoda} seconds")
print(f"Average execution time for master_rada: {avg_time_rada} seconds")