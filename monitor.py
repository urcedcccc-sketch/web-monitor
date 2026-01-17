import requests
import hashlib
import os

# 1. 读取目标 URL
with open('url.txt', 'r') as f:
    target_url = f.read().strip()

# 2. 抓取并对比
def check():
    if not target_url: return
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(target_url, headers=headers, timeout=20)
        new_hash = hashlib.md5(response.text.encode('utf-8')).hexdigest()
        
        last_hash = ""
        if os.path.exists('last_hash.txt'):
            with open('last_hash.txt', 'r') as f:
                last_hash = f.read().strip()
        
        if new_hash != last_hash:
            with open('last_hash.txt', 'w') as f:
                f.write(new_hash)
            print("CHANGE_DETECTED")
            exit(10) # 触发变化信号
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check()
