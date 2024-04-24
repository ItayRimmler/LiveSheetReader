#include "C:/Users/User/PycharmProjects/LiveSheetReader/ver2/src/lib/chain_process/Chain.h"
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;


vector<int> Chain::get_groups() const {
    vector<int> values;
    for (const auto& element : this->val) {
        values.push_back(element.get_group());
    }
    return values;
}

vector<int> Chain::get_indices() const {
    vector<int> values;
    for (const auto& element : this->val) {
        values.push_back(element.get_index());
    }
    return values;
}


vector<string> Chain::get_types() const {
    vector<string> values;
    for (const auto& element : this->val) {
        values.push_back(element.get_type());
    }
    return values;
}

void Chain::calc_cont() {
    this->cont.clear();
    for (int i = 0; i < this->get_len() - 1; i++) {
        if (this->val[i + 1].get_index() - this->val[i].get_index() == 1) {
            this->cont.push_back(1);
        }
        else { this->cont.push_back(0); }
    }
}

void Chain::calc_score() {
    int j = 1;
    this->score = 0;
    for (int i = 0; i < this->get_len() - 1; i++) {
        if (this->cont[i] == 1) {
            j++;
            if (i == this->get_len() - 2) {
                this->score = this->score + pow(j, j);
                j = 1;
            }
        }
        else {
            this->score += pow(j, j);
            j = 1;
        }
    }
    this->score = this->score * pow(this->get_len(), this->get_len());
}

vector<Chain> Chain::possible_matches(const vector<Note>& other) const {
    vector<Chain> list_of_possibilities;
    int i = 0;
    while (i < static_cast<int>(other.size())) {
        int j = 0, counter = this->get_len();
        vector<Note> possibility;
        while ((counter > 0) && ((i + j) < this->get_len()) && (j < other.size())) {
            if (other[j].get_type() == this->val[i + j].get_type()) {
                possibility.push_back(this->val[i + j]);
                counter--;
            }
            j++;
        }
        Chain temp(possibility);
        list_of_possibilities.push_back(temp);
        i++;
    }
    return list_of_possibilities;
}

vector<Note> Chain::match(const vector<Note>& other) const {
    cout << 1 << endl;
    vector<Chain> list_of_possibilities = possible_matches(other);
    int highest_score = 0;
    vector<Note> result;
    for (auto& chain : list_of_possibilities) {
        chain.calc_cont();
        chain.calc_score();
        int temp = chain.get_score();
        if (temp > highest_score) {
            result = chain.get_val();
            highest_score = temp;
        }
    }
    return result;
}

