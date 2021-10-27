## Implementing nginx as a loadbalancer


### 1.Create a `.conf` file under `/etc/nginx/conf.d/`

### 2. Remove default file from `/etc/nginx/sites-enabled/`

### 3. Reload nginx server  
   
      ` sudo systemctl reload nginx ` 

### 4. run pyhton web apps

   * app1.py  
   * app2.py
   * app3.py

### 5.Check loadbalancing on browser