import requests
import json
import pymysql

#consumindo a API
request = requests.get('http://teste-inpe.herokuapp.com/')

db = pymysql.connect("localhost","root","essasenhae#Will6969","inpe" )

#parseando os dados
dados = json.loads(request.text)

cursor = db.cursor()

#salvando os dados no banco
'''i = 0
while i < len(dados):
    
    cursor.execute("INSERT INTO dados (id) VALUES ('{}')".format(json.dumps(dados[i])))
    
    i+=1'''
    
#buscando os dados do banco
busca = cursor.execute("SELECT * FROM dados")


db.commit()

db.close()



