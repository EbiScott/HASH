import sys
import os

from encode_file import encode_menu
from decode_file import decode_menu
from hash_file import hash_menu
from crack_hash_file import crack_menu


def banner():
	print("""
		###	###	##	 ########  ###    ###
		###	###    #  #     ##	   ###    ###
		###########   ######   ########	   ##########
		###	###  ##    ##	      ##   ###	  ###
		###	### ###    ### ########    ###	  ###


   			Remember to Hash Responsibly...


Created by:
	X: @Ebi_Scott
""")


def main():
	while True:
		banner()
		print("[1] Encode")
		print("[2] Decode")
		print("[3] Hash")
		print("[4] Crack Hash")
		print("[0] Exit")


		choice = input(">>")

		if choice == "1":
			encode_menu()
		elif choice == "2":
			decode_menu()
		elif choice == "3":
			hash_menu()
		elif choice == "4":
			crack_menu()
		elif choice == "0":
			sys.exit()
		else:
			print("Invalid choice, please enter a number from 1-4 or 0 to exit")



if __name__ == "__main__":
	main()

