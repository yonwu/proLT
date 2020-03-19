usage: term_plotter.py [-h] --terms TERMS [TERMS ...] [--title TITLE]
                       [--path PATH] [--output OUTPUT]

plot certain terms.

optional arguments:
  -h, --help            show this help message and exit
  --terms TERMS [TERMS ...]
                        list of terms
  --title TITLE         plot title
  --path PATH           target folder
  --output OUTPUT       output file name

Example:

python3 term_plotter.py --terms "america" "united states"  --title "’America’ vs. ’United States’" --path "/Users/yonwu/proLT/assignment4/term_plotter/us_presidential_speeches/"
