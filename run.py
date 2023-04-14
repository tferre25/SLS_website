
from flaskblog import create_app #in --init.py

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
