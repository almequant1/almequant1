# -*- encoding utf-8 -*-
import os, requests, time, sys, decimal, urllib, http.client

#DEFINIÇÃO DE VARIÁVEIS
x=1
#lendo linhas do arquivo 
cred = [] # Declarando o vetor cred

#Abrindo arquivo com API key e secret para escrever nas variaveis.
apiks = open("C:/users/almeq/Documents/apiks.txt",mode='r')
for line in apiks:
    cred.append(line.rstrip()) #Add cada linha em uma posição no vetor Cred
apiks.close()
API_KEY = cred[0] # Add primeira linha do txt em API_key
API_SECRET = cred[1] # Add segundalinha do txt em API_SECRET 

#até aqui o código está 100% ok - já testado.


# Criando Dicionário que contém as credenciais de acesso
credenciais = {
                "grant_type": "client_credentials", #Não sei se está certo
                "api_key":  API_KEY , #OK
                "api_secret":  API_SECRET #OK 
              }

#DEFINIÇÃO DE FUNÇÕES
#def buy_BTCQ
#requestbuy = https://quantum.atlasquantum.com/api/buy
#buy BTCQ order a 0.02, usando BTC_balance total

#def sell_BTCQ
#requestsell = https://quantum.atlasquantum.com/api/sell
#sell BTCQ order a 0.03, usando BTCQ_balance total

#OPERAÇÃO
while x==1:

	acesso = requests.post('https://quantum.atlasquantum.com/api/oauth/token', data = credenciais) #login/autenticate
	print(acesso.text)
		#Vou adicionar depois um ifelse com sucesso/falha de conexão, mas primeiro preciso entender o <Response>

	BTC_balance = requests.get('https://quantum.atlasquantum.com/api/balance/BTC') #check BTC_balance
	print("Seu Saldo de BTC é: ",BTC_balance.text)
	#if BTC_balance > 0:
		#print("Saldo BTC maior que zero, tentando colocar ordem para comprar BTCQ!")
		#buy_BTCQ() #executar função de comprar BTCQ

	BTCQ_balance = requests.get('https://quantum.atlasquantum.com/api/balance/BTCQ') #check BTCQ_balance
	print("Seu Saldo de BTCQ é: ",BTCQ_balance.text)
	#if BTCQ_balance > 0:
		#print("Saldo BTCQ maior que zero, tentando colocar ordem para comprar BTCQ!")
		#sell_BTCQ() #executar função de vender BTCQ

	print("Reiniciando Ciclo em 1s")
	time.sleep(1)
