#!python

"""The intention of this module is to show examples of basic user input in python """
import sys

print("Total arguments passed:", len(sys.argv))

print("This is the name of the python script:", sys.argv[0])

print("The following arguments were entered:")
for x in range(1, len(sys.argv)):
    print("\t", sys.argv[x])

print("")
print("Lets get some real time user input...")
response = input("Should we deploy the following to production?[y/n]")

if response in [*'yY']:
    print("Yes, deploying to production")
elif response in [*"Nn"]:
    print("No, but too late its been deployed...")
else:
    print("I don't understand your input try again")
