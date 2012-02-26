import os.path
from fabric.api import env, local, prompt


env.project_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
env.user_name = env.project_name
env.production = False
env.server_flavor = None


# ENVIRONMENTS

def staging():
    """Deploy on staging server"""
    env.branch = "develop"
    env.remote = "staging"

def production():
    """Deploy on live server"""
    env.production = True
    env.branch = "master"
    env.remote = "production"


# COMMANDS

def deploy():
    """Update code, migrate database and restart server."""
    if env.production:
        input = prompt('Are you sure you want to deploy to the production server?', default="n", validate=r'^[yYnN]$')
        if input not in ['y','Y']:
            exit()
    local("git push %(remote)s %(branch)s:master" % env)
    migrate()
    reload_server()

def migrate():
    """Sync and migrate the database."""
    local("heroku run python manage.py syncdb --remote %(remote)s" % env)
    local("heroku run python manage.py migrate --remote %(remote)s" % env)

def reload_server():
    """Reload the webserver and take the server flavor into account."""
    local("heroku restart --remote %(remote)s" % env)
