# python-BigData

Main concepts: 

- vectorizations
- Just-in-time compilation
- Parallelization
- Distributed task executions

Major Tools:

- numpy
- pandas
- numba
- dask
  - dask frame
  - dask array
  - dask machine learning

 Python is a popular programming language for developing software and data science applications. Its popularity stems from many factors such as simplicity, readability, portability, etc. As such, Python is slow compared to C or Fortran and it does not manage memory well. These limitations in speed and memory management may not be significant when analyzing small data sets, but it becomes a bottleneck when analyzing big data sets. Techniques based on vectorization, parallelization, just in time compilation, and distributed task executions have been widely adopted by the Python community to address these challenges associated with big data. This presentation will address a few techniques suitable for large scale data analysis and answer the following questions: What to do when the data set size exceeds the available physical memory? How to speed up the data analysis? How to distribute the workloads when doing machine learning for big data sets?

