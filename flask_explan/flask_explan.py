# app.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

# 初始化 SocketIO（即使不用也可保留）
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.get_json() or {}
    print(f"[{time.strftime('%H:%M:%S')}] 收到插件心跳:", data)
    return jsonify({
        "status": "ok",
        "server_time": time.time(),
        "message": "收到心跳"
    })

# 如果你仍想用 SocketIO，也可以保留，但插件用 HTTP 更简单
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=15119, debug=True, allow_unsafe_werkzeug=True)

