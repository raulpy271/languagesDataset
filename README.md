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
