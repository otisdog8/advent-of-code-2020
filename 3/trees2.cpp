#include <bits/stdc++.h>

int main()
{
    std::ifstream infile("trees.in");
    std::string data;
    std::vector<std::vector<bool>> grid;
    int result = 0;
    while (infile >> data)
    {
        std::vector<bool> temp;
        auto p = data.begin();
        while (p < data.end())
        {
            temp.push_back(*p == '#');
            p++;
        }
        grid.push_back(temp);
    }

    int size = grid.at(0).size();
    long res = 1;

    int count = 0;
    for (int i = 0; i < grid.size(); i++)
    {
        if (grid[i][count % size])
        {
            result++;
        }
        count += 1;
    }
    res *= result;
    result = 0;
    count = 0;
    for (int i = 0; i < grid.size(); i++)
    {
        if (grid[i][count % size])
        {
            result++;
        }
        count += 3;
    }
    res *= result;
    result = 0;
    count = 0;
    for (int i = 0; i < grid.size(); i++)
    {
        if (grid[i][count % size])
        {
            result++;
        }
        count += 5;
    }
    res *= result;
    result = 0;
    count = 0;
    for (int i = 0; i < grid.size(); i++)
    {
        if (grid[i][count % size])
        {
            result++;
        }
        count += 7;
    }
    res *= result;
    result = 0;
    count = 0;
    for (int i = 0; i < grid.size(); i += 2)
    {
        if (grid[i][count % size])
        {
            result++;
        }
        count += 1;
    }
    res *= result;

    std::cout << res << std::endl;
}