sg() {
   #ACTULIZADOR
   
   [[ ! -e /etc/versin_script ]] && echo 1 >/etc/versin_script
   v11=$(cat /etc/versin_script_new)
   v22=$(cat /etc/versin_script)
   [[ $v11 = $v22 ]] && vesaoSCT="\033[1;37mVersion\033[1;32m $v22  \033[1;31m]" || vesaoSCT="\033[1;31m($v22)\033[1;97m→\033[1;32m($v11)\033[1;31m  ]"
   local colors="/etc/VPS-MX/colors"
   if [[ ! -e $colors ]]; then
      COLOR[0]='\033[1;37m' #BRAN='\033[1;37m'
      COLOR[1]='\e[31m'     #VERMELHO='\e[31m'
      COLOR[2]='\e[32m'     #VERDE='\e[32m'
      COLOR[3]='\e[33m'     #AMARELO='\e[33m'
      COLOR[4]='\e[34m'     #AZUL='\e[34m'
      COLOR[5]='\e[91m'     #MAGENTA='\e[35m'
      COLOR[6]='\033[1;97m' #MAG='\033[1;36m'
   else
      local COL=0
      for number in $(cat $colors); do
         case $number in
         1) COLOR[$COL]='\033[1;37m' ;;
         2) COLOR[$COL]='\e[31m' ;;
         3) COLOR[$COL]='\e[32m' ;;
         4) COLOR[$COL]='\e[33m' ;;
         5) COLOR[$COL]='\e[34m' ;;
         6) COLOR[$COL]='\e[35m' ;;
         7) COLOR[$COL]='\033[1;36m' ;;
         esac
         let COL++
      done
   fi
   NEGRITO='\e[1m'
   SEMCOR='\e[0m'
   case $1 in
   -ne) cor="${COLOR[1]}${NEGRITO}" && echo -ne "${cor}${2}${SEMCOR}" ;;
   -ama) cor="${COLOR[3]}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}" ;;
   -verm) cor="${COLOR[3]}${NEGRITO}[!] ${COLOR[1]}" && echo -e "${cor}${2}${SEMCOR}" ;;
   -verm2) cor="${COLOR[1]}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}" ;;
   -azu) cor="${COLOR[6]}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}" ;;
   -verd) cor="${COLOR[2]}${NEGRITO}" && echo -e "${cor}${2}${SEMCOR}" ;;
   -bra) cor="${COLOR[0]}${SEMCOR}" && echo -e "${cor}${2}${SEMCOR}" ;;
   "-bar2" | "-bar") cor="${COLOR[1]}————————————————————————————————————————————————————" && echo -e "${SEMCOR}${cor}${SEMCOR}" ;;
   -tit) echo -e "\e[97m \033[1;41m| #-#-► 🐲 SCRIPT VPS•MX ◄-#-# | \033[1;49m\033[1;49m \033[1;31m[ \033[1;32m $vesaoSCT " && echo -e "${SEMCOR}${cor}${SEMCOR}" ;;
   esac
}
