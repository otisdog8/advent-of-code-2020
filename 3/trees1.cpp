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

    int count = 0;
    for (int i = 0; i < grid.size(); i++)
    {
        if (grid[i][count % size])
        {
            result++;
        }
        count += 3;
    }

    std::cout << result << std::endl;
}