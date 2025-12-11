from appfleshi import app
from flask_bootstrap import Bootstrap

if __name__ == '__main__':
    app.run(debug=True)
    bootstrap = Bootstrap(app)