import sys

print(sys.argv)

if len(sys.argv) == 1:
	print("Please provide a number")
else:
	try:
		value = int(sys.argv[1])
		print(value)
		print(type(value))
	except ValueError:
		print("Please provide a valid integer")

