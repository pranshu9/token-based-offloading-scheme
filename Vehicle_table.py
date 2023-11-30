class VehicleStatus:
    def __init__(self, position, server_range):
        self.position = position  # -1 for behind, 0 for no information, +1 for forward
        self.server_range = server_range  # Server range, e.g., "A", "B", "C", etc.

class VehicleTable:
    def __init__(self):
        self.table = {}

    def update_status(self, vehicle_id, position, server_range):
        self.table[vehicle_id] = VehicleStatus(position, server_range)

    def get_status(self, vehicle_id):
        return self.table.get(vehicle_id, VehicleStatus(0, ""))  # Return default values if the vehicle is not found

    def print_table(self):
        for vehicle_id, status in self.table.items():
            print(f"Vehicle {vehicle_id}: Position - {status.position}, Server Range - {status.server_range}")

# Example usage:
vehicle_table = VehicleTable()

# Update status for Vehicle 1
vehicle_table.update_status(1, -1, "A")

# Update status for Vehicle 2
vehicle_table.update_status(2, -1, "B")

# Update status for Vehicle 3 (no information about itself)
vehicle_table.update_status(3, 0, "")

# Update status for Vehicle 4
vehicle_table.update_status(4, 0, "B")

# Update status for Vehicle 5
vehicle_table.update_status(5, 0, "B and C")

# Update status for Vehicle 6
vehicle_table.update_status(6, 0, "C")

# Update status for Vehicle 7
vehicle_table.update_status(7, 1, "")  # +1 indicates it is in the forward direction

# Print the vehicle table
vehicle_table.print_table()

# Get the status of Vehicle 3
status_vehicle_3 = vehicle_table.get_status(3)
print(f"Status of Vehicle 3: Position - {status_vehicle_3.position}, Server Range - {status_vehicle_3.server_range}")
