# DiscoLib
Discord bot library 

## Error
```
  File "test.py", line 5, in <module>
    connection.run()
  File "/home/pi/git/discodip/src/discord/discord.py", line 41, in run
    self._connection.update()
  File "/home/pi/git/discodip/src/discord/connection.py", line 58, in update
    data = self.socket.recv()
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_core.py", line 300, in recv
    opcode, data = self.recv_data()
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_core.py", line 317, in recv_data
    opcode, frame = self.recv_data_frame(control_frame)
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_core.py", line 330, in recv_data_frame
    frame = self.recv_frame()
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_core.py", line 364, in recv_frame
    return self.frame_buffer.recv_frame()
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_abnf.py", line 361, in recv_frame
    self.recv_header()
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_abnf.py", line 309, in recv_header
    header = self.recv_strict(2)
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_abnf.py", line 396, in recv_strict
    bytes_ = self.recv(min(16384, shortage))
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_core.py", line 434, in _recv
    return recv(self.sock, bufsize)
  File "/home/pi/.local/lib/python3.5/site-packages/websocket/_socket.py", line 94, in recv
    "Connection is already closed.")
websocket._exceptions.WebSocketConnectionClosedException: Connection is already closed.
```