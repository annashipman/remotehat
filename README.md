# Remote Hat

Code to run a remote game of Hat.

## Testing

This project uses Vagrant. To test the application locally, `vagrant up` and it is running at [http://localhost:8080/hat](http://localhost:8080/hat). To run the tests, ssh to the box and `python3 /vagrant/remotehat/manage.py test hat`

## Deploying

At the moment, set up of the remote server is manual, and deployment only deploys the code under `/remote/hat` to the same place on the server. That means the database and the apache server all need to be set up prior to first deploy.
