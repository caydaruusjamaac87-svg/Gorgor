#!/data/data/com.termux/files/usr/bin/bash

# Faylka kormeerka
FILE="/data/data/com.termux/files/home/scan_results.txt"
OLD_FILE="/data/data/com.termux/files/home/old_scan.txt"
SENT=false 

# Waxaad token-kaaga ku kaydisaa faylka .env ee aan GitHub gelin
# Si aad tan u isticmaasho, ku qor "source .env" ka hor inta aanad script-kan socodsiin
# ama ku qor variable-kan halkan laakiin xusuusnow inaad tirtirto ka hor inta aanad GitHub gelin

BOT_TOKEN="Halkan_ku_dhig_furahaaga_cusub"
CHAT_ID="7004346809"

while true; do
    nmap -p 8080 localhost > "$FILE"
    
    if grep -q "open" "$FILE"; then
        if [ "$SENT" = false ]; then
            # Halkan ayaan ku isticmaalaynaa variable-ka beddelka furaha
            curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage?chat_id=$CHAT_ID&text=Digniin: Dekedda 8080 waa la helay!"
            SENT=true
            pkill -f "python -m http.server"
        fi
    else
        SENT=false
    fi
    sleep 5
done


