
from app import create_app
from app import db
from app.models import User

# Creating app instance
app = create_app('development')

@app.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )


if __name__ == '__main__':
    app.run()
    
    
    