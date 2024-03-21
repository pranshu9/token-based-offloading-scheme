#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class VehicleStatus {
public:
    int position;         // -1 for behind, 0 for no information, +1 for forward
    string serverRange;   // Server range, e.g., "A", "B", "C", etc.

    // Constructor
    VehicleStatus(int pos, string range) : position(pos), serverRange(range) {}
};

class VehicleTable {
private:
    unordered_map<int, VehicleStatus> table;

public:
    // Method to update status for a vehicle
    void updateStatus(int vehicleId, int position, string serverRange) {
        table[vehicleId] = VehicleStatus(position, serverRange);
    }

    // Method to get status of a vehicle
    VehicleStatus getStatus(int vehicleId) {
        if (table.find(vehicleId) != table.end()) {
            return table[vehicleId];
        } else {
            return VehicleStatus(0, ""); // Return default values if vehicle not found
        }
    }

    // Method to print the vehicle table
    void printTable() {
        for (auto& entry : table) {
            cout << "Vehicle " << entry.first << ": Position - " << entry.second.position << ", Server Range - " << entry.second.serverRange << endl;
        }
    }
};

int main() {
    // Create an instance of VehicleTable
    VehicleTable vehicleTable;

    // Update status for Vehicle 1
    vehicleTable.updateStatus(1, -1, "A");

    // Update status for Vehicle 2
    vehicleTable.updateStatus(2, -1, "B");

    // Update status for Vehicle 3 (no information about itself)
    vehicleTable.updateStatus(3, 0, "");

    // Update status for Vehicle 4
    vehicleTable.updateStatus(4, 0, "B");

    // Update status for Vehicle 5
    vehicleTable.updateStatus(5, 0, "B and C");

    // Update status for Vehicle 6
    vehicleTable.updateStatus(6, 0, "C");

    // Update status for Vehicle 7
    vehicleTable.updateStatus(7, 1, ""); // +1 indicates it is in the forward direction

    // Print the vehicle table
    vehicleTable.printTable();

    // Get the status of Vehicle 3
    VehicleStatus statusVehicle3 = vehicleTable.getStatus(3);
    cout << "Status of Vehicle 3: Position - " << statusVehicle3.position << ", Server Range - " << statusVehicle3.serverRange << endl;

    return 0;
}
