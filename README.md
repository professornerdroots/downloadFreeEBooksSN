# Download Free E-Books From Springer Nature  

Automatically download huge lists of free PDF e-books released by Springer Nature to foster the fight against the SARS-COV-2 pandemic. Read the article from Springer Nature announcing this release [here](https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960).

## How to Run
The full list of English e-books released by Springer Nature is downloadable by just running the code, like here:
```
$ python downloadFreeEBooksSN
```
To download other free e-books from Springer Nature, provide a text file containing a book *url* per line, like here: 
```
$ python downloadFreeEBooksSN textfile
```

### Required Python Modules 
A few modules are required and can be easily installed with *pip*.
```
$ pip install lxml wget
```

## Copyright 
Copyrighted in 2020 under the terms of the GPL V3. 
