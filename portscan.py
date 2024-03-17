import socket
import os
import sys


print("Olá, seja bem vindo ao LL Scan 1.0!")

# Capturando e validando o endereço do alvo a ser analisado
while True:
    try:
        alvo= input("Digite o endereço do alvo, exemplo hostname (bancocn.com) ou IP (104.21.52.8):")
        socket.gethostbyname(alvo)
        print("Alvo validado!")
        break

    except socket.gaierror:
        print("Alvo invalido ou inexistente")

print("Vamos Scanear algumas portas mais usadas e retornaremos as abertas")

# Portas TCP mais utilizadas
ports = [20, 21, 22, 25, 53, 80, 81, 110, 113, 143, 161, 443, 465, 554, 587, 943, 993, 995, 1043, 1194, 1433, 1434, 1521, 1522, 1523, 1524, 1525, 1526, 1935, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2399, 3050, 3306, 3389, 3690, 5432, 5960, 8043, 8044, 8080, 8181, 8282, 8443, 10025]

# Função para reiniciar o programa em caso de erro.
def reiniciar_programa():
    python = sys.executable
    os.execl(python,python, *sys.argv)

# Laço for irá percorrer todas as portas fazer a conexão e retornar as portas abertas
try:
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.3)
        code = client.connect_ex((alvo, port))
        if code == 0:
            print(port, "Porta aberta")
except ValueError:
    print("Nos desculpe! Ocorreu um erro, reiniciaremos o programa!")
    reiniciar_programa()

# Interação para scaner personalizado ou finalizar programa
while True:
    resposta = input("Deseja fazer um scaner personaliza? Digite  S / N:")
    if (resposta.lower() == "s"):
        break

    elif (resposta.lower() == "n"):
        print("Obrigado por usar o LL Scan! Estamos finalizando o programa!")
        sys.exit()
        
    else: 
        print("Comando inválido! Digite S / N:")
    

# Capturando portas para scaner personalizado
while True:
    try:
        ent_port = input("Digite os numeros das portas apenas separados por espaços: exemplo (80 71 100)")
        li_ports = list(map(int, ent_port.split()))
        print("Começando o scaner  ", li_ports)
        break
    except ValueError:
        print("Dados inválidos! Por favor digite novamente!")

# Scaneando portas digitadas       
try:
    for port2 in li_ports:
        client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2.settimeout(0.3)
        code2 = client2.connect_ex((alvo, port2))
        if code2 == 0:
            print(port2, "Porta aberta")
    
    print("Retornamos apenas as portas abertas, as demais estão fechadas")
               
except ValueError:
    print("Nos desculpe! Ocorreu um erro, reiniciaremos o programa!")

# Scanear outro alvo ou finalizar programa
while True:
    resposta2 = input("Deseja scanear outro alvo?  Digite  S / N:")
    if (resposta2.lower() == "s"):
        reiniciar_programa()
        break

    elif (resposta2.lower() == "n"):
        print("Obrigado por usar o LL Scan! Estamos finalizando o programa!")
        sys.exit()
        
    else: 
        print("Comando inválido! Digite S / N:")
