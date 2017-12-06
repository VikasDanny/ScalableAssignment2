import socket, pickle       


def authentication():
    input1 = raw_input("Enter 1 to login, 2 to sign up: ")
    socket_authen.send(input1.encode())
    username = raw_input("Enter username: ")
    socket_authen.send(username.encode())
    password = raw_input("Enter password: ")
    socket_authen.send(password.encode())
    print(username, password, input1)
    
    
    
    val = (socket_authen.recv(1024)).decode()
    if val == 'true':
        directory()
    elif val == 'false':
        print 'Incorrect password'
        authentication()
    else:
        print 'Username already exists'
        authentication()
        
 def directory():    
    inp = raw_input('Type 1 to create a new file, and 2 to access existing file ')
    if inp == '1':
        f_name = raw_input('enter file name ')        
        info = raw_input('Write data into file: ')
        socket_dir.send(f_name.encode())
        socket_dir.send(info.encode())
        
        data = socket_dir.recv(2048)
        files = pickle.loads(data)
        directory()
    else:
        file_name = raw_input("Enter File Name, type exit to terminate: ")
        socket_dir.send(file_name.encode())    
        data = socket_dir.recv(2048)
        data1 = data.decode()
        print data1

if __name__ == '__main__':
   
    host = 'localhost'
    port_dir = 5001
    socket_dir = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_dir.connect((host, port_dir))

    socket_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
    port_file = 5003              
    socket_file.connect((host, port_file))

    port_lock = 6002
    socket_lock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_lock.connect((host, port_lock))
