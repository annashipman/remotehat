# Remote Hat

Code to run a remote game of Hat.

## Testing

This project uses Vagrant. To test the application locally, `vagrant up` and it is running at [http://localhost:8080/hat](http://localhost:8080/hat). To run the tests, ssh to the box and `python3 /vagrant/remotehat/manage.py test hat`

## Deploying

At the moment, set up of the remote server is manual, and deployment only deploys the code under `/remote/hat` to the same place on the server. That means the database and the apache server all need to be set up prior to first deploy.

## Next steps

The next step here is to choose direction:

1. Harden what we have (when game is running, anyone can interfere)
2. Make it reusable – new game on spot instance, or maybe serverless?
3. Improve what we have (timer, harder to duplicate, new game, maybe team allocation, etc)

There is a philosophical design decision here about how self-contained it should be vs a crutch for a real life interaction (e.g scoring and timing offline).
