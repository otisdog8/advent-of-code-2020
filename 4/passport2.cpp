#include <bits/stdc++.h>

int main()
{
    std::ifstream infile("passport.in");

    std::vector<std::unordered_map<std::string, std::string>> passports;
    std::unordered_map<std::string, std::string> passport;
    for (std::string line; std::getline(infile, line);)
    {
        if (line.size() == 0)
        {
            passports.push_back(passport);
            passport.clear();
        }
        else
        {
            std::istringstream iss = std::istringstream{line};
            std::string str;
            while (iss >> str)
            {
                passport[str.substr(0, str.find(":"))] = str.substr(str.find(":") + 1);
            }
        }
    }

    std::string parts[7] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

    int result = 0;
    std::cout << passports.size() << std::endl;

    for (auto passport : passports)
    {
        bool pass = true;
        for (auto part : parts)
        {
            if (!passport.count(part))
            {
                pass = false;
                break;
            }
        }
        if (pass)
        {
            result++;
        }
    }

    std::cout << result << std::endl;
}