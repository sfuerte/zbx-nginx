# zbx-nginx

Zabbix Template for Nginx statistics. The script is written in Python.

![Request Statistics](https://github.com/sfuerte/zbx-nginx/blob/master/images/zbx_nginx-request_stats.png)
![Connection Statistics](https://github.com/sfuerte/zbx-nginx/blob/master/images/zbx_nginx-conn_status.png)

## System requirements

- [python](http://www.python.org/downloads/) >= 2.7.9 (e.g. Debian 8 or higher)

- [nginx](http://nginx.org/) with configured `http_stub_status_module`

## Features

- HTTP/HTTPS support
- Connection Statistics:
  - Active
  - Reading
  - Waiting
  - Writing
- Request Statistics:
  - Accepted
  - Handled
  - Total
- 'Requests Statistics' graph
- 'Connection Status' graph
- Screen combining both graphs
- Version information
- `{$NGINX_HOST}` and `{$NGINX_PORT}` macros for customization

## Installation

### Nginx Configuration

Add the following to your default vhost configuration file:

```conf
    location /nginx_status {
        stub_status on;
        access_log   off;
        allow 127.0.0.1;
        deny all;
    }
```

### Zabbix Configuration

1) Copy `userparameter_nginx.conf` to `/etc/zabbix/zabbix_agentd.d` folder (or whatever is default and/or configured on your system).

1) Copy `nginx-stat.py` to `/etc/zabbix/zabbix_agentd.scripts` folder.
IMPORTANT: if you use another folder for agent scripts, then update userparameter file in the previous step!

1) Import XML template file (`zbx_template_nginx.xml`) into Zabbix via Web GUI (Configuration -> Templates -> Import).

1) Assign the imported template to a host and enjoy!

## Troubleshooting

A simple run of the script from a console should give just one number in return, for example:

```shell
> /etc/zabbix/zabbix_agentd.scripts/nginx-stat.py -h localhost -p 443 -a active
14
```
