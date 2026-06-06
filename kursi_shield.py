import datetime
import hashlib
import os
import time

def log_activity(data):
    if "tiktok.com" not in data:
        return
    hash_object = hashlib.sha256(data.encode())
    hex_dig = hash_object.hexdigest()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    log_file = f"kursi_logs_{date_str}.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] DATA: {data} | HASH: {hex_dig[:15]}...\n"
    with open(log_file, "a") as f:
        f.write(log_entry)
    print(f"La diiwaangeliyay: {hex_dig[:10]}...")

print("--- Kursi Digital Shield (100% Pro Edition) ---")
last_copied = ""

try:
    while True:
        # Isticmaalka amarka tooska ah ee Termux
        result = os.popen('termux-clipboard-get').read().strip()
        if result != last_copied and "tiktok.com" in result:
            print(f"\nLink cusub: {result}")
            log_activity(result)
            last_copied = result
        time.sleep(2) # Wuxuu hubinayaa 2-dii ilbiriqsi kasta
except KeyboardInterrupt:
    print("\n--- Kursi Digital Shield waa la joojiyay ---")


