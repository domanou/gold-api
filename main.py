import requests

def get_gold(start_date: str, end_date: str):
    url = f"https://api.nbp.pl/api/cenyzlota/{start_date}/{end_date}?format=json"
    response = requests.get(url)
    gold_prices = response.json()
    return gold_prices

if __name__ == "__main__":
    output = get_gold("2021-04-07", "2021-04-08")
    print(output)