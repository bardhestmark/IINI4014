name = input("What is your full name?\n")

initials = ''

for n in name.split():
    initials += n[0].upper()

print("Hello %s \nYour initials are %s \nWelcome to python programming!" % (name, initials))
