from flask import Flask
from flask_socketio import SocketIO
import pyautogui
import json

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('valueChange')
def handle_change_postion(data):
    print('Received data' + data)
    try:
        # Assuming 'data' is a JSON string containing {x, y, z}
        position = json.loads(data)
        x = position.get('x', 0)
        y = position.get('y', 0)

         # Get the current mouse position
        current_x, current_y = pyautogui.position()
        print(f"Current position: ({current_x}, {current_y})")

        # Calculate the new position
        new_x = min(max(current_x + int(x), 0), pyautogui.size().width - 1)
        new_y = min(max(current_y + int(y), 0), pyautogui.size().height - 1)

        print(f"Moving mouse to: ({new_x}, {new_y})")

        # Move the mouse cursor to the new position
        pyautogui.moveTo(new_x, new_y)

        print(pyautogui.position())
    except Exception as e:
        print(f"Error processing data: {e}")

@socketio.on('click')
def handle_on_click(data):
    print('CLICKED________')
    try:
        if data == 'right':
            pyautogui.rightClick()

        if data == 'left':
            pyautogui.leftClick()

    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == '__main__':
    socketio.run(app)