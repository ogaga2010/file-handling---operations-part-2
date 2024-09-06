def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("Reading from file:")
        print(content)

def write_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)
        print(f"Written to file: {text}")

def append_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text)
        print(f"Appended to file: {text}")

def modify_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace(old_text, new_text)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Replaced '{old_text}' with '{new_text}' in file.")

# Codingal usage
file_path = 'Codingal.txt'

# Create the example file
with open(file_path, 'w') as file:
    file.write("Hello, World!\nThis is a test file.\nIt contains multiple lines.\n")

# Read from file
read_file(file_path)

# Write to file
write_file(file_path, "This is new content.\n")

# Read from file again to see the changes
read_file(file_path)

# Append to file
append_file(file_path, "This line is appended.\n")

# Read from file again to see the changes
read_file(file_path)

# Modify file content
modify_file(file_path, "new content", "modified content")

# Read from file again to see  the changes
read_file(file_path)