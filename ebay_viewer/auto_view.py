import requests
import random

def get_proxy():
    """Returns a random proxy from the list of proxies."""
    with open("proxies.txt", "r") as f:
        proxies = f.readlines()
    proxy = random.choice(proxies).strip()
    return proxy

def open_product_page(url, proxy):
    """Opens the product page with the given URL and proxy."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, proxies={"http": proxy})
        if response.status_code == 200:
            print("Product page opened successfully with proxy:", proxy)
        else:
            print("Failed to open product page with proxy:", proxy)
    except requests.exceptions.RequestException as e:
        print("Error while opening the product page with proxy:", proxy)
        print("Exception:", e)

if __name__ == "__main__":
    url = input("enter item url")
    for _ in range(250):
        proxy = get_proxy()
        open_product_page(url, proxy)
