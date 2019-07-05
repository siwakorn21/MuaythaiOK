import requests

def main():
    res = requests.get("http://api.fixer.io/latest?base=USD&symbols=EUR")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.jason()
    rate = data["rates"]["EUR"]
    print(rate)

if __name__ == "__main__":
    main()
