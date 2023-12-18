#!/usr/bin/python3
#Desenvolvedor: Caleb Marcelino (Mr Code)
#
#Facebook: https://www.facebook.com/caleb.marcelino.16144
#Esse script eh um modulo da ferramenta RAY-GET responsavel por efetuar ataques de bruteforce de directorios em site
import requests
import os
from time import sleep

def banner(): 
    os.system('bash ./www/bi/banner.sh')
    print('')
    os.system('echo "=============> BRUTEFORCE DE DIRECTORIO [\e[92mHabilitado\e[0m]"')
    print('==')



def bruteforce_director(target):
    
    target = target.strip()

    valid = target[-1]

    if valid == '/':
        pass
    else:
        target = target + '/'

    print('bruteforce !')

    with open('wordlist_apache.txt') as archive:
        wordlist = archive.readlines()
        discover = []  # Corrigindo para ser uma lista
        count = 0
        descoberte = 0

        print('Fazendo bruteforcing, pode demorar...')
    
        for i in wordlist:
            os.system('clear')
            os.system('bash ./www/bi/banner2.sh')
            print('')
            print('=============> BRUTEFORCE DE DIRECTORIO [\e[92mHabilitado\e[0m]')
            print('==')

            dir = i.strip()
            if dir[0] == '/' and target[-1] == '/':
                obb = dir[1:]
                url = target + obb
            else:
                url = target + dir
            print('[+]- Os directorios descobertos sao guardados no arquivo: director_discovered.temp')
            print(f"=============> Testando: {url}")
            print(f"=============> Requests: {count}")
            print(f"=============> Descobertos: {descoberte}")

            response = requests.get(url)

            if response.status_code == 200:
                discover.append(url)
                print(f'======> Descoberto: [\e[92m{url}\e[0m]')
                descoberte = descoberte + 1
                with open('director_discovered.temp', 'a') as discovered_file:
                    discovered_file.write(f"{url}\n")

            count = count + 1
    print('Terminado..!!')

                    
def get_headers(target):

    target = target

    response = requests.head(target)
    
    headers = response.headers
    
    try:
        server = headers['Server']
    
        start_index = 0
        end_index = server.find(' ')
        
        web_server = server[start_index:end_index]
        if len(web_server) > 2:
            os.system(f'echo "==> Servidor: [\e[92m{web_server}\e[0m]"')
            if 'ngin' in web_server:
                print('')
                os.system('echo "\e[35mO Servidor Ngin eh mas usado em Ambiente Linux\e[0m"')
                os.system('echo "\e[35mEh provavel que o Sistem do alvo seja um Linux\e[0m"')
                print('')

        else:
            os.system(f'echo "==> Servidor: [\e[92mNão Detectado\e[0m]"')
        
        try:
            start_index = server.find('(')
            end_index = server.find(')')
            if start_index and end_index != -1:
                system = server[start_index + 1 :end_index]
                os.system(f'echo "==> Sistema:  [\e[92m{system}\e[0m]"')
            print('')
            print('[+] Deseja prosseguir para o Bruteforce?')
            print('[1]- SIM')
            print('[2]- NAO')
            print('')
            option = input('>>> ')

            if option == '1':
                
                bruteforce_director(target)
                
            else:
                pass
                
                
        except:
            print('')

    except:
        os.system(f'echo "==> Servidor: [\e[92mNão Detectado\e[0m]"')
        os.system(f'echo "==> Sistema: [\e[92mNão Detectado\e[0m]"')
        
        print('')
    
def initial_brute(target):

    try:
        response = requests.get(target)
    
        if response.status_code == 200:
            
            os.system('echo "==> ALVO: [\e[92mOnline\e[0m]"')
            #Iniciando ataque
            sleep(1.5)
            print('')
            os.system('echo "==> Iniciando [\e[92mAtaque!!\e[0m]"')
            sleep(1.5)
            os.system('clear')
            banner()
            os.system(f'echo "========================> ALVO: [\e[1;31m{target}\e[0m]"')
            os.system('echo "==> Detectando [\e[92mServidor\e[0m]"')
            os.system('echo "==> Detectando [\e[92mSistema\e[0m]"')
    
            print('==')
            print('==> Esse processo pode demorar um pouco...')
            print('')
            get_headers(target)
                

        elif response.status_code == 404:
            os.system('echo "==> ALVO: [\e[92mInvalido\e[0m]"')
        else:
            os.system('echo "==> Não foi possivel [\e[92mValidar\e[0m]"')
            
    except Exception as error:
        if 'failed to establish a new connection' in str(error).lower():
            os.system('echo "==> [\e[1;31mErro ao conectar\e[0m]"')
            os.system('echo "==> [\e[1;31mVerifique sua conexão a internet\e[0m]"')
            print('')
            
        elif 'No scheme supplied' in str(error):
                
            try:
                content_ = str(error).lower()
                    
                start_index = content_.find('http')
                end_index = content_.find('?')

                http = content_[start_index:-1]
                https = http.replace('http://','https://')
                print('==')
                os.system(f'echo "==>[\e[1;31mProtocolo não definido, tente:\e[0m \e[92m{http}\e[0m ou \e[92m{https}\e[0m"')
                print('')
                
                  
            except:
                os.system('echo "==> [\e[1;31mOcorreu um erro que não foi possivel determinar, tente novamente\e[0m]"')
        else:
            os.system('echo "==> [\e[1;31mOcorreu um erro que não foi possivel determinar, tente novamente\e[0m]"')
        
def main():
    try:
        banner()
        print('---|Exemplo de URL de dominio: https://google.com | https://governo.gov.ao')
        print('==')
        color_code = "\033[91m"  
        reset_code = "\033[0m"
        print(color_code + '[+]- Digite a URL do domínio do site: ' + reset_code, end='')
        domain = input('')
        print('')
        initial_brute(domain)
    except:
         os.system('echo "==> [\e[1;31mOcorreu um erro que não foi possivel determinar, tente novamente e verifique a URL\e[0m]"')
        
        
        

main()