# Katharina

In January 1734, he (Leonhard Euler) married Katharina Gsell (1707–1773) [^1]

This tool helps selecting next problems to solve on [Project Euler](https://projecteuler.net/).

## Setup

1. Copy `.env.example` to `.env` and fill your Project Euler session id. You can get this id by logging in to Project Euler and looking at the cookies.

2. Install the project with `poetry install`.

3. Run `poetry run katharina` to get the suggestions.

To have the command `katharina` available everywhere install using `python3 -m pip install --user -e .`

## Usage

You can filter and sort problems by problem id (`pid`), difficulty, authors and solved status.

```
❯ katharina 'difficulty == 30 | solved | sort authors asc'
  problem_id  title                             difficulty    authors  solved
------------  ------------------------------  ------------  ---------  --------
         832  Mex Sequence                              30        274  True
         839  Beans in Bowls                            30        329  True
         770  Delphi Flip                               30        490  True
         612  Friend Numbers                            30        700  True
         555  McCarthy 91 Function                      30        720  True
         581  $47$-smooth Triangular Numbers            30        894  True
         371  Licence Plates                            30       1713  True
         321  Swapping Counters                         30       1811  True
         293  Pseudo-Fortunate Numbers                  30       3116  True
         204  Generalised Hamming Numbers               30       7650  True
         173  Hollow Square Laminae I                   30       9490  True
         113  Non-bouncy Numbers                        30      11717  True
         123  Prime Square Remainders                   30      12152  True
         116  Red, Green or Blue Tiles                  30      12792  True
         119  Digit Power Sum                           30      13033  True
         108  Diophantine Reciprocals I                 30      13386  True
          95  Amicable Chains                           30      15327  True
         100  Arranged Probability                      30      17414  True
          78  Coin Partitions                           30      18138  True
```

```
❯ katharina 'pid <= 200 | not solved | sort difficulty asc'
  problem_id  title                                     difficulty    authors  solved
------------  --------------------------------------  ------------  ---------  --------
         154  Exploring Pascal's Pyramid                        65       2801  False
         165  Intersections                                     65       2758  False
         168  Number Rotations                                  65       2822  False
         196  Prime Triplets                                    65       2720  False
         200  Prime-proof Squbes                                65       2518  False
         156  Counting Digits                                   70       2599  False
         163  Cross-hatched Triangles                           70       1940  False
         170  Pandigital Concatenating Products                 70       2115  False
         175  Fractions and Sum of Powers of Two                70       1894  False
         176  Common Cathetus Right-angled Triangles            70       2010  False
         189  Tri-colouring a Triangular Grid                   70       2170  False
         199  Iterative Circle Packing                          70       2064  False
         167  Investigating Ulam Sequences                      75       1804  False
         180  Golden Triplets                                   75       1675  False
         184  Triangles Containing the Origin                   75       1749  False
         194  Coloured Configurations                           75       1485  False
         177  Integer Angled Quadrilaterals                     80       1362  False
         198  Ambiguous Numbers                                 80       1190  False
```

[^1]: https://en.wikipedia.org/wiki/Leonhard_Euler#Career
