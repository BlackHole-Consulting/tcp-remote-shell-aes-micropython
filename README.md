# TCP IP Remote Shell Aes Micropython
A simetric encrypted tcp remote shell write in micropython for embeded devices .

The blackOS remote shell

## Usage

### Listen for remote connection

```Python

import tcpshell

tcpshell.genkeys()

tcpshell.tcpshell("","66580466190907158953400191855519")


```


### Send command to micropython device and get the response

```Python

import tcpshell


tcpshell.blackcmd("192.168.1.163","a = gc.mem_free()","66580466190907158953400191855519")

b'\x10\x93\\\xc5.\xb9\xa4d\xa6\xe6\x1b\xc2\x85<\x14$\xcdi\x8dH&\x7fQ\x89\xf5\x91\x93\xe3\x11\xe4\x86k'

b"{'a': 22864}    "


```

