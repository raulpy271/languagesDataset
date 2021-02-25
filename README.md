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

## How to setup the script
