#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


namespace mediapipe{
    class GoblinCalculator12 : public CalculatorBase {
        public:
        static Status GetContract{CalculatorContract *cc} {
            using namespace std;
            cc->Inputs().Index(0).Set<double>();
            cc->Outputs().Index(0).Set<double>();
            return OkStatus();
        }
    Status Process(CalculatorContext *cc) override {
        
    }
    }
}