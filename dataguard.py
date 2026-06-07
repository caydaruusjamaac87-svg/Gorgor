import time

def get_data_usage():
    try:
        with open('/proc/net/dev', 'r') as f:
            lines = f.readlines()
            total = 0
            for line in lines[2:]:
                data = line.split()
                # Tani waxay soo ururinaysaa xogta interfaces-ka oo dhan
                total += int(data[1]) + int(data[9])
            return total
    except:
        return 0

start = get_data_usage()
print("--- Kursi Data Guard wuu shaqaynayaa ---")

try:
    while True:
        current = get_data_usage()
        used = (current - start) / (1024 * 1024)
        print(f"Xogta la isticmaalay: {used:.2f} MB", end='\r')
        time.sleep(5)
except KeyboardInterrupt:
    print("\nJoojiyay.")


