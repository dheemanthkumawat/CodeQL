import os

def read_file(filename):
    # Vulnerable to command injection if `filename` contains shell metacharacters.
    os.system(f"cat {filename}")

if __name__ == "__main__":
    filename = input("Enter the filename to read: ")
    read_file(filename)
