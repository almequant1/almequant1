# -*- encoding utf-8 -*-
import os, requests, time, sys, decimal, urllib, http.client

#DEFINIÇÃO DE VARIÁVEIS
x=1
api_key = open("C:/users/almeq/Documents/apikey.txt", mode='r')
api_key = api_key.read()
api_secret = open("C:/users/almeq/Documents/apisecret.txt", mode='r')
api_secret = api_secret.read()
#Já testei essa função de leitura dos arquivos com api e está ok.
#Preferi deixar dessa forma pq ai eu posso pedir ajuda no código sem expor minha API.

#DEFINIÇÃO DE FUNÇÕES
#def buy_BTCQ
#requestbuy = https://quantum.atlasquantum.com/api/buy
#buy BTCQ order a 0.02, usando BTC_balance total

#def sell_BTCQ
#requestsell = https://quantum.atlasquantum.com/api/sell
#sell BTCQ order a 0.03, usando BTCQ_balance total

#OPERAÇÃO
#while x==1:

acesso = requests.post('https://quantum.atlasquantum.com/api/oauth/token', api_key, api_secret) #login/autenticate
print(acesso)

BTC_balance = requests.get('https://quantum.atlasquantum.com/api/balance/BTC') #check BTC_balance
print(BTC_balance)
#if BTC_balance > 0,
	#buy_BTCQ() #executar função de comprar BTCQ

BTCQ_balance = requests.get('https://quantum.atlasquantum.com/api/balance/BTCQ') #check BTCQ_balance
print(BTCQ_balance)
#if BTCQ_balance > 0
	#sell_BTCQ() #executar função de vender BTCQ

#	print("Reiniciando Ciclo em 1s")
#	time.sleep(1)
