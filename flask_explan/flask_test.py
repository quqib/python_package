from flask import Flask
from flask_socketio import SocketIO, disconnect
from flask import request

app = Flask(__name__)

# 允许所有CORS
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('connect')
def handle_connect():
    print('客户端尝试连接...')
    print(f'来源: {request.origin}')
    print(f'客户端信息: {request.sid}')

    # 方法A：立即断开连接（不会导致服务器错误）
    disconnect()
    return  # 不返回False

    # 或者方法B：延迟断开
    # socketio.emit('error', {'message': '连接被拒绝'}, room=request.sid)
    # disconnect(request.sid)


@socketio.on('message')
def handle_message(data):
    print('收到消息:', data)


if __name__ == '__main__':
    print('启动服务器...')
    print('服务器会接受连接但立即断开')
    socketio.run(app, host='0.0.0.0', port=12345, debug=True, allow_unsafe_werkzeug=True)