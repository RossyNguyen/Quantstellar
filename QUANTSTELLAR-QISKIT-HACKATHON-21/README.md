QUANTSTELLAR 
==============================

Studies of Star, Galaxy and Quasar Systems Using QSVM.

We aim to demonstrate the quantum enhancement of QSVM for big data applications on a novel domain of astronomical objects classification using SDSS (Sloan Digital Sky Survey) dataset. We will benchmark our implementation against a classical SVM algorithm comparing time complexity, accuracy and robustness. 

**Usecase**: 
Studies of Star, Galaxy and Quasar Systems often result in vast quantities of high-dimensional data. Both big data analysis and feature mapping are computationally intensive and inefficient classically. These issues are not unique to astronomy but present in many fields. Using QSVM we can take advantage of the large dimensionality of quantum feature space to provide exponential improvements. 

**Dataset decription:** 
"The Sloan Digital Sky Survey has created the most detailed three-dimensional maps of the Universe ever made, with deep multi-color images of one third of the sky, and spectra for more than three million astronomical objects.The data consists of 10,000 observations of space taken by the SDSS. Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar." - SDSS

**Relevant Researchs:**

https://github.com/Qiskit/qiskit-tutorials/blob/master/tutorials/machine_learning/01_qsvm_classification.ipynb //
https://indico.in2p3.fr/event/22938/contributions/93156/attachments/63074/86666/Fink_Moller_MLIN2P3.pdf //
https://www.kaggle.com/lucidlenn/sloan-digital-sky-survey //

Project Structure Reference
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
