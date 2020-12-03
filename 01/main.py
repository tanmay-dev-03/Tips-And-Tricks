import os

terminal_size = os.get_terminal_size()

print(terminal_size)

print("-"*terminal_size.columns)
print("Hello there!".center(terminal_size))
print("-"*terminal_size.columns)
print("\n"*2)
print(" Content with different fill ".center(terminal_size.columns,"#"))
