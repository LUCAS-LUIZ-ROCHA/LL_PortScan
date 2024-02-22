# LL Scan - Ferramenta de Port Scan personalizada
## Olá Lucas Luiz aqui! Deixa eu aprensentar o LL port scan.
Desenvolvi em linguagem pythom um programa para realizar port scanner (scanner de porta),
Objetivo do LL Scan é  mapear as portas TCP e UDP, e retornar quais destas portas se encontram aberta.
A ferramenta pode procurar servidores vulneráveis, serviços em um hostname e IP. Para ser usado em Pentest, para análise 
de vunerabilidade. Com objetivo de auxiliar a criar relatórios para melhoria de defesa cibernética.
O site usado para sugestão é o [www.bancocn.com](http://www.bancocn.com/), este site mantido pela [Solyd Offensive Security](https://solyd.com.br/)
para que estudantes de Cyber Security, possam atacar, explorar vunerabilidades, etc... Neste site idicado esta autorizado pela Solyd, e ele se reconstrói a cada 15
minutos.

## Como usar e como funciona:
### Primeiro ele irá solicitar o endereço do alvo:
---
### Olá, seja bem vindo ao LL Scan 1.0!
### Digite o endereço do alvo, exemplo hostname (bancocn.com) ou IP (104.21.52.8):
---
Digite o endereço do alvo, no caso do site  banco da corea do norte (feito para teste).
Não inserir o "www", exemplo o endereço http://www.bancocn.com inserir -> bancocn.com,
ou o IP -> 104.21.52.8. Caso você digite um ip ou hostname inválido ele irá solicitar novamente a entrada,
pois programei para fazer uma validação do alvo.
Em seguida ele apresentará:

---
### Alvo validado!
### Vamos Scanear algumas portas mais usadas e retornaremos as abertas:
---
O programa irá percorrer uma lista com algumas das portas TCP/IP mais usadas. Estas são:
ports = 20, 21, 22, 25, 53, 80, 81, 110, 113, 143, 161, 443, 465, 554, 587, 943, 993, 995, 1043, 1194, 1433, 1434,
1521, 1522, 1523, 1524, 1525, 1526, 1935, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2090, 2091, 2092,
2093, 2094, 2095, 2096, 2399, 3050, 3306, 3389, 3690, 5432, 5960, 8043, 8044, 8080, 8181, 8282, 8443, 10025

Você verá somente as portas abertas, e a saída será:

---

### 80 Porta aberta
### 443 Porta aberta
### 2082 Porta aberta
### 2083 Porta aberta
### 2086 Porta aberta
### 2087 Porta aberta
### 2095 Porta aberta
### 2096 Porta aberta
### 8080 Porta aberta
### 8443 Porta aberta

---

Em seguida irá solicitar mais uma entrada:

---
### Deseja fazer um scaner personaliza? Digite  S / N:

---
Caso queria finalizar digite N, o programa irá encerrar.
### -> Obrigado por usar o LL Scan! Estamos finalizando o programa! 
Digite S p/ Sim,  para continuar e o programa seguirá para você digitar as portas que deseja scanear.
Caso digite algo errado, ou sim, não, ele irá solicitar a entrada novamente. 

---
### Digite os numeros das portas apenas separados por espaços: exemplo (80 71 100):

---
Aqui, você irá inserir as portas que deseja, separadas apenas por espaços. 
exemplo: 80 70 100 
Ele irá forma uma lista, e verificar cada porta.
Caso digite 80 , outra porta, será tratado como erro e solicitará denovo a entrada correta.

logo após a verificação, retorna as portas abertas, caso não haja nenhuma, retornará vazio e apenas:

---
### Retornamos apenas as portas abertas, as demais estão fechadas
### Deseja scanear outro alvo?  Digite  S / N:

---
Caso deseje scanear outro alvo digite s, o programa irá reiniciar.
Digite n para finalizar.

