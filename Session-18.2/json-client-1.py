# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost' #si queremos que hable con ensembl, pondremos el ip adress del ensembl

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT) # connect

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers") # send the request
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse() # con este method lees la respuesta, the da un HTTP RESPONSE, objecto con several attributes como status y reason

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8") # esto es una string, por lo que para usarla, json.load

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
print()
print("Name: ", end="")
print(person['Firstname'], person['Lastname'])

print("Age: ", end="")
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']

# Print the number of elements int the list
print("Phone numbers: ",  end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    print("  Phone {}:".format(i))

    # The element num contains 2 fields: number and type
    print("    Type: ", end='')
    print(num['type'])
    print("    Number: ", end='')
    print(num['number'])