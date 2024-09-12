from pwn import *

HOST = "2048.challs.olicyber.it"
PORT = 10007
r = remote(HOST, PORT)

#data = r.recvuntil(b"operazioni:")
data = r.recvline()
data = r.recvline()

for i in range(2049):
        data = r.recv(1024)
        print(str(i) + ' ' + str(data))

        operation, a, b, bin = str(data).split(' ')

        a = int(a)
        b = int(b)


        if operation[2:] == 'SOMMA':
                sum = a + b
                r.sendline(str(sum).encode())
        elif operation[2:] == 'POTENZA':
                sum = pow(a,b)
                r.sendline(str(sum).encode())
        elif operation[2:] == 'PRODOTTO':
                sum = a * b
                r.sendline(str(sum).encode())
        elif operation[2:] == 'DIFFERENZA':
                sum = a - b
                r.sendline(str(sum).encode())
        elif operation[2:] == 'DIVISIONE_INTERA':
                sum = int(a/b)
                r.sendline(str(sum).encode())

print(data)
r.close()
