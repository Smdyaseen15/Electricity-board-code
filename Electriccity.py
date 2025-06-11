class ElectricityBoard:
    def __init__(self):
        self.electricity_map = {}

    def add_connection(self, connection_id, connection_type):
        self.electricity_map[connection_id] = connection_type.lower()

    def find_count_of_connections(self, connection_type):
        connection_type = connection_type.lower()
        count = sum(1 for c_type in self.electricity_map.values() if c_type == connection_type)
        return count if count > 0 else -1

    def find_connection_ids(self, connection_type):
        connection_type = connection_type.lower()
        connection_ids = [c_id for c_id, c_type in self.electricity_map.items() if c_type == connection_type]
        return connection_ids if connection_ids else None

# Example Usage
def main():
    eb = ElectricityBoard()

    num_records = int(input("Enter the number of connection records to be added: "))
    for _ in range(num_records):
        record = input("Enter the connection record (ConnectionId:ConnectionType): ")
        connection_id, connection_type = record.split(":")
        eb.add_connection(connection_id, connection_type)

    search_type = input("Enter the Connection Type to be searched: ")
    count = eb.find_count_of_connections(search_type)
    if count == -1:
        print(f"No connections were found for {search_type}")
    else:
        print(f"The count of connection IDs based on {search_type.upper()} is {count}")

    filter_type = input("Enter the Connection Type to identify the Connection IDs: ")
    connection_ids = eb.find_connection_ids(filter_type)
    if connection_ids is None:
        print(f"No Connection IDs were found for {filter_type}")
    else:
        print(f"Connection IDs based on {filter_type.upper()} are: {', '.join(connection_ids)}")

if __name__ == "__main__":
    main()
