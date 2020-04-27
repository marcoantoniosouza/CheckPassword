import sys
import getpass
import argparse

from http_request import pwned_api_pw
from hash_password import hash_txt_pw

msg = {
	'input_pass': 'Digite a senha: ',
	'output_not_found': 'Senha não encontrada',
	'output_found': 'Senha encontrada.',
	'output_count': ' Número de ocorrências: '
}

parser = argparse.ArgumentParser(description='CheckPassword')
parser.add_argument('--password', '-p', nargs='?')


def main():
	args = parser.parse_args()

	arg_pw = args.password if args.password else getpass.getpass(prompt=msg.get('input_pass'))

	hex = hash_txt_pw(arg_pw)
	arr = pwned_api_pw(hex[:5])

	pw_count = arr.get(hex[5:])

	print(msg.get('output_not_found')) if not pw_count else print(msg.get('output_found') + msg.get('output_count') + pw_count)


if __name__ == '__main__':
	main()