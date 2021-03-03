import random
from matplotlib import pyplot as plt

random.seed(2)
L1 = [random.randint(1,10) for x in range(20)]
print(L1)
L2 = [random.randint(1,10) for x in range(20)]
print(L2)
L3 = [random.randint(1,10) for x in range(20)]
print(L3)
plt.plot(L1, "r-.", label="list_1")
plt.plot(L2, "g-o", label="list_2")
plt.plot(L3, "y-*", label="list_3")
plt.legend()
plt.show()

















