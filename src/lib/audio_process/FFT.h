#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <complex>
#include <cmath>

using namespace std;

vector<complex<double>> Divide(vector<complex<double>> sub){
    if (static_cast<int>(sub.size()) > 1){
        vector<complex<double>> subodd;
        vector<complex<double>> subeven;
        int N = static_cast<int>(sub.size());
        for (int i = 0; i <N; i++){
            if (i%2 == 0){
                subeven.push_back(sub[i]);
            } else {
                subodd.push_back(sub[i]);
            }
        }
        subodd = Divide(subodd);
        subeven = Divide(subeven);
        vector<complex<double>> result(N);
        for (size_t k = 0; k < N / 2; k++) {
            complex<double> t = polar(1.0, -2 * 3.141592653589793238460 * k / N) * subodd[k];
            result[k] = subeven[k] + t;
            result[k + N / 2] = subeven[k] - t;
        }
        return result;
    }
    return sub;
}

vector<complex<double>> FFT(vector<int> signal){
    vector<complex<double>> result;
    vector<complex<double>> arg;
    for (int i = 0; i< signal.size(); i++) {
        arg.push_back(complex<double>(signal[i], 0.0));
    }
    cout << static_cast<int>(arg.size()) << endl;
    for (int i = 0; i<static_cast<int>(arg.size()); i++){
        cout << arg[i].real() << " ";
    }
    result = Divide(arg);
    cout << endl << static_cast<int>(result.size()) << endl;
    for (int i = 0; i<static_cast<int>(result.size()); i++){
        cout << result[i].real() << " ";
    }
    cout << endl;
    return result;
}