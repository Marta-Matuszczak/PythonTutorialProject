with open("notes.txt", "w") as file:
    file.write("some todo...")


# This is an alternative for:
"""
file = open("notes.txt", "w")
try:
    file.write("some todo...")
finally:
    file.close()
"""
