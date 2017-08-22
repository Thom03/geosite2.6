# # {{ project_name }} - GEOSITES ON GEONODE2.6 README

=========================================================

Installation
------------

Install geonode with::
To create a new project using geosites-project as a template, follow the steps below to set up a virtual environment, install GeoNode, and create a GeoSites project.  In the examples below project_name is a unique name for your project and example.org is the domain for the GeoNode sites.

    $ sudo add-apt-repository ppa:geonode/stable

    $ sudo apt-get update

    $ sudo apt-get install geonode

    
    $ django-admin startproject project_name --template=https://github.com/Thom03/geosite2.6/archive/master.zip -epu,rst,yml


    $ cd project_name
    
    $ bash ./setup.sh example.org


.. note:: You should NOT use the name geonode for your project as it will conflict with the default geonode package name.


### GeoServer

A single GeoServer instance is used to serve data to all of the GeoSites.  Install GeoServer as normal for GeoNode either on the same machine or a different one. Each site will proxy the /geoserver URL to the address of GeoServer (see the nginx configuration files). However, The default GeoNode installation sets the URL of the GeoNode site in one of the GeoServer config files: Edit the *GEOSERVER_DATA_DIR/security/auth/geonodeAuthProvider/config.xml* by changing the baseUrl field to an empty string:

	<baseUrl></baseUrl>

When baseUrl is empty, GeoServer will attempt to authenticate against the requesting URL.  Since a reverse proxy to GeoServer is configured on the web servers the requesting URL can be used to determine the URL to GeoNode. In fact, setting baseUrl to an empty string will work on a non GeoSites implementation of GeoNode as well, since a proxy is configured by default for a regular GeoNode project as well.

## GeoSites Project

After installing you will have a directory of files for your project. A GeoSites project looks similar to a normal GeoNode project, but with additional folders and settings files for sites

~~~
geosites-project
├── project_name
│   ├── __init__.py
│   ├── local_settings.py
│   ├── master
│   │   ├── conf
│   │   │   ├── gunicorn
│   │   │   └── nginx
│   │   ├── __init__.py
│   │   ├── local_settings.py
│   │   ├── settings.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── site_base.css
│   │   │   ├── img
│   │   │   │   └── README
│   │   │   ├── js
│   │   │   │   └── README
│   │   │   └── README
│   │   ├── templates
│   │   │   ├── site_base.html
│   │   │   ├── site_index.html
│   │   └── wsgi.py
│   ├── post_settings.py
│   ├── pre_settings.py
│   ├── sites.json
│   └── urls.py
├── manage_all.py
├── manage.py
├── README.rst
├── setup.py
└── setup.sh
~~~

Naviage to /etc/apache2/site-available/ to copy conf file for geonode for your master site

    sudo cp geonode.conf  master.geonode.conf

Edit the file /etc/apache2/sites-available/master.geonode.conf and change the following directive from:

    WSGIScriptAlias / /var/www/geonode/wsgi/geonode.wsgi

to:

    WSGIScriptAlias / /path/to/my_geonode/my_geonode/wsgi.py
    


Add the "Directory" directive for your folder like the following example:

    <Directory "/home/vagrant/my_geonode/my_geonode/">

       Order allow,deny

       Options Indexes FollowSymLinks

       Allow from all

       Require all granted

       IndexOptions FancyIndexing
       
    </Directory>

Restart apache::

    $ sudo service apache2 restart

Edit the templates in my_geonode/templates, the css and images to match your needs.

In the my_geonode folder run::

    $ python manage.py collectstatic
    
    
Edit hosts file:
    
    $ sudo nano /etc/hosts
    
Add the url of your master:    


Site 2
-----
Copy  and rename the site template from geosites and  put it at the directory of your project
where master is located.
 
 Add the site manually through the admin panel. And carefully write 
 the Site id. This site Id you will use it later during settings.py edits.

Edit setting.py by setting the following variables:
        
        SITE_ID = 
        SITE_NAME = 'site2'

Raname local_setting_sample.py to local_setting.py and set the following 
variables:

            SITEURL = 'http://$DOMAIN'
            
            example: SITEURL = 'http://site2.geonode.org'
            
            
Naviage to /etc/apache2/site-available/ to copy conf file for geonode for your master site

    sudo cp master.geonode.conf  site2.geonode.conf

Edit the file /etc/apache2/sites-available/site2.geonode.conf and change the following directive from:

    
    
from:

    WSGIScriptAlias / /path/to/my_geonode/my_geonode/wsgi.py  
 
to

    WSGIScriptAlias / /path/to/my_geonode/site2/wsgi.py  

Edit  the "Directory" directive for your folder like the following example:

from:
 <Directory "/home/vagrant/my_geonode/my_geonode/">

       Order allow,deny

       Options Indexes FollowSymLinks

       Allow from all

       Require all granted

       IndexOptions FancyIndexing
       
    </Directory>
    
 to:
    
     <Directory "/home/vagrant/my_geonode/site2/">

       Order allow,deny

       Options Indexes FollowSymLinks

       Allow from all

       Require all granted

       IndexOptions FancyIndexing
       
    </Directory>
    
To achieve creating  a virtualhost in the webserver related to the new created site. Remember to setup the WSGIDeamonProcess with the name you gave to the folder created at point 1. and the path to the geosites directory. WSGIProcessGroup
have to be pointed to the name you choose for the folder you created at point 1.
Eventually, WSGIScriptAlias have to be set to the wsgi.py you have in your site folder.   
    
 Restart apache::

    $ sudo service apache2 restart   
    
 Edit hosts file:
    
    $ sudo nano /etc/hosts
    
Add the url of your site2:    
