from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the root route
@app.route('/')
def serve_index():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Serve the HTML file from the same directory
    return send_from_directory(script_dir, 'index.html')

if __name__ == '__main__':
    # Start the Flask web server
    app.run(host='20.208.5.36', port=8080)
