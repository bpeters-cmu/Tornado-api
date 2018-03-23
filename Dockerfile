FROM continuumio/miniconda3

RUN conda install -c anaconda redis-py && \
    git clone https://github.com/bpeters-cmu/Tornado-api.git && \
    conda update -y -n base conda && \
    conda install -y -c anaconda redis-py

WORKDIR /Tornado-api

EXPOSE 80
CMD python app.py
