#include <Python.h>
#include <stdlib.h>

/******************************************************************************
 * Example of embedding python code into c program. Purpose is to use a trained 
 * Keras neural network to make predictions on data. 
 *
 * Forrest Davis
 * August 11, 2016
*******************************************************************************/
int main(int argc, char *argv[]){

    /* Instantiate python objects */
    PyObject *pProgramName, *pModule, *pDict, *pClass, *pInstance, *pValue;
    PyObject *pArgs, *pString;
    int i;

    /* create strings for python program details */
    char *program_name = "keras_model";
    char *class_name = "KerasModel";
    char *predict_function = "predict";
    char *fann_file = "fv.txt";
    char *fm_file = "parser.fm";
    char *model_arch = "trained_model.json";
    char *model_weights = "trained_model_weights.h5";

    /* set environment so that correct python program is called */
    setenv("PYTHONPATH",".",1);

    /* Initialize python interperter and get python class from 
     * program */
    Py_Initialize();
    pProgramName = PyString_FromString(program_name);
    pModule = PyImport_Import(pProgramName);
    pDict = PyModule_GetDict(pModule);
    pClass = PyDict_GetItemString(pDict, class_name);

    /* Set python tuple for Instance of python class */
    pArgs = PyTuple_New(2);

    pString = PyString_FromString(model_arch);
    PyTuple_SetItem(pArgs, 0, pString);
    pString = PyString_FromString(model_weights);
    PyTuple_SetItem(pArgs, 1, pString);

    if(PyCallable_Check(pClass)){
        pInstance = PyObject_CallObject(pClass, pArgs);
    }

    /* Format function name and variables for function call */
    PyObject *pFunctionName = PyString_FromString(predict_function);
    PyObject *pFM_file = PyString_FromString(fm_file);
    PyObject *pFANN_file = PyString_FromString(fann_file);

    /* Call function from python class three times */
    for(i=0; i<3; i++){
        pValue = PyObject_CallMethodObjArgs(pInstance, pFunctionName, 
                pFM_file, pFANN_file, NULL); 

        if(pValue != NULL){
            printf("Return of call : %ld\n", PyInt_AsLong(pValue));
            Py_DECREF(pValue);
        }
        else{
            PyErr_Print();
        }
    }

    /* Free python calls */
    Py_DECREF(pModule);
    Py_DECREF(pProgramName);
    Py_DECREF(pString);
    Py_DECREF(pFM_file);
    Py_DECREF(pFANN_file);
    Py_DECREF(pFunctionName);
    Py_DECREF(pDict);
    Py_DECREF(pClass);
    Py_DECREF(pInstance);
    Py_Finalize();

    return 0;

}
