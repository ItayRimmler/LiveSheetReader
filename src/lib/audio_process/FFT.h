#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <complex>
#include <cmath>

using namespace std;

vector<int> Divide(vector<int> sub){
    if (static_cast<int>(sub.size()) > 1){
        vector<int> subodd;
        vector<int> subeven;
        for (int i = 0; i <static_cast<int>(sub.size()); i++){
            if (i%2 == 0){
                subeven.push_back(sub[i]);
            } else {
                subodd.push_back(sub[i]);
            }
        }
        subodd = Divide(subodd);
        subeven = Divide(subeven);
        vector<int> result;
        for (int i = 0; i <(static_cast<int>(sub.size())/2); i++){
            result.push_back(subodd[i]);
            result.push_back(subeven[i]);
        }
        return result;
    }
    else (sub[0])++;
    return sub;

}

vector<int> FFT(vector<int> signal){
    vector<int> result;
    result.resize(static_cast<int>(signal.size()));
    cout << "a" << endl;
    for (int i = 0; i<static_cast<int>(result.size()); i++){
        cout << result[i] << " ";
    }
    cout << endl << "b" << endl;
    result = Divide(result);
    for (int i = 0; i<static_cast<int>(result.size()); i++){
        cout << result[i] << " ";
    }
    cout << endl;
    return result;
}