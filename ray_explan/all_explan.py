"""
涉及多线程 多进程 多协程
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'this is test'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

