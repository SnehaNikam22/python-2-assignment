filename = "example.txt"

# 1. Create and write to a file
with open(filename, "w") as file:
    file.write("Hello, this is the first line")
    file.write("File handling in Python is easy")

print("File created and written successfully")

# 2. Read the file
with open(filename, "r") as file:
    content = file.read()
    print("Reading file content:")
    print(content)

# 3. Append to the file
with open(filename, "a") as file:
    file.write("This line is appended later")

print("Content appended successfully")

# 4. Read again after appending
with open(filename, "r") as file:
    print("Updated file content:")
    print(file.read())

                                                                                                                                                                                                                                                                                                                                                                                                                       