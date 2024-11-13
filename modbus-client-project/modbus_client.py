from pymodbus.client import ModbusTcpClient

# Create a Modbus client instance pointing to the Docker container on port 5020
client = ModbusTcpClient('localhost', port=5020)

# Connect to the server
if client.connect():
    print("Connected to Modbus Server")

    # Read 5 registers starting at address 0
    result = client.read_holding_registers(0, 5)

    # Check if there's an error
    if result.isError():
        print("Error reading registers.")
    else:
        # Iterate through the result registers
        for i in range(5):
            register_value = result.registers[i]
            print(f"Register {i} Value: {register_value}")

    client.write_register(0, 0x1010)
    result = client.read_holding_registers(1, 1)  # Read the value back from register 9
    if result.isError():
        print("Error reading register")
    else:
        print(f"Register value: {result.registers}")
    # Close the connection
    client.close()
else:
    print("Failed to connect to Modbus server.")


