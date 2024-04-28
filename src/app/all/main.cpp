#include "../../lib/all/get_from_python.h"
#include "../../lib/audio_process/FFT.h"
#include "../../lib/chain_process/Chain.h"
using namespace std;
int main(){
    vector<int> arr = audio_from_python();
    vector<complex<double>> arry = FFT(arr);
    return 0;
}