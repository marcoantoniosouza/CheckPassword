import requests

# recebe como parêmetro os primeiros 5 caracteres da HASH gerada pra senha
# retorna um dicionário com o restante da HASH e a quantidade de ocorrências 
def pwned_api_pw(hex):
	req = requests

	response = req.get('https://api.pwnedpasswords.com/range/' + hex)

	return ({i.split(':')[0]:i.split(':')[1] for i in response.text.split('\r\n')})