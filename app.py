from flask import Flask, jsonify
import os
import socket
from datetime import datetime
 
app = Flask(__name__)
 
# Function to get the pod IP
def get_pod_ip():
    return socket.gethostbyname(socket.gethostname())
 
# Function to get the node IP
def get_node_ip():
    return os.environ.get('NODE_IP', 'Node IP not set')
 
@app.route('/')
def display_ips():
    pod_ip = get_pod_ip()
    node_ip = get_node_ip()
    return jsonify({
        'pod_ip': pod_ip,
        'node_ip': node_ip,
        'message': f'Request served by Pod IP: {pod_ip} on Node IP: {node_ip}'
    })
 
@app.route('/datetime')
def get_datetime():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({
        'datetime': current_time
    })
 
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)