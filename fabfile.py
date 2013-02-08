from __future__ import with_statement
from fabric.api import *

prod_server = 'user@123.456.789' # your production (or staging) server's details

def prod():
    """ Use production server settings """
    env.hosts = [prod_server]
    env.directory = '/home/dir/to/webroot'
    env.activate = 'source /home/dir/to/venv/bin/activate'
    env.settings = 'your_app.settings' # where your_app is the name of your core Django app
    env.prefix = 'PRODUCTION=1' # set an environment var to tell django were on the production machine

def virtualenv(command):
    with cd(env.directory):
        run(env.activate + '&&' + command)

def git_pull():
    """Updates the repository."""
    with cd(env.directory):
        run('git pull origin master') # or whatever you use as your deployment branch

def restart_daemon():
    """Should restart the daemon in a Apache/mod_wsgi setup"""
    with cd(env.directory):
        run("touch your_app/wsgi.py") # where your_app is your core apps dir

def deploy():
    """Run the actual deployment steps: $ fab prod deploy"""
    local('git push')
    git_pull()
    virtualenv("pip install -r %s/requirements.txt" % env.directory)
    with prefix('export %s' % env.prefix):
        virtualenv("python manage.py syncdb --settings='%s' --noinput" % env.settings)
        virtualenv("python manage.py migrate --settings='%s' --noinput" % env.settings) # run South migrations
        virtualenv("python manage.py collectstatic --settings='%s' --noinput" % env.settings) # collect static files
        virtualenv("python manage.py compress --settings='%s'" % env.settings) # compress static files
    restart_daemon()