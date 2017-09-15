#include <stdint.h>
#include <iostream>

extern "C"
{
    // A function adding two integers and returning the result
    uint8_t SampleAddInt(uint8_t i1, uint8_t i2)
    {
        std::cout << "HEY" << '\n';
        return i1 + i2;
    }
 
    // A function doing nothing ;)
    void SampleFunction1()
    {
        // insert code here
    }
 
    // A function always returning one
    int SampleFunction2()
    {
        // insert code here
        
        return 1;
    }
}