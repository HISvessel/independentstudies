#!/usr/bin/env python3
"""this is an introduction to the pandas framework, that goes hand in
hand with numpy for array computation by providing powerful data structures:
1) Series
2) DataFrames

They are built on NumPy and are ideal for logging and analyzing data. In our future app,
it is good for workout data, aggregating form metrics over sessions, or preparing
summaries like average elbow angles across reps."""

import pandas as pd
import numpy as np

#data recompiled from captured images
#stored as a dictionary of repetitions and elbow angles at each repetition
data = {
    'rep': [1, 2, 3, 4, 5],
    'elbow_angle': [95, 88, 90, 92, 87]
}
df = pd.DataFrame(data) #data compiled as a table
print(df.describe())  # summary stats

#makes and prints new kv of all reps with above 90 degrees bend in elbow, stored as true or false
df['above_90'] = df['elbow_angle'] > 90
print(df)
