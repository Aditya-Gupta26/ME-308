with open('MDP_final.txt', 'r') as file:
    # Read the contents of the file into a list
    file_contents = file.readlines()

# Open the file in 'write' mode to write the modified content
with open('new_try.txt', 'w') as file:
    # Write the modified content to the file
    file.writelines(file_contents)

x = 1