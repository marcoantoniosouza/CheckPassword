import hashlib

# recebe como parêmetro a senha em texto
# retorna HASH dessa senha em SHA1 (uppercase)
def hash_txt_pw(text):
	m = hashlib.sha1()

	m.update(text.encode())

	return m.hexdigest().upper()
