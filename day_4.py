# Given Data
LOGS = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

def analyze_logs(log_list):
    # Dictionary to store counts
    counts = {"ERROR": 0, "INFO": 0, "WARNING": 0}
    
    for log in log_list:
        # Bonus: Ignore case sensitivity by converting log to uppercase
        upper_log = log.upper()
        
        # Check which keyword exists in the string
        if "ERROR" in upper_log:
            counts["ERROR"] += 1
        elif "INFO" in upper_log:
            counts["INFO"] += 1
        elif "WARNING" in upper_log:
            counts["WARNING"] += 1
            
    # Bonus: Find most frequent log type
    # max() on the dictionary items based on their values (counts)
    most_frequent = max(counts, key=counts.get)
    
    return counts, most_frequent

# Execute
log_counts, top_log = analyze_logs(LOGS)

# Display Results
print("--- Log Analysis Report ---")
for log_type, total in log_counts.items():
    print(f"{log_type}: {total}")

print(f"\nMost Frequent Log Type: {top_log} ({log_counts[top_log]} occurrences)")
