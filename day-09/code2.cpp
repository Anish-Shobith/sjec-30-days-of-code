#include <iostream>
#include <iterator>
#include <sstream>

std::string repeat(const std::string& input, size_t num)
{
    std::ostringstream os;
    std::fill_n(std::ostream_iterator<std::string>(os), num, input);
    return os.str();
}

int main()
{
    int n;
    std::cout<<"rows : ";
    std::cin>>n;
    for (int i = 0; i < n; i++)
        std::cout<<std::string(n - i - 1, ' ')<<repeat("# ", i + 1)<<std::endl;
    for (int i = 0; i < n; i++)
        std::cout<<std::string(i + 1, ' ')<<repeat("# ", n - i - 1)<<std::endl;
    return 0;
}
