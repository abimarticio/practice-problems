# Given a string name = “Zophie”, display the following output.
# ***Z***
# ***o***
# ***p***
# ***h***
# ***i***
# ***e***
name = "Zophie"

for index in range(len(name)):
    print(f"***{name[index]}***")

for letter in name:
    print(f"***{letter}***")

for index, letter in enumerate(name):
    print(f"***{letter}***")