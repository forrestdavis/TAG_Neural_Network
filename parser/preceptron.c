#include <stdio.h>
#include <python2.7/Python.h>

int main(){
    
    PyObject *pName, *pModule, *pDict, *pFunc;
    PyObject *pArgs, *pValue;

    Py_Initialize();

    PyRef module = PyImport_ImportModule("class.py");


    Py_Finalize();

    return 0;
}
