import os
from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

@app.route("/<path:name>")
def get_page(name):
    """
    core logic: 
    If file exists, return it. Else, trigger error handler.
    """
    if ".." in name or "~" in name or "//" in name:
        abort(403)

    # Looking for files in the 'pages' directory
    pages_dir = "pages"
    file_path = os.path.join(pages_dir, name)

    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_from_directory(pages_dir, name), 200
    else:
        # Triggering the 404 handler
        abort(404)

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def error_403(e):
    return render_template('403.html'), 403

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)