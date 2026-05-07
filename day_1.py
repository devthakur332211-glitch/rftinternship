data = [10, None, 20, 10, "", 30, None, 40]

def clean_data(input_list):
    # 1. Remove invalid values (None and empty strings)
    
    filtered_data = [item for item in input_list if item is not None and item != ""]
    
    # 2. Remove duplicates
    
    unique_data = list(set(filtered_data))
    
    # Bonus: Sort the final list
    unique_data.sort()
    
    # Bonus: Count how many values were removed
    removed_count = len(input_list) - len(unique_data)
    
    return unique_data, removed_count

# Execute the function
clean_list, count = clean_data(data)

# Output results
print(f"Cleaned List: {clean_list}")
print(f"Total values removed: {count}")
