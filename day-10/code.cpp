// naive way because my brain ded.
#include <iostream>

int main() {
  int m;
  std::cin>>m;
  int count = 0;

  // Use nested for loops to iterate through all possible combinations
  for (int a = 2; a <= m - 3; a++) {
    for (int b = 2; b <= m - 3; b++) {
      for (int c = 2; c <= m - 3; c++) {
        for (int d = 2; d <= m - 3; d++) {
          for (int e = 2; e <= m - 3; e++) {
            // Check if the combination is valid
            if (a + b + c + d + e == m) {
              // If it is valid, increase the count
              count++;
            }
          }
        }
      }
    }
  }
  std::cout<<count<<std::endl;
  return 0;
}