# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function


# works only for lower case and for abs(rot_num) less than 26. will try to add code to cover those cases later.
def string_rotator(s, rot_num):
		rotated_s = ''
		for c in s:
			x = ord(c) + rot_num
			if x <= 97:
				x = 122 + 1 - 97 + x
				rotated_s += chr(x)
			elif (x >= 97 and x <= 122):
				rotated_s += chr(x)
			else:
				x = x - 122 - 1 + 97
				rotated_s += chr(x)
		print rotated_s
# main() calls the above functions with interesting inputs,
def main():
	string_rotator("melon",-20)
	string_rotator("cheer",7)
	string_rotator("sleep",9)
	

if __name__ == '__main__':
  main()