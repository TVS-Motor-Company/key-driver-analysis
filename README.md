# Key Driver Analysis
---

Key Driver Analysis also known as Importance Analysis and Relative Importance Analysis. The goal of this analysis is to quantify the relative importance of each of the predictor variables in predicting the target variable. Each of the predictors is commonly referred to as a driver.

For more information on key driver analysis refer to [this blog post](https://bnriiitb.github.io/blog/key-driver-analysis/driver-analysis/importance-analysis/relative-importance-analysis/johnson-relative-weights/shapley-regression/2021/05/04/key-driver-analysis.html) 


## Installation
---
### Using pip
[![PyPi Version](https://badge.fury.io/py/key-driver-analysis.svg)](https://pypi.org/project/key-driver-analysis/)

You can install using the pip package manager by running
```sh
pip install key-driver-analysis
```

Alternatively, you could install the latest version directly from Github:
```sh
pip install https://github.com/TVS-Motor-Company/key-driver-analysis/key-driver-analysis/archive/master.zip
```

### Using conda

You can install using the conda package manager by running
```sh
conda install -c conda-forge key-driver-analysis
```
### From source

Download the source code by cloning the repository or by pressing 'Download ZIP' on this page.

Install by navigating to the proper directory and running:
```sh
python setup.py install
```


## Usage
---

```python
import pandas as pd
import key_driver_analysis as kda

df = pd.DataFrame(data={
        'age': [40, 50, 60, 10, 20, 30, 7, 80, 90],
        'salary': [123, 4423, 56563, 75545, 2345, 2346, 5534, 775, 34345],
        'no_of_cars_owned': [1, 3, 4, 2, 1, 3, 5, 3, 2],
        'no_of_mobiles_purchased': [10, 3, 5, 65, 34, 6, 21, 76, 9]
    })
    print(df)
    target = 'no_of_mobiles_purchased'
    features=set(df.columns.tolist()).difference(set([target]))
    print(f'target --> {target}')
    print(f'features --> {features}')
    rw_df = kda.relative_importance(df,
                                target=target,
                                features=features,
                                verbose=True)
    print(rw_df)
```

```text

   age  salary  no_of_cars_owned  no_of_mobiles_purchased
0   40     123                 1                       10
1   50    4423                 3                        3
2   60   56563                 4                        5
3   10   75545                 2                       65
4   20    2345                 1                       34
5   30    2346                 3                        6
6    7    5534                 5                       21
7   80     775                 3                       76
8   90   34345                 2                        9
target --> no_of_mobiles_purchased
features --> {'salary', 'no_of_cars_owned', 'age'}
(9, 4)
Dataset size before dropping nulls --> (9, 4)
Dataset size after dropping nulls --> (9, 4)
r2 score --> 0.05963122389990851
            feature  raw_rel_imp  norm_rel_imp
0            salary     0.035140     58.928857
1  no_of_cars_owned     0.019415     32.558853
2               age     0.005076      8.512289
```
## References
* [RWA Web: A Free, Comprehensive, Web-Based, and User-Friendly Tool for Relative Weight Analyses by Scott Tonidandel and James M. LeBreton](https://link.springer.com/article/10.1007/s10869-014-9351-z)
* [Relative Importance Analysis: A Useful Supplement to Regression Analysis by Scott Tonidandel and James M. LeBreton](https://link.springer.com/article/10.1007/s10869-010-9204-3)
* [Determining the Statistical Significance of Relative Weights by Scott Tonidandel et al](https://pubmed.ncbi.nlm.nih.gov/19968399/)