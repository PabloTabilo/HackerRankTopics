#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    vector<int> p = {15,  12,  8,   8,   7,   7,   7,   6,   5,   3};
    vector<int> h = {10,  25,  17,  11,  13,  17,  20,  13,  9,   15};
    
    float sample_mean1 = 0, sample_mean2 = 0;
    int n = p.size();
    float nd = 1.0f*n;
    
    for(int i=0;i<n;i++){
        sample_mean1 += (float)p[i];
        sample_mean2 += (float)h[i];
    }
    sample_mean1 /= nd;
    sample_mean2 /= nd;
    
    float cov12 = 0;
    float var1 = 0;
    float var2 = 0;
    
    for(int i=0;i<n;i++){
        cov12 += (sample_mean1 - (float)p[i]) * (sample_mean2 - (float)h[i]);
        var1 += (sample_mean1 - (float)p[i]) * (sample_mean1 - (float)p[i]);
        var2 += (sample_mean2 - (float)h[i]) * (sample_mean2 - (float)h[i]);
    }
    
    cov12 /= (nd-1);
    var1 /= (nd-1);
    var2 /= (nd-1);
    
    float corr = cov12 / sqrt(var1 * var2);
    float app3decimals = round(corr * 1000.0) / 1000.0;
    cout << app3decimals << endl;
    return 0;
}