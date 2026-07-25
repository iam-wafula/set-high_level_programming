#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    int i, size;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("  size: %d\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);

    printf("  first %d bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
        printf(" %02x", (unsigned char)bytes->ob_sval[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t i, size;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);

        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
        {
            printf("bytes\n");
            print_python_bytes(item);
        }
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyList_Check(item))
            printf("list\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("%s\n", Py_TYPE(item)->tp_name);
    }
}
