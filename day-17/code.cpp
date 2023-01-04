#include <iostream>
#include <vector>

int main() {
  int n;
  std::cin>>n;
  std::vector<int> frames;
  for (int i = 0; i < n; i++) {
    int f;
    std::cin>>f;
    if (!frames.empty() && frames.back() == f) {
      continue;
    }
    frames.push_back(f);
  }
  for (int i = 0; i < frames.size(); i++) {
    std::cout<<frames[i]<<" ";
  }
  return 0;
}
