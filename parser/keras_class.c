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
    char *load_function = "load";
    char *load_file = "1000_gold";
    char *fann_file = "fv.fann";
    char *fm_file = "parser.fm";
    char *data_directory = "./";

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
    pArgs = PyTuple_New(1);

    pString = PyString_FromString(data_directory);
    PyTuple_SetItem(pArgs, 0, pString);

    if(PyCallable_Check(pClass)){
        pInstance = PyObject_CallObject(pClass, pArgs);
    }

    /* Format function name and variables for function call */
    PyObject *pPredFunction = PyString_FromString(predict_function);
    PyObject *pLoadFunction = PyString_FromString(load_function);
    PyObject *pFM_file = PyString_FromString(fm_file);
    PyObject *pFANN_file = PyString_FromString(fann_file);
    PyObject *pLOAD_file = PyString_FromString(load_file);

    /* Load pretrained model */
    PyObject_CallMethodObjArgs(pInstance, pLoadFunction, pLOAD_file, NULL);

    /* Call function from python class three times */
    for(i=0; i<3; i++){
        pValue = PyObject_CallMethodObjArgs(pInstance, pPredFunction,
                pFANN_file, pFM_file, NULL);

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
    Py_DECREF(pLOAD_file);
    Py_DECREF(pPredFunction);
    Py_DECREF(pDict);
    Py_DECREF(pClass);
    Py_DECREF(pInstance);
    Py_Finalize();

    return 0;

}
