# maxarcat

Maxarcat is a Python client for searching the [Maxar Catalog](https://doc.content.maxar.com).

The client consists of two parts:

* maxarcat_client:  Automatically generated client created by Swagger codegen
    from the Maxar Catalog OpenAPI specification.
* maxarcat:  Wrapper code on top of maxarcat_client providing a clean interface
    to the generated client.

A single Python wheel called "maxarcat" includes both of these packages.

See Jupyter notebooks in the "notebooks" directory for examples of using
the maxar-catalog package.
