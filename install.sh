#!/data/data/com.termux/files/usr/bin/bash

function explicação {
   apt install python -y
   if [ $? -eq 0 ]; then
       echo -e "[\e[32m√\e[0m] Instalado Com sucesso!\n\n"
       echo -e "A ferramenta fara uma varredura de ips próximos ira\nInvadir o mais proximo\n"
       read -p "Press enter para continuar"
       clear; python invade.py
   else
       echo -e "[\e[1;31mX\e[0m] ERRO CONECTION NOT FOUND!!'
       sleep 4
   fi
}

explicação
