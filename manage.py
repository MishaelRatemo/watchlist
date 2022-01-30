
from app import create_app
# from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

# manager = Manager(app)
# manager.add_command('server',Server)

# from app.main import app

if __name__ == '__main__':
    # app.run()
    app.run()
