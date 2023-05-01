import time, random
n = int(input())

def compute_e_ver1(n):

    sum = 1
    for i in range(1, n+1):
        factorial = 1
        for j in range(1, i+1):
            factorial *= j
        sum += 1/factorial
    return sum	

print(compute_e_ver1(n))

before = time.process_time()
compute_e_ver1(n)
after = time.process_time()
print(after - before)
	
def compute_e_ver2(n):

    sum = 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        sum += 1/factorial
        
        if i == n:
            sum += 1/((i-1)*factorial*i)  
    
    return sum 

print(compute_e_ver2(n))

before = time.process_time()
compute_e_ver2(n)
after = time.process_time()
print(after - before)
	
