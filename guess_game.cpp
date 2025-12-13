#include <iostream>
#include <cstdlib>   // for rand()
#include <ctime>     // for time()

int main() {
    // Initialize random seed
    std::srand(std::time(0));
    int number = std::rand() % 10 + 1;  // Random number 1-10
    int guess;

    std::cout << "Guess the number between 1 and 10: ";

    while (true) {
        std::cin >> guess;

        if (guess < number) {
            std::cout << "Too low! Try again: ";
        } else if (guess > number) {
            std::cout << "Too high! Try again: ";
        } else {
            std::cout << "Correct! The number was " << number << std::endl;
            break;
        }
    }

    return 0;
}
