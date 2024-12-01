#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main(int, char **)
{
    //with ranges
    ifstream file("../../input.txt");
    if (file.is_open())
    {
        int s1 = 0, s2 = 0;
        string str;
        while (file >> str)
        {
            int r1s, r2s, r1e, r2e;
            sscanf(str.c_str(), "%d-%d,%d-%d", &r1s, &r1e, &r2s, &r2e);

            // part 1
            if (((r2s >= r1s) && (r2e <= r1e)) || ((r2s <= r1s) && (r2e >= r1e)))
            {
                s1++;
            }

            // part 2
            if (!((r1s > r2e) || (r2s > r1e)))
            {
                s2++;
            }
        }
 
        cout << "Part 1 (ranges): " << s1 << endl;
        cout << "Part 2 (ranges): " << s2 << endl;
    }
    else
    {
        cout << "Error opening file \n";
        return -1;
    }

    // with set and set_intersection
    file.clear();
    file.seekg(0);
    if (file.is_open())
    {
        int s1 = 0, s2 = 0;
        string str;
        while (file >> str)
        {
            int r1s, r2s, r1e, r2e;
            sscanf(str.c_str(), "%d-%d,%d-%d", &r1s, &r1e, &r2s, &r2e);

            set<int> r1, r2;
            for (auto i = r1s; i <= r1e; i++)
            {
                r1.insert(i);
            }

            for (auto i = r2s; i <= r2e; i++)
            {
                r2.insert(i);
            }

            std::vector<int> v_intersection;

            std::set_intersection(r1.begin(), r1.end(),
                                  r2.begin(), r2.end(),
                                  std::back_inserter(v_intersection));

            if (v_intersection.size() == r1.size() || v_intersection.size() == r2.size())
            {
                s1++;
            }

            if (v_intersection.size() > 0)
            {
                s2++;
            }
        }

        cout << "Part 1 (sets): " << s1 << endl;
        cout << "Part 2 (sets): " << s2 << endl;

        file.close();
    }
    else
    {
        cout << "Error opening file \n";
        return -1;
    }
}
