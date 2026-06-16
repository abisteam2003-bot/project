from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/get-links', methods=['GET'])
def get_whatsapp_links():
    try:
        # The message content and target numbers
        message = "Hi"
        numbers = ["919944246620", "917598957741"]
        
        # Build standard URL targets safely on the server side
        urls = [f"https://wa.me/{number}?text={encode_msg(message)}" for number in numbers]
        
        return jsonify({'status': 'success', 'links': urls})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def encode_msg(text):
    import urllib.parse
    return urllib.parse.quote(text)

if __name__ == '__main__':
    # Render passes an environmental variable named PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)