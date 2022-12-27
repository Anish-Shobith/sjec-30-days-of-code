#include <iostream>

int main()
{
    int n;
    std::cout<<"rows : ";
    std::cin>>n;

    for (int i = 0; i < n; i++)
    {
        std::string s;
        for (int j = 0; j < i + 1; j++)
            s += "# ";
        std::cout<<std::string(n - i - 1, ' ')<<s<<std::endl;
    }

    for (int i = 0; i < n; i++)
    {
        std::string s;
        for (int j = 0; j < n - i - 1; j++)
            s += "# ";
        std::cout<<std::string(i + 1, ' ')<<s<<std::endl;
    }
    return 0;
}
