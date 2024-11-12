from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('172.18.0.2', port=5020)

while True:
    try:
        result = client.read_holding_registers(address=1, count=1, unit=1)
        print(result)
    except Exception as e:
        print(f"Connection failed: {e}")
        break  # Exit if connection fails
