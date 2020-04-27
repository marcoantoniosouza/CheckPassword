import sys
import getpass
import argparse

from http_request import pwned_api_pw
from hash_password import hash_txt_pw

parser = argparse.ArgumentParser(description='CheckPassword')
parser.add_argument('--password', '-p', nargs='?')


def main():
	args = parser.parse_args()

	if args.password == None:
		arg_pw = getpass.getpass(prompt='Digite a senha: ')
	else:
		arg_pw = args.password

	hex = hash_txt_pw(arg_pw)
	arr = pwned_api_pw(hex[:5])

	pw_count = arr.get(hex[5:])

	if pw_count == None:
		print("Senha não encontrada")
	else:
		print("Senha encontrada. Número de ocorrências: " + pw_count)

if __name__ == '__main__':
	main()