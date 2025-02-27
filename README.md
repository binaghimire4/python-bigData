# Python for Big Data Analysis
Python is a popular programming language for developing software and data science applications. Its popularity stems from many factors such as simplicity, readability, portability, etc. As such, Python is slow compared to C or Fortran and it does not manage memory well. These limitations in speed and memory management may not be significant when analyzing small data sets, but it becomes a bottleneck when analyzing big data sets. Techniques based on vectorization, parallelization, just in time compilation, and distributed task executions have been widely adopted by the Python community to address these challenges associated with big data. In these examples, we will address a few techniques suitable for large scale data analysis and answer the following questions: 
 - How to speed up the data analysis?
   - NumPy, Numba, and Dask
 - What to do when the data set size exceeds the available physical memory? 
   - Dask Arrays, Bags, and Dataframes 
 - How to distribute the workloads when doing machine learning for big data sets?
   - Dask Machine Learning (API to Scikit-Learn, PyTorch, Tensorflow, and Keras)

You can execute the example notebooks in Binder Hub or Google Colab. 


[![Binder](http://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dmbala/binder-PyML/main)
or
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dmbala/python-bigData)
