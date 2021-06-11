QUANTSTELLAR 
==============================

Studies of Stars, Galaxies and Quasars Using QSVM.

We aim to demonstrate the quantum enhancement of QSVM for big data applications on a novel domain of astronomical objects classification using SDSS (Sloan Digital Sky Survey) dataset. We will benchmark our implementation against a classical SVM algorithm comparing the twwo on the basis of time complexity, accuracy and robustness. 

**Usecase**: 
Studies of Star, Galaxy and Quasar Systems often result in copious amounts of high-dimensional data. Both big data analysis and feature mapping are computationally intensive and inefficient classically. These issues are not just unique to astronomy but present in many fields like particle physics, geosciences etc. Using QSVM we can take advantage of the large dimensionality of quantum feature space to provide exponential improvements. 

**Dataset decription:** 
In this project, our main dataset are from Data Release 16 (DR16) of the Sloan Digital Sky Survey (SDSS-IV), which contains SDSS observation through August 2018. The component of DR16 included in this research is catalog data inclduing parameters measured from images and spectra, such as magnitudes and redshifts.

Main dataset: Skyserver_12_30_2019 4_49_58 PM.csv
Reference link to the dataset: https://www.sdss.org/dr16 https://www.kaggle.com/muhakabartay/sloan-digital-sky-survey-dr16


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
    ├── notebooks          <- Jupyter notebooks that contains our development and model training
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
