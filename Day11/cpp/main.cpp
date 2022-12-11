#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <string.h>
#include <queue>
#include <assert.h>

using namespace std;

struct Monkey
{
    queue<int> items;
    char op;
    uint8_t val_op;
    uint8_t test;
    uint8_t tt;
    uint8_t tf;
    uint32_t inspected = 0;

    void print()
    {
        cout << "op: " << op << " test: " << (int)test << " tt: " << (int)tt << " tf: " << (int)tf << " inspected: " << inspected << " items: ";
        queue<int> Q = items;
        for (size_t i = 0; i < Q.size(); i++)
        {
            cout << Q.front() << " ";
            Q.push(Q.front());
            Q.pop();
        }
        cout << endl;
    }

    void execute(vector<Monkey> *other_monkeys)
    {
        while (!items.empty())
        {

            int item = items.front();
            items.pop();
            int64_t val = 0;
            switch (op)
            {
            case '+':
                if (val_op != 0)
                    val = item + val_op;
                else
                    val = item + item;
                break;

            case '*':
                if (val_op != 0)
                    val = item * val_op;
                else
                    val = item * item;
                break;

            default:
                cout << "Error: op not valid \n";
                exit(-1);
                break;
            }

            val = val / 3;
            if (val % test == 0)
            {
                other_monkeys->at(tt).items.push(val);
            }
            else
            {
                other_monkeys->at(tf).items.push(val);
            }

            inspected++;
        }
    }
};

int solve_one(string input_file)
{
    ifstream file(input_file);
    if (file.is_open())
    {
        vector<Monkey> monkeys;
        string line, tmp;

        // with this we skip always the first line "Monkey X"
        while (getline(file, line))
        {
            if (line.size() < 2)
            {
                getline(file, line); // skip empty
            }

            Monkey m;
            std::stringstream ss(line);

            getline(file, line); // items
            std::stringstream items(line);
            items >> tmp >> tmp; // skip Starting items:
            while (items >> tmp)
            {
                char *token;
                char *buf = strdup(tmp.c_str());
                token = strtok(buf, ",");
                m.items.push(atoi(token));
            }
            getline(file, line); // operations
            std::stringstream operation(line);
            operation >> tmp >> tmp >> tmp >> tmp; // skip "Operation: new = old"
            operation >> tmp;
            m.op = tmp.c_str()[0];
            operation >> tmp;
            m.val_op = atoi(tmp.c_str());

            getline(file, line); // test
            std::stringstream test(line);
            test >> tmp >> tmp >> tmp; // skip "Test: divisible by"
            test >> tmp;
            m.test = atoi(tmp.c_str());

            getline(file, line); // tt
            std::stringstream tt(line);
            tt >> tmp >> tmp >> tmp >> tmp >> tmp; // skip "If true: throw to monkey"
            tt >> tmp;
            m.tt = atoi(tmp.c_str());

            getline(file, line); // tf
            std::stringstream tf(line);
            tf >> tmp >> tmp >> tmp >> tmp >> tmp; // skip "If false: throw to monkey"
            tf >> tmp;
            m.tf = atoi(tmp.c_str());
            monkeys.push_back(m);
        }

        for (size_t i = 0; i < 20; i++)
        {
            for (size_t i = 0; i < monkeys.size(); i++)
            {
                monkeys[i].execute(&monkeys);
            }
        }

        vector<int> inspected;
        for (auto m : monkeys)
        {
            inspected.push_back(m.inspected);
        }
        sort(inspected.begin(), inspected.end(), greater<int>());

        return inspected[0] * inspected[1];

        file.close();
    }
    else
    {
        cout << "Error opening file \n";
        return -1;
    }
}

struct Monkey2
{
    queue<int> items;
    char op;
    uint8_t val_op;
    uint8_t test;
    uint8_t tt;
    uint8_t tf;
    uint32_t inspected = 0;
    uint32_t lcm;

