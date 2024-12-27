import pandas as pd


df = pd.read_csv("GPT-Benchmark/igbo_amazon.csv")


unique_values = df["Reject"].unique()

# Print the unique values
print("Unique values in AssignmentStatus", ":", unique_values)

# Filter out rows where AssignmentStatus is "Rejected"
filtered_df = df[df['AssignmentStatus'] != "Rejected"]

# Select specific columns
selected_columns = filtered_df[['WorkTimeInSeconds', 'WorkerId', 'AssignmentStatus', 
                                'Input.igbo_sent', 'Answer.translated', 'LifetimeApprovalRate']]

# Rename columns
selected_columns = selected_columns.rename(columns={
    'Input.pid_sent': 'igbo_input',
    'Answer.translated': 'eng_output',
})

selected_columns['WorkTimeInMinutes'] = selected_columns['WorkTimeInSeconds'] / 60

# Calculate and print the number of unique WorkerId
num_unique_workers = selected_columns['WorkerId'].nunique()
print("Number of unique Worker IDs:", num_unique_workers)

num_col = selected_columns.shape[0]

print("Columns: ", num_col)

selected_columns.to_csv("GPT-Benchmark/sell1.csv",index=False)

shortest_times = selected_columns.nsmallest(20, 'WorkTimeInSeconds')

output_df = shortest_times[["WorkerId","WorkTimeInSeconds","LifetimeApprovalRate",'igbo_input','eng_output']]

output_df.to_csv("GPT-Benchmark/shortest2.csv", index=False)
