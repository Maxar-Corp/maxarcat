# maxarcat

Maxarcat is a Python client for searching the
[Maxar Catalog](https://doc.content.maxar.com).

The client consists of two parts:

* maxarcat_client:  Automatically generated client created by
    [Swagger codegen](https://github.com/swagger-api/swagger-codegen)
    from the [Maxar Catalog OpenAPI specification](https://doc.content.maxar.com/maxar-content-catalog.html).
* maxarcat:  Wrapper code on top of maxarcat_client providing a simple interface
    to the generated client.

A single Python wheel called "maxarcat" includes both of these packages.

See the Jupyter notebook in this repo
([jupyter-notebooks/Maxar python client tutorial.ipynb](jupyter-notebooks/Maxar%20python%20client%20tutorial.ipynb))
for examples of using the client.  Also see documentation on the
[Maxar Catalog](https://doc.content.maxar.com) website.

## Installation

maxarcat is available on PyPi at https://pypi.org/project/maxarcat

```
pip install maxarcat
```