    void print()
    {
        cout << "op: " << op << " test: " << (int)test << " tt: " << (int)tt << " tf: " << (int)tf << " inspected: " << inspected << " items: ";
        queue<int> Q = items;
        for (size_t i = 0; i < Q.size(); i++)
        {
            cout << Q.front() << " ";
            Q.push(Q.front());
            Q.pop();
        }
        cout << endl;
    }

    void execute(vector<Monkey2> *other_monkeys)
    {
        while (!items.empty())
        {

            uint64_t item = items.front();
            items.pop();
            uint64_t val = 0;
            switch (op)
            {
            case '+':
                if (val_op != 0)
                    val = item + val_op;
                else
                    val = item + item;
                break;

            case '*':
                if (val_op != 0)
                    val = item * val_op;
                else
                    val = item * item;
                break;

            default:
                cout << "Error: op not valid \n";
                exit(-1);
                break;
            }
            val = val % lcm;
            if (val % test == 0)
            {
                other_monkeys->at(tt).items.push(val);
            }
            else
            {
                other_monkeys->at(tf).items.push(val);
            }

            inspected++;
        }
    }
};

uint64_t solve_two(string input_file)
{
    ifstream file(input_file);
    if (file.is_open())
    {
        vector<Monkey2> monkeys;
        string line, tmp;

        int lcm = 1;

        // with this we skip always the first line "Monkey X"
        while (getline(file, line))
        {
            if (line.size() < 2)
            {
                getline(file, line); // skip empty
            }

            Monkey2 m;
            std::stringstream ss(line);

            getline(file, line); // items
            std::stringstream items(line);
            items >> tmp >> tmp; // skip Starting items:
            while (items >> tmp)
            {
                char *token;
                char *buf = strdup(tmp.c_str());
                token = strtok(buf, ",");
                m.items.push(atoi(token));
            }
            getline(file, line); // operations
            std::stringstream operation(line);
            operation >> tmp >> tmp >> tmp >> tmp; // skip "Operation: new = old"
            operation >> tmp;
            m.op = tmp.c_str()[0];
            operation >> tmp;
            m.val_op = atoi(tmp.c_str());

            getline(file, line); // test
            std::stringstream test(line);
            test >> tmp >> tmp >> tmp; // skip "Test: divisible by"
            test >> tmp;
            m.test = atoi(tmp.c_str());
            lcm *= m.test;

            getline(file, line); // tt
            std::stringstream tt(line);
            tt >> tmp >> tmp >> tmp >> tmp >> tmp; // skip "If true: throw to monkey"
            tt >> tmp;
            m.tt = atoi(tmp.c_str());

            getline(file, line); // tf
            std::stringstream tf(line);
            tf >> tmp >> tmp >> tmp >> tmp >> tmp; // skip "If false: throw to monkey"
            tf >> tmp;
            m.tf = atoi(tmp.c_str());
            monkeys.push_back(m);
        }

        for (size_t i = 0; i < monkeys.size(); i++)
        {
            monkeys[i].lcm = lcm;
        }

        for (size_t i = 0; i < 10000; i++)
        {
            for (size_t i = 0; i < monkeys.size(); i++)
            {
                monkeys[i].execute(&monkeys);
            }
        }

        vector<uint64_t> inspected;
        for (auto m : monkeys)
        {
            inspected.push_back(m.inspected);
        }
        sort(inspected.begin(), inspected.end(), greater<uint64_t>());

        return inspected[0] * inspected[1];

        file.close();
    }
    else
    {
        cout << "Error opening file \n";
        return -1;
    }
}

int main(int, char **)
{
    // with ranges
    assert(solve_one("../test.txt") == 10605);
    cout << "Part 1: " << solve_one("../../input.txt") << endl;
    assert(solve_two("../test.txt") == 2713310158);
    cout << "Part 2: " << solve_two("../../input.txt") << endl;
}