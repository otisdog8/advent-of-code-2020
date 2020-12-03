#include <bits/stdc++.h>

int main()
{
    // doing this in O(n) because I feel special. Worst case is O(n^2). I could get guranteed O(nlogn) with normal set.
    std::ifstream infile("reportrepair.in");
    int a;
    std::unordered_set<int> b;

    while (infile >> a)
    {
        b.insert(a);
    }

    for (const int elem : b)
    {
        for (const int elem2 : b)
        {
            if (b.find(2020 - elem2 - elem) != b.end())
            {
                int c = (elem * elem2 * (2020 - elem - elem2));
                std::cout << c << std::endl;
            }
        }
    }
}