from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def index():
    return send_from_directory('.', 'jumpgame.html')


@app.route('/<path:filename>')
def static_files(filename):
    # Basic safety check
    if '..' in filename or filename.startswith('/'):
        abort(404)
    return send_from_directory('.', filename)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
