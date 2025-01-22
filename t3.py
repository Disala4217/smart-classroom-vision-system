import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)  # For reproducibility
data = {
    "attendance_rate": np.random.randint(50, 101, 100),  # 50% to 100%
    "class_participation": np.random.randint(1, 11, 100),  # 1 to 10
    "gaze_duration": np.random.randint(30, 121, 100),  # 30 to 120 mins
    "engagement_level": np.random.choice([1, 2, 3], 100)  # 1=High, 2=Medium, 3=Low
}

df = pd.DataFrame(data)
print(df.head())



