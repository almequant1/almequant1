# -*- encoding utf-8 -*-
import os, requests, time, sys, decimal, urllib, http.client, json

#DEFINIÇÃO DE VARIÁVEIS
x=1
#lendo linhas do arquivo 
cred = [] # Declarando o vetor cred

########## Abrindo arquivo com API key e secret para escrever nas variaveis ##########
apiks = open("C:/users/almeq/Documents/apiks.txt",mode='r')
for line in apiks:
    cred.append(line.rstrip()) #Add cada linha em uma posição no vetor Cred
apiks.close()
API_KEY = cred[0] # Add primeira linha do txt em API_key
API_SECRET = cred[1] # Add segundalinha do txt em API_SECRET 

########## Criando var DIC e var JSON que contém as credenciais de acesso ##########
auth = {
                "grant_type": "client_credentials",
                "api_key": API_KEY,
                "api_secret": API_SECRET
		}
authjson = json.dumps(auth)

# Login/Autenticação (usar var json)
acesso = requests.post('https://quantum.atlasquantum.com/api/oauth/token', data = authjson)
respostaacesso = json.loads(acesso.text)  #Transformando Json em dicionário para extrair valores dos atributos
#Vou adicionar depois um ifelse com sucesso/falha de conexão, mas primeiro preciso entender o <Response>

########## Criando var DIC e var JSON que contém o token validado da sessão ##########
granttoken = {
				"grant_type": "refresh_token",
    			"refresh_token": respostaacesso['token_type'] + " " + respostaacesso['refresh_token']
   			 }
granttokenjson = json.dumps(granttoken)

########## Criando var DIC e var JSON que contém o token validado da sessão ##########
refreshtoken = {
					'Authorization': respostaacesso['token_type'] + " " + respostaacesso['refresh_token']
				}
refreshtokenjson = json.dumps(refreshtoken)
#--------------------------------até aqui o código está 100% ok - já testado.-----------------------------#

													########## DEFINIÇÃO DE FUNÇÕES #########
#def buy_BTCQ
#requestbuy = https://quantum.atlasquantum.com/api/buy
#buy BTCQ order a 0.019, usando BTC_balance total

#def sell_BTCQ
#requestsell = https://quantum.atlasquantum.com/api/sell
#sell BTCQ order a 0.020, usando BTCQ_balance total

															########## OPERAÇÃO ##########
while x==1:

	#refreshsession = requests.post('https://quantum.atlasquantum.com/api/oauth/token', data = granttokenjson)
	#print (refreshsession.text)

	#checksession = requests.post('https://quantum.atlasquantum.com/api/checksession', data = refreshtokenjson)
	#print (checksession.text)

	BTC_balance = requests.get('https://quantum.atlasquantum.com/api/balance/BTC', data = refreshtoken) #check BTC_balance
	print("Seu Saldo de BTC é: ",BTC_balance.text)
	#if BTC_balance > 0:
		#print("Saldo BTC maior que zero, tentando colocar ordem para comprar BTCQ!")
		#buy_BTCQ() #executar função de comprar BTCQ

	BTCQ_balance = requests.get('https://quantum.atlasquantum.com/api/balance/BTCQ', data = refreshtokenjson) #check BTCQ_balance
	print("Seu Saldo de BTCQ é: ",BTCQ_balance.text)
	#if BTCQ_balance > 0:
		#print("Saldo BTCQ maior que zero, tentando colocar ordem para comprar BTCQ!")
		#sell_BTCQ() #executar função de vender BTCQ

	print("Reiniciando Ciclo em 5s")
	time.sleep(5)
