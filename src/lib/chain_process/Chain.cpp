#include "Chain.h"
#include <math>
#include <vector>
#include <string>

vector<int> Chain::get_groups() const{
    vector<int> values;
    for (const auto& element : val) {
        values.push_back(element.get_group());
    }
    return values;
}

vector<int> Chain::get_indices() const{
    vector<int> values;
    for (const auto& element : val) {
        values.push_back(element.get_index());
    }
    return values;
}


vector<string> Chain::get_types() const{
    vector<string> values;
    for (const auto& element : val) {
        values.push_back(element.get_type());
    }
    return values;
}

void Chain::calc_cont() const{

}

