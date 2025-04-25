from flask import Flask, jsonify
import os
import socket
 
app = Flask(__name__)
 
# Function to get the pod IP
def get_pod_ip():
    return socket.gethostbyname(socket.gethostname())
 
# Function to get the node IP (from environment variable or fallback)
def get_node_ip():
    return os.environ.get('NODE_IP', 'Not available')
 
@app.route('/')
def home():
    pod_ip = get_pod_ip()
    node_ip = get_node_ip()
    return jsonify({
        'message': 'Welcome to the Simple REST API',
        'pod_ip': pod_ip,
        'node_ip': node_ip
    })
 
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)