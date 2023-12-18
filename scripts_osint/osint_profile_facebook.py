#!/usr/bin/python3
#Desenvolvedor: Caleb Marcelino (Mr Code)
#idd: Cientista de computação (Hacker)
# Esse script é responsavel por executar o modulo facebook osint da ferramenta RAY-GET

import os
import requests
import mechanize
from time import sleep
from bs4 import BeautifulSoup

def facebook_osint(target):
    target = target
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
    )]
    
    try:
        print('')
        os.system('echo "[+]========> \e[35mEscaneando o perfil\e[0m"')
        response = br.open(target)
        sleep(0.5)
        response_content = response.read().decode('utf-8')
        soup = BeautifulSoup(response_content,'html.parser')
        
        title = soup.title
        html = soup.prettify()
        with open('http_facebook.html','w') as archive:
            archive.write(html)
    
    except Exception as error:
        os.system(f'echo "Ocorreu um erro: > \e[1;31m{str(error)}\e[0m"')
    
    try:
        soup = BeautifulSoup(response_content,'html.parser')
    
        title = soup.title
    
        profile_name = title.text.replace('| Facebook','')
        print("")
        if profile_name:
            if 'Iniciar' in profile_name:
                os.system(f'echo "[+]- Nome do perfil: \e[1;31m Nao detectado, perfil privado\e[0m"')
            else:
                
                os.system(f'echo "[+]- Nome do perfil: \e[92m {profile_name} \e[0m"')
        else:
            os.system(f'echo "[+]- Nome do perfil: \e[1;31m Nao detectado\e[0m"')
    except:
        os.system(f'echo "[+]- Nome do perfil: \e[1;31m Nao detectado\e[0m"')
        
    try:
        nikname = soup.find('span',class_="alternate_name")
        nikname = nikname.text
        nikname = nikname.replace('(','')
        nikname = nikname.replace(')','')
        
        if nikname:
            os.system(f'echo "[+]- Alcunha: \e[92m{nikname}\e[0m"')
        else:
            os.system(f'echo "[+]- Alcunha: \e[92m Nao detectado\e[0m"')
    except:
        os.system(f'echo "[+]- Alcunha: \e[1;31m Nao detectado\e[0m"')
        
    try:     
        work = soup.find('span',class_="_52jc _52ja")
        work = work.text
        
        if work:
            os.system(f'echo "[+]- Idd: \e[92m{work}\e[0m"')
        else:
            os.system(f'echo "[+]- Idd: \e[1;31m Nao detectado\e[0m"')
    except:
        os.system(f'echo "[+]- Idd: \e[1;31m Nao detectado\e[0m"')


    a_information = soup.find_all('a',class_='_4e81')

    if a_information:
        for i in a_information:
            data = i.text
            if data:
                os.system(f'echo "[+]- Idd: \e[92m{data}\e[0m"')
        
    div = soup.find_all('div',class_='_5xu4')
        
    #Obtendo a cidade do perfil

    try:
        content = str(div[2])
        
        start_index = content.find('<h4>')
        end_index = content.find('</h4>')
        
        city = content[start_index + len('<h4>'):end_index]
        
        if city:
            os.system(f'echo "[+]- Cidade atual: \e[92m{city}\e[0m"')
        else:
            os.system(f'echo "[+]- Cidade atual: \e[92m Nao detectado\e[0m"')
    except:
         os.system(f'echo "[+]- Cidade atual: \e[1;31m Nao detectado\e[0m"')
    print('')
    print('=== BAIXANDO A IMAGEM DO PERFIL ===')
    print('')

    try:
        img = soup.find('img', class_="profpic img")
        src_img = img['src']
    
        response = requests.get(src_img)
        print(response.status_code)
        if response.status_code == 200:
            try:
                os.system('rm imagem_do_perfil.jpg')
            except:
                pass
        
            try:
                with open('imagem_do_perfil.jpg', 'wb') as archive:
                    archive.write(response.content)
                    print('Imagem salva... nome: imagem_do_perfil.jpg')
            except Exception as e:
                print(f'Erro ao salvar a imagem: {e}')
        else:
            print('Não foi possivel acessar a imagem do perfil')
            print('Parece que a imagem de perfil é privada ou não pode ser acessada por fontes desconhecia')
        
    except:
        print('Nao foi possivel baixar a imagem:')
    print('')
    print('Tenha em mente que você está usando a versão 1.0 do RAY-GET')
    print('É possivel que você nem sempre obtenha bons resultados')
    print('Recomendo usar a versão premium do RAY-GET')
    print('')
    print('000- Caso não consiga o premium Você pode efetuar um Osint mas profundo manualmente -000')
    print('')
       
def main():

    pause = True

    while pause:

        os.system('bash ./www/bi/banner.sh ')
        os.system('echo "=============> FACEBOOK OSINT [\e[92mHabilitado\e[0m]"')
        print('')
        
        target = input('Digite a url do perfil: ')
        
        if (len(target) < 10 or 'facebook' not in target or 'https' not in target or '//' not in target):
            print("")
            os.system(f'echo "|==> [+]-\e[1;31m URL INVALIDA [+]\e[0m <==|"')
            sleep(2.5)

        else:
            pause = False

    facebook_osint(target)
          
    

main()