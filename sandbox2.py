def remove_bracketed_part(timestamp_str):
    # Split the string on space and take all parts except the last one (in brackets)
    parts_without_brackets = timestamp_str.split()[:-1]
    # Join these parts back into a string
    adjusted_timestamp = ' '.join(timestamp_str.split()[:-1])
    return adjusted_timestamp

# Example usage
timestamp = "Fri, 29 Dec 2023 10:42:19 -0800 (PST)"
adjusted_timestamp = remove_bracketed_part(timestamp)
print(adjusted_timestamp)