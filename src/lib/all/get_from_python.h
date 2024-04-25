#pragma once
#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> audio_from_python(){
    ifstream file("C:/Users/User/PycharmProjects/LiveSheetReader/ver2/data/recording.bin", ios::binary);
    vector<int> arr;
    int value;
    while (file.read(reinterpret_cast<char*>(&value), sizeof(int16_t))) {
        arr.push_back(static_cast<int16_t> (value));
    }
    file.close();
    return arr;
}