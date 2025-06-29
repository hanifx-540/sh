import os
import time

folder = "/sdcard/hanifx"
os.makedirs(folder, exist_ok=True)

stop_flag = "/sdcard/hanifx_stop.flag"
count = 0

while True:
    if os.path.exists(stop_flag):
        print("[*] Stop flag detected. Exiting.")
        break

    filename = os.path.join(folder, f"hanifx_file_{count}.txt")
    try:
        with open(filename, "w") as f:
            f.write("X" * 1024 * 1024 * 5)  # 5 MB
        print(f"[+] Created: {filename}")
    except Exception as e:
        print(f"[!] Error: {e}")
        break

    count += 1
    time.sleep(1)
