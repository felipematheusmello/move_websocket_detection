from flask import Flask
from flask_socketio import SocketIO
import pyautogui
import json

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('valueChange')
def handle_change_postion(data):
    try:
        if data:
            position = json.loads(data)
            if position:
                x = position.get('x', 0)
                y = position.get('y', 0)

                current_x, current_y = pyautogui.position()

                new_x = min(max(current_x + int(x) * -15, 0), pyautogui.size().width - 1)
                new_y = min(max(current_y + int(y) * -15, 0), pyautogui.size().height - 1)


                pyautogui.moveTo(new_x, new_y, 0.1)

    except Exception as e:
        print(f"Error processing data: {e}")

@socketio.on('click')
def handle_on_click(data):
    try:
        if data == 'right':
            pyautogui.rightClick()

        if data == 'left':
            pyautogui.leftClick()

    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == '__main__':
    socketio.run(app)