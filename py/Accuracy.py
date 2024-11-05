import pandas as pd# Define the true angle for the new data set
import numpy as np


true_angle = 10

# Data for the tests 120 degrees
data = {
    "X": [-6.00, -15.50, -15.00, -37.50, -23.00, -73.00, -17.00, -22.00,
          -71.00, -65.50, -8.50, -34.50, -35.50, -23.00, -19.50, -19.00,
          -15.00, -68.50, -38.50, -22.50, -18.50, -73.00, -35.50, -21.50,
          -20.00, -76.50, -37.00, -13.00, -15.00],
    "Y": [12.12, 45.90, 45.03, 80.54, 55.43, 105.66, 29.44, 50.23, 114.32,
          104.79, 32.04, 71.88, 75.34, 48.50, 32.04, 50.23, 41.57, 104.79,
          78.81, 44.17, 38.97, 109.12, 78.81, 42.44, 46.77, 111.72, 71.01,
          38.11, 53.69],
    "Result_Angle": [116.33, 108.66, 108.42, 114.97, 112.54, 124.64, 120.00,
                     113.65, 121.84, 122.01, 104.86, 115.64, 115.23, 115.37,
                     121.32, 110.72, 109.84, 123.17, 116.04, 117.00, 115.39,
                     123.78, 114.25, 116.87, 113.15, 124.40, 117.52, 108.84,
                     105.61]
}

# Define the initial data set
# Define the initial data set at 0 degree
data = {
    "X": [110.00, 81.50, 48.00, 64.00, 43.50, 100.50, 49.50, 70.00, 82.00, 46.50,
          94.00, 76.50, 44.00, 65.00, 25.00, 77.50, 49.50, 49.00, -23.00, 27.00,
          46.50, 37.00, -15.50, 39.50, 44.50, 21.50, 38.00, 81.00, 63.00, 67.00],
    "Y": [15.59, 32.04, 29.44, 24.25, 18.19, 14.72, 25.11, 19.05, 17.32, 14.72,
          19.05, 18.19, 22.52, 13.86, 13.86, 7.79, 9.53, 12.12, 31.18, 17.32,
          7.79, 10.39, 21.65, 9.53, 11.26, 18.19, 12.12, 17.32, 17.32, 17.32],
    "Result Magnitude": [111.10, 87.57, 56.31, 68.44, 47.15, 101.57, 55.51, 72.55, 83.81, 48.78,
                         95.91, 78.63, 49.43, 66.46, 28.58, 77.89, 50.41, 50.48, 38.74, 32.08,
                         47.15, 38.43, 26.63, 40.63, 45.90, 28.16, 39.89, 82.83, 65.34, 69.20],
    "Result_Angle": [8.07, 21.46, 31.53, 20.75, 22.69, 8.33, 26.90, 15.23, 11.93, 17.57,
                     11.46, 13.37, 27.10, 12.03, 29.00, 5.74, 10.89, 13.90, 126.42, 32.68,
                     9.52, 15.69, 125.60, 13.56, 14.20, 40.23, 17.70, 12.07, 15.37, 14.49]
}


# Create a DataFrame
df_120 = pd.DataFrame(data)

# Calculate absolute error
df_120['Absolute_Error'] = np.abs(df_120['Result_Angle'] - true_angle)

# Sort the DataFrame by Result Angle
df_120_sorted = df_120.sort_values(by='Result_Angle')

# Drop 2% from the start and end of the sorted DataFrame
drop_count = int(len(df_120_sorted) * 0.08)  # Calculate 2% of the total count
df_120_trimmed = df_120_sorted.iloc[drop_count:-drop_count] if drop_count > 0 else df_120_sorted

# Calculate metrics
num_tests = len(df_120_trimmed)
accuracy = df_120_trimmed['Absolute_Error'].mean()
precision = df_120_trimmed['Absolute_Error'].std()



# Calculate True Positives, False Positives, False Negatives
# Assuming any angle within 5 degrees of the true angle is a True Positive
tolerance = 1
true_positives = ((df_120_trimmed['Result_Angle'] >= (true_angle - tolerance)) &
                  (df_120_trimmed['Result_Angle'] <= (true_angle + tolerance))).sum()
false_positives = (num_tests - true_positives)  # Assuming all non-TPs are FP
false_negatives = 0  # No false negatives in this context as we only count within the tolerance

# Calculate Recall and F1 Score
recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Create the results table
results_table_120 = pd.DataFrame({
    "Metric": ["Number of Tests", "Accuracy", "Precision", "Recall", "F1 Score"],
    "Value": [num_tests, accuracy, precision, recall, f1_score]
})

print(results_table_120)
print(len(df_120_trimmed))
