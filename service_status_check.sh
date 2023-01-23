#!/bin/bash

echo "Checking Service Status"

curl_https_url () {
    max_in_s=3
    delay_in_s=1
    total_in_s=0
    while [ $total_in_s -le "$max_in_s" ]
    do
        echo "Wait ${total_in_s}s"
        https_code=$(curl -s -o /dev/null -w "%{http_code}" https://${service_name}.dev.ma.halo-telekom.com/${service_name}-service)
        #https_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:${service_name})
        if [ $https_code != "200" ]
        then
            total_in_s=$(( total_in_s +  delay_in_s))
            sleep $delay_in_s
            echo "$service_name has not started, Please check the service log"
        else
            echo "$service_name has successfully started "
            break
            
        fi
       
    done
}

for service_name in $(cat build-summary.txt); do
curl_https_url $service_name 
done
