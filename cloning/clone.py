#!/usr/bin/python3
#Desenvolvedor: Caleb Marcelino (Mr Code)
#Esse script eh um modulo da ferramenta RAY-GET responsavel por clonar paginas da web

import requests
import os

def clone_site(url):

    response = requests.get(url)

    if response.status_code == 200:
        os.system('echo "==> SITE: [\e[92mValidado\e[0m]"')
        print('=====> Clonando site <====')

        try:
            with open('site_clonado.html','w') as archive:
                archive.write(response.text)
                os.system('echo "==> SITE: [\e[92mClonado\e[0m]"')
                os.system('echo "Abra o arquivo: [\e[92msite_clonado.html\e[0m] no navegador"')
                
                print('para nao perder esse site clonado quando executar novamente a ferramenta deseja dar um nome proprio?')
                print('')
                only_name = input('[1]- Sim \n[2]- Nao \n>>: ')

                if only_name.strip().lower() == "1" or 's' in only_name:
                    new_name = input('Digite o novo nome do arquivo: ')

                    if len(new_name) < 2:
                        print('')
                        print('Nome invalido, o arquivo nao foi renomeado')
                    else:
                        os.system(f'mv site_clonado.html "{new_name}.html"')
                        os.system('echo "|=======> \e[92mNome alterado com sucesso!\e[0m"')

                else:
            
                    print('')
        except:
            os.system('echo "==> SITE: [\e[1;31mNao clonado\e[0m]"')
            
    else:
        os.system('echo "==> SITE: [\e[92mNao acessivel\e[0m]"')
        os.system('echo "==> SITE: [\e[92mNao Clonado\e[0m]"')


def main():

    os.system('bash ./www/bi/banner.sh')
    print('')
    os.system('echo "=============> WEB SITE CLONER [\e[92mHabilitado\e[0m]"')
    print('')
    url = input('Digite a url do site: ')

    clone_site(url)


main()