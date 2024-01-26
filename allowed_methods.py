import subprocess

url = "http://example.com"
methods = ["OPTIONS", "GET", "HEAD", "POST", "DELETE", "TRACE", "PROPFIND", "PROPPATCH", "COPY", "MOVE", "LOCK", "UNLOCK", "PUT"]

for method in methods:
    modified_command = f"curl -I -X {method} {url}"
    print(f"Executing: {modified_command}")

    try:
        result = subprocess.run(modified_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        response_lines = result.stdout.splitlines()
        http_code = next((line.split()[1] for line in response_lines if line.startswith("HTTP")), None)

        if http_code == "200":
            print(f"Response for {method}: {http_code} OK")
        else:
            print(f"Response for {method}: {http_code}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error executing {modified_command}: {e}")
    
    print("-------------------------")
