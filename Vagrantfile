# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update

    sudo apt-get -y install apache2 apache2-utils ssl-cert
    sudo apt-get -y install libapache2-mod-wsgi-py3
  SHELL

  config.vm.network :forwarded_port, guest: 80, host: 8080

  config.vm.provider "virtualbox" do |vb|
    # disable generating ubuntu-bionic-18.04-cloudimg-console.log file in the shared folder
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end
end
