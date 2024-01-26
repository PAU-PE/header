#!/bin/bash

url="http://example.com"
methods=("OPTIONS" "GET" "HEAD" "POST" "DELETE" "TRACE" "PROPFIND" "PROPPATCH" "COPY" "MOVE" "LOCK" "UNLOCK" "PUT")

for method in "${methods[@]}"; do
    modified_command="curl -I -X $method $url"
    echo "Executing: $modified_command"
    
    response=$(eval $modified_command 2>&1)
    http_code=$(echo "$response" | grep -i "^HTTP" | awk '{print $2}')
    
    if [ "$http_code" == "200" ]; then
        echo "Response for $method: $http_code OK"
    else
        echo "Response for $method: $http_code"
    fi
    
    echo "-------------------------"
done
