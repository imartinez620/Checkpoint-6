class Usuario:
	def __init__(self, usuario, psw):
		self.usuario = usuario
		self.psw = psw

mi_usuario = Usuario("Iñaki","ASD")

print(f'Mi usuario es {mi_usuario.usuario} y mi clave {mi_usuario.psw}')