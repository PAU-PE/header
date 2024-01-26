#!/bin/bash

url="https://www.tesla.com/"
methods=("OPTIONS" "GET" "HEAD" "POST" "DELETE" "TRACE" "PROPFIND" "PROPPATCH" "COPY" "MOVE" "LOCK" "UNLOCK" "PUT")

for method in "${methods[@]}"; do
    response=$(curl -X "$method" -s -o /dev/null -w "%{http_code}" --location "$url")

    if [ "$response" -eq 200 ]; then
        echo "Response for $method: $response OK"
    else
        echo "Response for $method: $response"
    fi

    echo "-------------------------"
done

