# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-18.04"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update

    sudo apt-get -y install apache2 apache2-utils ssl-cert
    sudo apt-get -y install libapache2-mod-wsgi-py3

    sudo cp /vagrant/files/localhost.conf /etc/apache2/sites-available/localhost.conf

    sudo a2ensite localhost.conf
    sudo systemctl reload apache2
    sudo apt-get -y install default-libmysqlclient-dev

    sudo apt-get -y install python3-pip

    python3 -m pip install -r /vagrant/requirements.txt

    debconf-set-selections <<< 'mysql-server mysql-server/root_password password MySuperPassword'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password MySuperPassword'
    sudo apt-get -y install mysql-server

    mysql -uroot -pMySuperPassword -e "CREATE DATABASE hat CHARACTER SET utf8;"
    mysql -uroot -pMySuperPassword -e "CREATE USER 'dev_user'@'localhost' IDENTIFIED BY 'password';"
    mysql -uroot -pMySuperPassword -e "GRANT ALL PRIVILEGES ON * . * TO 'dev_user'@'localhost';"

    cd /vagrant/remotehat/
    python3 manage.py migrate
  SHELL

  config.vm.network :forwarded_port, guest: 80, host: 8080

end
