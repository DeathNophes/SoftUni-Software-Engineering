text = input().split()
input_line = input()
while input_line != "3:1":
    command = input_line.split()

    if "merge" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:     # We check if the indexes are out of range!
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1   # We don't want it to break, that's why -1
        merged_elements = "".join(text[start_index:end_index + 1])      # So it does not break on index
        text[start_index:end_index + 1] = [merged_elements]     # New text

    elif "divide" in command:
        index = int(command[1])
        partitions = int(command[2])
        element = text[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):     # We use this range because we divide on these parts
            if current_element_index != partitions - 1:
                divided_partition.append(element[current_element_index * partition_length:
                                                 (current_element_index + 1) * partition_length])
            else:
                divided_partition.append(element[current_element_index * partition_length:])
        text[index:index + 1] = divided_partition

    input_line = input()
print(" ".join(text))
