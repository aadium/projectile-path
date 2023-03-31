#include <iostream>
#include "trajectory.h"

using namespace std;

int main(int argc, char const *argv[])
{
    float angleinit;
    float vinit;
    float g = 9.81;
    char again = 'y';

    while (again == 'y' || again == 'Y') {
        std::cout << "Enter the initial velocity (m/s): ";
        std::cin >> vinit;
        std::cout << "Enter the angle of projection (degrees): ";
        std::cin >> angleinit;

        std::cout << "=======================================================" << std::endl;
        pequation(angleinit, vinit, g);
        std::cout << "Flight time (s): " << tflight(angleinit, vinit, g) << std::endl;
        std::cout << "Maximum height (m): " << hmax(angleinit, vinit, g) << std::endl;
        std::cout << "Horizontal range (m): " << hrange(angleinit, vinit, g) << std::endl;
        std::cout << "Maximum possible range (m): " << rangemax(vinit, g) << std::endl;
        std::cout << "=======================================================" << std::endl;
        std::cout << "Calculate another trajectory? (y/n): ";
        std::cin >> again;
    }

    std::cout << "Exiting program..." << std::endl;

    return 0;
}
