from app import create_app
from flask_script import Manager,Server
from app import db
from app.models import User
from app.models import Role
from app.models import Review
from flask_migrate import Migrate, MigrateCommand


# Creating app instance
# app = create_app('development') # good for local development <<activate or uncoment on devpmt>>
app = create_app('production') # good for local production << deactivate or comment when on development mode>>


manager = Manager(app)
manager.add_command('server',Server)

# initialize migrate class that has been imported
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,
                 Role=Role,Review=Review)

# from app.main import app

if __name__ == '__main__':
    # app.run()
    manager.run()















    