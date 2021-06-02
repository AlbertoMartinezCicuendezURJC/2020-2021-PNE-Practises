import http.client


PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

endpoint1 = "/info/A"

try:
    conn.request("GET", endpoint1)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

a_info = conn.getresponse()
print(f"Response received!: {a_info.status} {a_info.reason}\n")

a_dict = a_info.read().decode()
print(a_dict)



