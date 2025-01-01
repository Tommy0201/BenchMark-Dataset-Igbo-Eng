import pandas as pd


def preprocessing_find_shortest(file_name):
    df = pd.read_csv(file_name)


    unique_values = df["Reject"].unique()

    # Print the unique values
    print("Unique values in AssignmentStatus", ":", unique_values)

    # Filter out rows where AssignmentStatus is "Rejected"
    filtered_df = df[df['AssignmentStatus'] != "Rejected"]

    # Select specific columns
    selected_columns = filtered_df[['WorkTimeInSeconds', 'WorkerId', 'AssignmentStatus', 
                                    'Input.pid_sent', 'Answer.translated', 'LifetimeApprovalRate']]

    # Rename columns
    selected_columns = selected_columns.rename(columns={
        'Input.pid_sent': 'pid_input',
        'Answer.translated': 'eng_output',
    })

    selected_columns['WorkTimeInMinutes'] = selected_columns['WorkTimeInSeconds'] / 60

    # Calculate and print the number of unique WorkerId
    num_unique_workers = selected_columns['WorkerId'].nunique()
    print("Number of unique Worker IDs:", num_unique_workers)

    num_col = selected_columns.shape[0]

    print("Columns: ", num_col)

    selected_columns.to_csv("GPT-Benchmark/pid1.csv",index=False)

    shortest_times = selected_columns.nsmallest(20, 'WorkTimeInSeconds')

    output_df = shortest_times[["WorkerId","WorkTimeInSeconds","LifetimeApprovalRate",'pid_input','eng_output']]

    output_df.to_csv("GPT-Benchmark/pidgin_shortest2.csv", index=False)
    
if __name__ == "__main__":
    # preprocessing_find_shortest("GPT-Benchmark/Pidgin_batch_results.csv")
    df = pd.read_csv("GPT-Benchmark/Pidgin_batch_results.csv")
    filtered_df = df[df['AssignmentStatus'] != "Rejected"]
    selected_df = filtered_df[['Input.pid_sent', 'Answer.translated']]
    # Rename columns
    selected_df  = selected_df.rename(columns={
        'Input.pid_sent': 'igbo_source',
        'Answer.translated': 'eng_translation',
    })
    selected_df.to_csv("GPT-BenchMark/AmazonMTurk/Pidgin_Trans.csv", index=False)
