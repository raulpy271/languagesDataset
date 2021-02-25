# Datasets with programming languages info

![Script mining data](/assets/extracting-languages-info.gif)

---

The goal of this repository is mining information to create datasets about programming languages. 

**Now the dataset has more than 600 languages**, 

which include the website of the languages, creation date, your paradigms, and type systems.

Besides, I have the goal to include information about the trends of each language, so, feels free to send suggestions about how to do it, or make it and send a pull request.

## Using the dataset

The following code query the newest programming languages:

```py
>>> from datasets import languages
>>> languages.sort_values('first_release', ascending=False, inplace=True)
>>> languages[['name', 'first_release']].head()
               name  first_release
494  project verona           2019
65           bosque           2019
582          source           2017
507              q#           2017
51        ballerina           2017
```

If you want to see more examples of the usage, see [this](/queries_examples.ipynb) page.

## How to use the dataset

The dataset is stored in `.csv` format inside the [datasets](/datasets/) directory, so, you only need to paste the link of the file:

```py
import pandas as pd
df_link = 'https://gist.githubusercontent.com/raulpy271/d2721c377c6c36926e4524c9f576b47b/raw/1efbd562e79671de0d9c7689e7162e0782a94ef7/languages.tsv'
df = pd.read_csv(df_link, sep='\t')
```

The above code can be used in [Jupyter](https://jupyter.org/), in [google colab](https://colab.research.google.com/), or in whatever environment that you have since you have pandas installed.

Another option is to clone this repository and imports the datasets from the top-level package:

```py
from datasets import languages
```

## How to setup the script

If you want to run this module to create in your pc the dataset with languages you need to install the dependencies and setup some configuration.

To install the dependencies, clone the repo and type and your terminal:

```sh
pip install -r requirements.txt
```

After installing the dependencies, you should configure the following:

This module use [selenium](https://www.selenium.dev/) to communicate with a web browser and navigate through the sites, so, you should install a web driver for help selenium to communicate with you browser, see [this](https://selenium-python.readthedocs.io/installation.html) tutorial if you don't know. 

After the download of your driver, you should tell the selenium where are the binaries of the driver and the browser, to make it, change the function [get_driver](/src/driver.py), which create instances of a driver.

After making the bellow configuration, you can run the module:

```sh
python main.py
```

With this command the script will navigate through Wikipedia searching all languages info, after the end of the process, the datasets will be saved in a path defined in the [consts.py](/src/consts.py) file, you can change it.

Besides, if you want only to test the script and you don't want to wait for the entire process, so there is a way to search only the first languages. The way is defining an environment variable called `TESTING` which has a `True` value. To define this variable use the [.env](https://pypi.org/project/python-dotenv/) file.
