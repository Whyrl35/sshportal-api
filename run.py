"""
Activate the venv first.
Then: `export FLASK_APP=run.p`
And: `flask run`
"""
from sshportal_api import app


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
