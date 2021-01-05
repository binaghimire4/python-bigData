import pandas as pd
import numpy as np
df = pd.DataFrame(data=np.random.randint(99999, 99999999, size=(10000000,14)),columns=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14'])
df['C15'] = pd.util.testing.rands_array(5, 10000000)
# Store data in CSV format
df.to_csv("huge_data.csv")
