#include <bits/stdc++.h>

int main()
{
    std::ifstream infile("password.in");
    std::string data;
    int result = 0;

    while (infile >> data)
    {
        auto p = data.begin();
        std::string start = "";
        std::string end = "";

        while (*p != '-')
        {
            start += *p;
            p++;
        }

        p++;

        while (p < data.end())
        {
            end += *p;
            p++;
        }

        char garbo, letter;
        infile >> letter;
        infile >> garbo;

        std::string pw = "";

        infile >> pw;

        p = pw.begin();
        int count = 0;

        while (p < pw.end())
        {
            if (*p == letter)
            {
                count++;
            }
            p++;
        }
        if (std::stoi(start) <= count && std::stoi(end) >= count)
        {
            result++;
        }
    }

    std::cout << result;
}