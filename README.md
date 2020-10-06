### 1. Install required packages
```
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools nginx supervisor
sudo apt install python3-venv
```

### 2. Clone Code repo
```
git clone https://github.com/faizan170/flask-app
mv flask-app testapp
cd testapp
python3 -m venv myprojectenv
source myprojectenv/bin/activate
pip install flask gunicorn werkzeug
```

### 3. Create Supervisor File
```
sudo nano /etc/supervisor/conf.d/hello_world.conf
```
And paste following code
```
[program:hello_world]
directory=/root/testapp
command=/root/testapp/myprojectenv/bin/gunicorn app:app -b localhost:8000
autostart=true
autorestart=true
```
Then run these commands
```
sudo supervisorctl reread
sudo service supervisor restart
```
To check status run
```
sudo supervisorctl status
```

### 4. Configure Nginx
Create a config file using
```
sudo vim /etc/nginx/conf.d/virtual.conf
```
And paste following code. Change IP with your machine IP
```
server {
    listen       80;
    server_name  149.28.226.39;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
Check status and restart nginx
```
sudo nginx -t
sudo service nginx restart
```
Now go to
```
http://YOUR_IP
```