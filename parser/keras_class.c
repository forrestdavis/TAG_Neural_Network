#include <Python.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

    PyObject *pName, *pModule, *pDict, *pClass, *pInstance, *pValue, *pArgs, *pString;
    int i, arg[8];
    char *program_name = "change";
    char *class_name = "KerasModel";
    char *predict_function = "predict";
    char *fann_file = "fv.txt";
    char *model_arch = "trained_model.json";
    char *model_weights = "trained_model_weights.h5";

    setenv("PYTHONPATH",".",1);

    Py_Initialize();
    pName = PyString_FromString(program_name);
    pModule = PyImport_Import(pName);
    pDict = PyModule_GetDict(pModule);

    pClass = PyDict_GetItemString(pDict, class_name);

    pArgs = PyTuple_New(2);

    pString = PyString_FromString(model_arch);
    PyTuple_SetItem(pArgs, 0, pString);
    pString = PyString_FromString(model_weights);
    PyTuple_SetItem(pArgs, 1, pString);

    if(PyCallable_Check(pClass)){
        pInstance = PyObject_CallObject(pClass, pArgs);
    }

    PyObject *pString1 = PyString_FromString(predict_function);
    pString = PyString_FromString(fann_file);

    for(i=0; i<3; i++){
        pValue = PyObject_CallMethodObjArgs(pInstance, pString1, pString, NULL); 

        char buffer[50];
        if(pValue != NULL){
            //printf("Return of call : %ld\n", PyInt_AsLong(pValue));
            sprintf(buffer, "%d", PyInt_AsLong(pValue));
            int mvt_code = atoi(buffer);
            printf("%d\n", mvt_code);
            Py_DECREF(pValue);
        }
        else{
            PyErr_Print();
        }
    }

    Py_DECREF(pModule);
    Py_DECREF(pName);
    Py_Finalize();

    return 0;

}
