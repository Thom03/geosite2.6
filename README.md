# # {{ project_name }} - GEOSITES ON GEONODE2.6 README

=========================================================

Installation
------------

Install geonode with::

    $ sudo add-apt-repository ppa:geonode/stable

    $ sudo apt-get update

    $ sudo apt-get install geonode

    
    $ django-admin startproject project_name --template=https://github.com/Thom03/geosite2.6/archive/master.zip -epu,rst,yml
    $ cd project_name
    
    $ bash ./setup.sh example.org


.. note:: You should NOT use the name geonode for your project as it will conflict with the default geonode package name.



Usage
-----

Rename the local_settings_sample.py to local_settings.py and edit it's content by setting the SITEURL, SITE_ID and SITENAME.

Master
-----
Master must have a SITE_ID of 1

In order to use geonode in Multi-tenancy mode, follow these steps:

check in settings.py if 'geonode.contrib.geosites' in GEONODE_CONTRIB_APPS is rightly uncommented
add in settings.py 'geonode.contrib.geosites' in INSTALLED_APPS
Setting.py of the master has to be modifies so that 'geonode.contrib.geosites' is 
activated since Geonode 2.6 geosites are included as Contrib Apps.
Copy the installed apps for installed   geonode and include them into settings.py 
and uncomment:

        'geonode.contrib.geosites'

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
