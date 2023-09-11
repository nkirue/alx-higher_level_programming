#include <Python.h>

/**
 * print_python_list_info -prints basic info .
 * @p: list.
 */
void print_python_list_info(PyObject *p)
{
	int siz, allc, x;
	PyObject *ob;

	siz = Py_SIZE(p);
	allc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", siz);
	printf("[*] Allocated = %d\n", allc);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		ob = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obi)->tp_name);
	}
}
