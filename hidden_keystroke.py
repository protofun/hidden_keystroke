import maskpass

# One line of code - encoding the normal visible password in a encoded not visible password with '*' as symbol
passwd = maskpass.askpass(prompt="Enter a password: ", mask="*")




