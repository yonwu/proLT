usage: wiki_query.py [-h] -item ITEM [ITEM ...]

Mining Wikipedia.

optional arguments:
  -h, --help            show this help message and exit
  -item ITEM [ITEM ...]
                        contend to be searched

# Example:
  python3 wiki_query.py -item Miloš Zeman
  python3 wiki_query.py -item Bob
  python3 wiki_query.py -item 1

# Explanation

## This script can deal with input information that contains space, for example: python3 wiki_query.py -item Miloš Zeman
## This script transform all the input to string, so a searching of string, numbers, or mixed can be performed.
## The script use -item as reburied parameter for easy reading of the command