#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <complex>
#include <cmath>
#include <algorithm>
//#include "C:\Users\User\PycharmProjects\LiveSheetReader\ver2\src\app\all\vcpkg\buildtrees\jsoncpp\src\1.9.5-13b47286ba.clean/include/json/json.h"

//#include "./vcpkg/buildtrees/jsoncpp/src/1.9.5-13b47286ba.clean/include/json/json.h"


using namespace std;

vector<double> convert(vector<complex<double>> initial){
    vector<double> result;
    for (int i = 0; i < initial.size(); i++)
        result.push_back(abs(initial[i]));
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
        window.insert(window.end(), sig.begin() + i, sig.begin() + i + N);
        int sum = 0;
        for (int j = 0; j < N; j++)
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

int first_peak(vector<double> signal){
    vector<double> temp;
    temp.insert(temp.end(), signal.begin(), signal.begin() + signal.size()/2);
    int imax = argmax(temp);
    int ibegin = -1;
    int iend = 0;
    double threshold = 0.1 * signal[imax];
    for (int i = 0; i < imax + 100; i++){
        if (signal[i] >= threshold)
            if (ibegin == -1) ibegin = i;
        if (ibegin != -1 && signal[i] < threshold) {iend = i; break;}
    }
    temp.clear();
    temp.insert(temp.end(), signal.begin(), signal.begin() + iend + 100);
    return argmax(temp);
}

vector<int> all_peaks(vector<double> signal){
    vector<int> peaks;
    int imax = argmax(signal);
    double threshold = 0.005 * signal[imax];
    for (int i = 1 ; i < signal.size()/2 - 1 ; i++)
        if (signal[i] >= threshold && signal[i - 1] < signal[i] && signal[i] > signal[i + 1]) peaks.push_back(i);
    return peaks;
}

vector<int> prominence(vector<int> initial, vector<double> signal){
    vector<int> result;
    int lefty;
    int righty;
    auto right = min(signal.begin() + initial[0] , signal.begin() + initial[1]);
    righty = *right;
    if (righty <= 0.2 * signal[initial[0]]) result.push_back(initial[0]);
    for (int i = 1; i < initial.size() - 1; i++){
        auto left = min(signal.begin() + initial[i - 1] , signal.begin() + initial[i]);
        lefty = *left;
        auto right = min(signal.begin() + initial[i] , signal.begin() + initial[i+1]);
        righty = *right;
        if (lefty <= 0.2 * signal[initial[i]] && righty <= 0.2 * signal[initial[i]]) result.push_back(initial[i]);
    }
    auto left = min(signal.begin() + initial[initial.size() - 2] , signal.begin() + initial[initial.size() - 1]);
    lefty = *left;
    if (lefty <= 0.2 * signal[initial[initial.size() - 1]]) result.push_back(initial[initial.size() - 1]);
    return result;
}

void detect_note(vector<complex<double>> fft){
    vector<double> signal = convert(fft);
    vector<double> smooth_signal = moving_average(signal);
    vector<double> HP_signal;
    for (int i = 0; i < signal.size(); i++) HP_signal.push_back(signal[i] - smooth_signal[i]);
    vector<double> normalised_signal;
    double max_element = HP_signal[argmax(HP_signal)];
    for (int i = 0 ; i < signal.size() ; i++)
        normalised_signal.push_back(HP_signal[i]/max_element);
//    double max_element = HP_signal[argmax(HP_signal)];
//    for (int i = 0 ; i < signal.size() ; i++)
//        normalised_signal.push_back(HP_signal[i]);///max_element);
    int fp = first_peak(normalised_signal);
    vector<int> peaks;
    peaks.push_back(fp);
    vector <int> temp = all_peaks(normalised_signal);
    peaks.insert(peaks.end(), temp.begin(), temp.end());
    vector<int> prominent_peaks;
    vector<int> temp2 = prominence(peaks, normalised_signal);
    prominent_peaks.insert(prominent_peaks.end(),temp2.begin(), temp2.end());
    for (int i = 0; i < prominent_peaks.size(); i++) {
        cout << prominent_peaks[i] << endl;
    }


}