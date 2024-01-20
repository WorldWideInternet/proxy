from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['POST'])
def proxy():
    url = request.form.get('url', '')

    if not url:
        return jsonify({'error': 'Missing URL parameter'})

    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
