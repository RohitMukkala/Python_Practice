def count_local_variables():
    x = 10
    y = 20
    z = 30
    local_vars = locals()
    num_local_vars = len(local_vars)
    print(f"Number of local variables declared in the function: {num_local_vars}")
   
count_local_variables()
