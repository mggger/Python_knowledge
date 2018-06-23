import pandas as pd 
import random

for i in range(1, 5):
    name = f'{i}.csv'
    result = []
    length = 10000000
    for i in range(length):
        key = i
        value = random.randint(970, 1000)
        result.append((key, value))
    df = pd.DataFrame(result, columns=['Key', 'Value'])
    df.to_csv(name, index=False)

