#include "Python.h"

/**
 * print_python_bytes - print information about Python bytes object
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytes_size, i;
	char *bytes_string;

	printf("[.] bytes object info\n");
	if (p != NULL && PyBytes_Check(p))
	{
		bytes_size = PyBytes_Size(p);
		bytes_string = PyBytes_AsString(p);
		printf("  size: %ld\n", bytes_size);
		printf("  trying string: %s\n", bytes_string);
		printf("  first %ld bytes:",
		       bytes_size + 1 < 10 ? bytes_size + 1 : 10);
		for (i = 0; i < bytes_size + 1 && i < 10; i++)
			printf(" %02x", bytes_string[i] & 0xff);
		putchar('\n');
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - print information about Python list object
 * @p: pointer to PyObject
 */
void print_python_list(PyObject *p)
{
	PyObject *item;
	PyListObject *list;
	Py_ssize_t list_size, list_alloc, i;
	const char *type;

	if (p != NULL && PyList_Check(p))
	{
		list_size = PyList_Size(p);
		if (list_size < 0)
			return;
		list = (PyListObject *)p;
		list_alloc = list->allocated;
		if (list_alloc < 0)
			return;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", list_size);
		printf("[*] Allocated = %ld\n", list_alloc);
		for (i = 0; i < list_size; i++)
		{
			item = list->ob_item[i];
			type = item->ob_type->tp_name;
			printf("Element %ld: %s\n", i, type);
			if (PyBytes_Check(item))
				print_python_bytes(item);
		}
	}
}
