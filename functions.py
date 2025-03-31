from jinja2 import Environment, FileSystemLoader
import os
from functools import wraps
from flask import request, Response

def render_template(templatePath,**kwargs):
    env = Environment(loader=FileSystemLoader('.'))
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    
    template = env.get_template(templatePath)
    return template.render(**kwargs)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == 'admin' and auth.password == 'admin'):
            return Response('Could not verify your access level for that URL.\n'
                            'You have to login with proper credentials', 401,
                            {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)

    return decorated