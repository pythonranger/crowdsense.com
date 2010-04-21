### -*- coding: utf-8 -*- ##

import os
from fabric.api import env

from saaskit.fabfile import ifnotsetted
from saaskit.fabfile import setup_production, update_production
from saaskit.fabfile import install_packages, mail_server_setup, log_setup
from saaskit.fabfile import github_setup, postgresql_setup, postgresql_user_db_flush
from saaskit.fabfile import webapp_setup, project_setup, update_webapp, build_webapp
from saaskit.fabfile import nginx_setup, apache2_setup, restart_webserver

env.SOURCE_PATH = 'src/crowdsense'
env.git_path = 'git@github.com:CrowdSense/crowdsense.com.git'

def production():
    #env.hosts = []
    
    ifnotsetted('host_string', 'crowdsense.com', True, 
        "No hosts found. Please specify (single) host string for connection")
    ifnotsetted('user', 'root', True, "Server user name")
    ifnotsetted('VPS_IP', '97.107.138.174', True, "VPS IP")
    ifnotsetted('POSTGRES_USER', 'crowdsense', True, "PostgreSQL user name")
    ifnotsetted('POSTGRES_PASSWORD', 'crowdsenseS3n89mkk', True, "PostgreSQL user's password")
    ifnotsetted('POSTGRES_DB', 'crowdsense', True, "PostgreSQL DATABASE")
    ifnotsetted('UBUNTU_VERSION', 'karmic', True, "Ubuntu version name")
    ifnotsetted('PAYPAL_EMAIL', 'admin_1255085897_biz@crowdsense.com', True, "PAYPAL EMAIL")
    ifnotsetted('PAYPAL_TEST', 'True', True, "PAYPAL TEST (True or False)?", r'^(True|False)$')
    
