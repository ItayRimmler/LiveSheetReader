#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <complex>
#include <cmath>
#include <algorithm>

using namespace std;

vector<double> convert(vector<complex<double>> initial){
    vector<double> result;
    for (int i = 0; i < initial.size(); i++)
        result.push_back(initial.real());
    return result;
}

int argmax(vector<double> vec){
    auto max_it = max_element(vec.begin(), vec.end());
    return distance(vec.begin(), max_it);
}

vector<double> moving_average(vector<double> sig){
    vector<double> new_sig, window;
    int N = 10;
    for (int j = 0; j < N; j++){
        int sum = 0;
        window.push_back(sig[j]);
        for (int i = 0; i < window.size(); i++)
            sum += window[i];
        new_sig.push_back(sum/N);
    }
    for (int i = N; i < sig.size() - N; i++){
        window.clear();
        window.insert(window.end(), sig.start() + i, sig.start() + i + N);
        int sum = 0;
        for (int j = 0; j < N; i++)
            sum += window[j];
        new_sig.push_back(sum/N);
    }
    for (int j = sig.size() - N; j < sig.size(); j++){
        int sum = 0;
        window.erase(window.begin());
        for (int i = 0; i < window.size(); i++)
            sum += window[i];
        new_sig.push_back(sum/N);
    }
    return new_sig;
}

vector<double> derive(vector<double> sig){
    int N = static_cast<int>(sig.size());
    vector<double> new_sig;
    new_sig.push_back(sig[0]);
    for (int i = 1; i < N; i++)
        new_sig.push_back(sig[i] - sig[i - 1]);
    return new_sig;
}

vector<string> detect_note(vector<complex<double>> fft){
    vector<double> signal = convert(fft);
    vector<double> smooth_signal = moving_average(signal);
    vector<double> derivative = derive(smooth_signal);
}