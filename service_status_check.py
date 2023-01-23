# python script to iterate through a text file and call the shell script.

import os
from string import Template
home = os.getcwd()
build_summary_file = os.path.join(home,'build-summary.txt')
# read the text file
with open(build_summary_file) as f:
    lines = f.readlines()

sh_script = """
    curl_https_url () {
          max_in_s=$$1
          delay_in_s=1
          total_in_s=0
          while [ $$total_in_s -le "$$max_in_s" ]
          do
              echo $${$service}
              echo "Wait $${total_in_s}s"
              https_code=$$(curl -s -o /dev/null -w "%{http_code}" https://$${$service}.dev.ma.halo-telekom.com/$${$service}-service/)
                  echo $${http_code}
                  if [ $$https_code != "200" ]
                  then
                      total_in_s=$$(( total_in_s +  delay_in_s))
                       sleep $$delay_in_s
                  else
                      echo 'Service has successfully started '
                  total_in_s=$$(( $$1 + delay_in_s))      
            
            
                  fi
       
            done
            echo 'Service has not started, Please check the service log'
                        }

        curl_https_url 5
"""
t = Template(sh_script)

# to remove new line character from the file content
lines = [x.strip('\n') for x in lines]

# iterate over the file contents and pass the content to shell script 

for v in lines:
    p = t.substitute({'service':v})
    #print(p)
    os.system(p)
