import numpy as np

N, M = map(int, input().split())


array = np.array([list(map(int, input().split())) for _ in range(N)])


mean_result = np.mean(array, axis=1)  
var_result = np.var(array, axis=0)   
std_result = np.std(array, axis=None) 

print(mean_result)
print(var_result)
print(f"{std_result:.11f}" if std_result > 0 else f"{std_result:.1f}")
