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

        if (p[std::stoi(start) - 1] == letter ^ p[std::stoi(end) - 1] == letter)
        {
            result++;
        }
    }

    std::cout << result;
}