import os

file = open("file.txt", "a")
file.write("\nLorem ipsum dolor sit amet, consectetur adipiscing elit.\nSuspendisse ultrices enim lorem, at tincidunt nibh varius quis. Fusce sollicitudin massa dictum, ultricies tellus nec, porta sapien. Phasellus sodales augue id diam mollis, ac molestie magna lobortis. Etiam consectetur lacinia arcu id pellentesque. Phasellus varius mattis magna non fringilla. Curabitur non metus in diam lobortis tempus. Fusce tempus ut mi quis tempor. Donec in leo a ipsum lacinia viverra. Aenean gravida felis odio, sed cursus risus consequat in. Curabitur dignissim quam id ullamcorper porta. In nec magna dolor. Sed condimentum justo id orci varius tincidunt. Fusce elementum mauris et quam varius, non venenatis diam dictum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;")
file.close()

file = open("file.txt", "r")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

file = open("file.txt", "w")
new_score = 9
file.write("Score = {}".format(new_score))
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()

if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")
