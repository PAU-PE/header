import requests

url = "https://www.tesla.com/"
methods = ["OPTIONS", "GET", "HEAD", "POST", "DELETE", "TRACE", "PROPFIND", "PROPPATCH", "COPY", "MOVE", "LOCK", "UNLOCK", "PUT"]

for method in methods:
    try:
        response = requests.request(method, url, allow_redirects=False)

        if response.status_code == 200:
            print(f"Response for {method}: {response.status_code} OK")
        else:
            print(f"Response for {method}: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error executing {method} request: {e}")

    print("-------------------------")
