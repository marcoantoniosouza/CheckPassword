import sys
import getpass
from http_request import pwned_api_pw
from hash_password import hash_txt_pw


def main():
	arg_count = len(sys.argv)

	if arg_count == 1:
		arg_pw = getpass.getpass(prompt='Digite a senha: ')
	else:
		arg_pw = sys.argv[1]

	hex = hash_txt_pw(arg_pw)
	arr = pwned_api_pw(hex[:5])

	pw_count = arr.get(hex[5:])

	if pw_count == None:
		print("Senha não encontrada")
	else:
		print("Senha encontrada. Número de ocorrências: " + pw_count)

if __name__ == '__main__':
	main()