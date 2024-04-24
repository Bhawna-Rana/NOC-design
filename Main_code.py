# Initialize variables
total_latency = 0
total_bytes_transferred = 0
total_transactions = 0

# Read the interface monitor output line by line
for line in interface_monitor_output:
    timestamp, txn_type, data = parse_line(line)
    
    # Update total transactions count
    total_transactions += 1
    
    # Calculate latency for reads
    if txn_type == "Rd":
        start_time = timestamp
        while True:
            next_line = read_next_line()
            next_timestamp, next_txn_type, _ = parse_line(next_line)
            if next_txn_type == "Data":
                end_time = next_timestamp
                break
        latency = end_time - start_time
        
    # Calculate latency for writes
    elif txn_type == "Wr":
        # Assuming one cycle latency for writes
        latency = 1
    
    # Calculate bandwidth
    bytes_transferred = calculate_bytes_transferred(data)
    
    # Update total latency and bytes transferred
    total_latency += latency
    total_bytes_transferred += bytes_transferred

# Calculate average latency and bandwidth
average_latency = total_latency / total_transactions
bandwidth = total_bytes_transferred / total_transactions

# Return average latency and bandwidth
return average_latency, bandwidth
