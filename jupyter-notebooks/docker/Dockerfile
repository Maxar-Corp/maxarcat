#
# Dockerfile for Jupyter notebook with maxarcat installed.
#
# Build like this:
#     cd maxarcat/jupyter-notebooks/docker
#     docker build --tag jupyter-maxarcat .
#
# Run like this to mount repo inside running container:
#     cd maxarcat
#     docker run --rm -p 8888:8888 -v "$(pwd):/home/jovyan/work" jupyter-maxarcat
#
# Then copy-and-paste into a browser the URL the jupyter service prints out.
#

FROM jupyter/base-notebook

# Packages the notebook uses
RUN pip install geopandas ipyleaflet

# Install the ipyleaflet jupyter extension.  See https://github.com/jupyter-widgets/ipyleaflet
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet

RUN pip install maxarcat
