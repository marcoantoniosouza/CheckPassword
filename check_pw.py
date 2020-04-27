import getpass
import argparse

from http_request import pwned_api_pw
from hash_password import hash_txt_pw

msg = {
	'input_pass': 'Digite a senha: ',
	'output_not_found': 'Senha não encontrada',
	'output_found': 'Senha encontrada.',
	'output_count': 'Número de ocorrências: ',
	'help_encode': 'Flag indicando se a senha passada já é uma HASH SHA1',
	'help_password': ''
}

parser = argparse.ArgumentParser(description='CheckPassword')
parser.add_argument('--password', '-p', nargs='?', help=msg.get('help_password'))
parser.add_argument('--encode', '-e', nargs='?', type=bool, default=False, choices=[True, False], help=msg.get('help_encode'))


def main():
	args = parser.parse_args()

	if args.password: arg_pw = args.password
	else: getpass.getpass(prompt=msg.get('input_pass'))

	if args.encode: hex = arg_pw
	else: hex = hash_txt_pw(arg_pw)

	arr = pwned_api_pw(hex[:5])

	pw_count = arr.get(hex[5:])

	if not pw_count: print(msg.get('output_not_found'))
	else: print(msg.get('output_found') + ' ' + msg.get('output_count') + pw_count)


if __name__ == '__main__':
	main()