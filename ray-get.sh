#!/usr/bin/bash
# RAY-GET 1.0
#Desenvolvedor: Caleb Marcelino (Mr Code)
#Facebook: Caleb Marcelino
#link: https://www.facebook.com/caleb.marcelino.16144
#Essa ferramenta foi desenvolvida para proposito educacional e de conhecimento
#Nao me responsabilizo com o jeito que sera usada essa ferramenta
#Cada um usa o seu conhecimento do jeito que achar melhor

function banner(){  bash ./www/bi/banner.sh 

}

function setup(){

    default="1"
    
    if [ -f "./lang.txt" ]; then
        #O arquivo existe
        default="0"
    else
        # O arquivo nao existe 
        default="1"
    fi

    if [ "$default" = "1" ]
    then
        banner
        echo "[1]- Português"
        echo "[2]- Inglês"
        echo -e "\n"
        read -p "opção>>> " lang
    
        if [ "$lang" = "1" ]; then
            lang="portugues"
            echo "portugues" > lang.txt
        elif [ "$lang" = "2" ]; then
            lang="ingles"
            echo ""
            echo "A versão em inglês do RAY-GET não foi finalizada"
            echo ""
    
            sleep 6.2
            main
        fi
    else
        main
fi
    
}

function osint(){

    banner

    python3 ./scripts_osint/osint_profile_facebook.py
    
    wait
}


function bruteforceDirector(){

    banner
    python3 ./bruteforce/bruteforce_director.py

    wait

    read -p "script bash..."
    main
}

function socialEngenering(){

    banner

}

function site_cloner(){

    python3 ./cloning/clone.py

    wait
    
    echo -e '\e[1;35m-------SITE CLONA-------\e[0m'
    read option

    

}

function main(){

    banner

    if [ "$default" = "0" ];
    then
        lang=$(< 'lang.txt')
    fi

    if [ "$lang" = "portugues" ];
    then
        cat ./languages/menu_pt.txt
        echo -e "\n"


    elif [ "$lang" = "ingles" ];
    then
        cat ./languages/menu_en.txt
        echo -e "\n"

    fi

    read -p "option>>> " option

    if [ "$option" = "1" ];
    then
        osint
        
    elif [ "$option" = "2" ];
    then
        bruteforceDirector
        
    elif [ "$option" = "3" ];
    then
        site_cloner
        
    else
        echo "Sessão finalizada! Volte embreve..."
    fi
    
}


setup