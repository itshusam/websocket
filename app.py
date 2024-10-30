from web_socket import WebSocketServer, socketio, app

message_storage = {}

app = WebSocketServer().create_app()

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
 
    user = data.get('user')
    message = data.get('message')
    
    print(f'Received message from {user}: {message}')
    
  
    if user not in message_storage:
        message_storage[user] = []  
    message_storage[user].append(message)


    socketio.emit('message', {'user': user, 'message': message})

@socketio.on('get_all_messages')
def get_all_messages(user):
   
    messages = message_storage.get(user, [])
    socketio.emit('all_messages', {'user': user, 'messages': messages})

if __name__ == '__main__':
    socketio.run(app)
