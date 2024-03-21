#include <iostream>
#include <string>

using namespace std;

class MecServerTable {
private:
    string serverName;
    int availableTokens;
    int consumedTokens;

public:
    // Constructor
    MecServerTable(string name, int initialTokens) : serverName(name), availableTokens(initialTokens), consumedTokens(0) {}

    // Method to grant a token
    bool grantToken() {
        if (availableTokens > 0) {
            availableTokens--;
            consumedTokens++;
            return true;
        } else {
            return false;
        }
    }

    // Method to release a token
    void releaseToken() {
        availableTokens++;
        consumedTokens--;
    }

    // Method to get the status of the server
    void getStatus() {
        cout << "Server Name: " << serverName << endl;
        cout << "Available Tokens: " << availableTokens << endl;
        cout << "Consumed Tokens: " << consumedTokens << endl;
    }
};

int main() {
    // Create instances of MecServerTable
    MecServerTable serverA("Server A", 2);
    MecServerTable serverB("Server B", 3);

    // Grant a token from Server A
    if (serverA.grantToken()) {
        cout << "Token granted by Server A" << endl;
    } else {
        cout << "Token request denied by Server A" << endl;
    }

    // Release a token back to Server A
    serverA.releaseToken();
    cout << "Token released back to Server A" << endl;

    // Get the status of Server A
    cout << "Status of Server A:" << endl;
    serverA.getStatus();

    // Get the status of Server B
    cout << "Status of Server B:" << endl;
    serverB.getStatus();

    return 0;
}
