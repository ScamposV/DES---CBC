'''
pyDes v2.0.1
@author Sebastián Campos
Bibliografías:
https://pypi.org/project/pyDes/#description
https://github.com/twhiteman/pyDes/blob/master/pyDes.py
https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
'''
import base64
from string import Template
from pyDes import *

'''
key = "hola1234";
text="e";
iv="00000002"
'''

#key
key= input("Ingrese una llave de 8 caracteres: ")
while len(key) !=8:
	key= input("Ingrese una llave de 8 caracteres, ni más ni menos: ");
#iv
iv= input("Ingrese una frase de 8 caracteres: ")
while len(iv) !=8:
	iv= input("Ingrese una llave de 8 caracteres, ni más ni menos: ");
#mensaje a cifrar
text= input("Ingrese un mensaje: ")
'''
while len(text) !=28:
	text= input("Ingrese un mensaje de 28 caracteres, ni más ni menos: ");
'''


keyb = bytes(key, 'Utf-8')
iv2= bytes(iv, 'Utf-8')
print("---------------------------------------------------------")
print ("LLave: ", keyb,"\nMensaje a cifrar: ", text,"\nvector: ", iv,"\n\n")

k = des(keyb, CBC, iv2, pad=None, padmode=PAD_PKCS5)
d = k.encrypt(text)
e=d.hex()


print ("Encrypted: %r" % e)
print ("Decrypted: %r" % k.decrypt(d, padmode=PAD_PKCS5))



f = open('index.html','w')
html="""
<!DOCTYPE html>

<html dir="ltr" lang="en">
<head>
<meta charset="utf-8"/>
<title>Mensaje Secreto</title>
<div class= $title2 id=$vector></div>
<div class= $title id=$encrip></div>
<div class=$key id=$keygold></div>
<p>$encrip</p>
</head>
<body>
<p>Este sitio contiene un mensaje secreto</p>
<script crossorigin="anonymous" integrity="sha512-nOQuvD9nKirvxDdvQ9OMqe2dgapbPB7vYAMrzJihw5m+aNcf0dX53m6YxM4LgA9u8e9eg9QX+/+mPu8kCNpV2A==" referrerpolicy="no-referrer" src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js"></script>
<script src="./DESCBC.js"></script>
</body>
</html>
"""
insertar=Template(html).safe_substitute(title='DESCBC',title2='iv' ,vector=iv,encrip=e,key='key',keygold=key)
f.write(insertar)
f.close()
