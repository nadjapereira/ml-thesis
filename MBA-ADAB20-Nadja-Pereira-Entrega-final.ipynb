{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6e4c2fe1",
   "metadata": {},
   "source": [
    "# Nadja Pereira \n",
    "Predição de ROAS em consulta de pesquisa (Google Merchandise Store)\n",
    "\n",
    "Pós-graduação - Analytics em Big data\n",
    "\n",
    "Coordenadores: \n",
    "Prof.ª Dr.ª Alessandra de Álvila Montini\n",
    "Prof. Dr.  Adolpho Walter Pimazoni Canton"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "732417e3",
   "metadata": {},
   "source": [
    "### Base Raw"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "08b25b77",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Keyword</th>\n",
       "      <th>Clicks</th>\n",
       "      <th>Cost</th>\n",
       "      <th>CPC</th>\n",
       "      <th>Users</th>\n",
       "      <th>Sessions</th>\n",
       "      <th>Bounce Rate</th>\n",
       "      <th>Pages / Session</th>\n",
       "      <th>Ecommerce Conversion Rate</th>\n",
       "      <th>Transactions</th>\n",
       "      <th>Revenue</th>\n",
       "      <th>ROAS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>hoodies</td>\n",
       "      <td>10184.0</td>\n",
       "      <td>8404.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4502.0</td>\n",
       "      <td>4740.0</td>\n",
       "      <td>87%</td>\n",
       "      <td>1,48</td>\n",
       "      <td>0%</td>\n",
       "      <td>7.0</td>\n",
       "      <td>884.0</td>\n",
       "      <td>-89%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Google Merchandise Store</td>\n",
       "      <td>9330.0</td>\n",
       "      <td>1660.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10301.0</td>\n",
       "      <td>20318.0</td>\n",
       "      <td>26%</td>\n",
       "      <td>7,47</td>\n",
       "      <td>5%</td>\n",
       "      <td>1072.0</td>\n",
       "      <td>133488.0</td>\n",
       "      <td>7943%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>hoody</td>\n",
       "      <td>6754.0</td>\n",
       "      <td>4920.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2674.0</td>\n",
       "      <td>2823.0</td>\n",
       "      <td>88%</td>\n",
       "      <td>1,45</td>\n",
       "      <td>0%</td>\n",
       "      <td>2.0</td>\n",
       "      <td>109.0</td>\n",
       "      <td>-98%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>youtube merchandise</td>\n",
       "      <td>6279.0</td>\n",
       "      <td>17233.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2958.0</td>\n",
       "      <td>3566.0</td>\n",
       "      <td>51%</td>\n",
       "      <td>3,49</td>\n",
       "      <td>1%</td>\n",
       "      <td>24.0</td>\n",
       "      <td>1287.0</td>\n",
       "      <td>-93%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>YouTube Merchandise Store</td>\n",
       "      <td>4711.0</td>\n",
       "      <td>6225.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3271.0</td>\n",
       "      <td>3908.0</td>\n",
       "      <td>46%</td>\n",
       "      <td>3,88</td>\n",
       "      <td>1%</td>\n",
       "      <td>44.0</td>\n",
       "      <td>2705.0</td>\n",
       "      <td>-57%</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Keyword   Clicks     Cost  CPC    Users  Sessions  \\\n",
       "0                    hoodies  10184.0   8404.0  1.0   4502.0    4740.0   \n",
       "1   Google Merchandise Store   9330.0   1660.0  0.0  10301.0   20318.0   \n",
       "2                      hoody   6754.0   4920.0  1.0   2674.0    2823.0   \n",
       "3        youtube merchandise   6279.0  17233.0  3.0   2958.0    3566.0   \n",
       "4  YouTube Merchandise Store   4711.0   6225.0  1.0   3271.0    3908.0   \n",
       "\n",
       "  Bounce Rate Pages / Session Ecommerce Conversion Rate  Transactions  \\\n",
       "0         87%            1,48                        0%           7.0   \n",
       "1         26%            7,47                        5%        1072.0   \n",
       "2         88%            1,45                        0%           2.0   \n",
       "3         51%            3,49                        1%          24.0   \n",
       "4         46%            3,88                        1%          44.0   \n",
       "\n",
       "    Revenue   ROAS  \n",
       "0     884.0   -89%  \n",
       "1  133488.0  7943%  \n",
       "2     109.0   -98%  \n",
       "3    1287.0   -93%  \n",
       "4    2705.0   -57%  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "baseraw = pd.read_csv('advertising-adwords-keywords-raw.csv', sep =';')\n",
    "baseraw.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6c44329c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clicks</th>\n",
       "      <th>Cost</th>\n",
       "      <th>CPC</th>\n",
       "      <th>Users</th>\n",
       "      <th>Sessions</th>\n",
       "      <th>Transactions</th>\n",
       "      <th>Revenue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>860.000000</td>\n",
       "      <td>859.000000</td>\n",
       "      <td>859.000000</td>\n",
       "      <td>859.000000</td>\n",
       "      <td>859.000000</td>\n",
       "      <td>859.000000</td>\n",
       "      <td>859.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>285.746512</td>\n",
       "      <td>299.527357</td>\n",
       "      <td>1.937136</td>\n",
       "      <td>108.805588</td>\n",
       "      <td>139.481956</td>\n",
       "      <td>2.916182</td>\n",
       "      <td>319.912689</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>3731.935975</td>\n",
       "      <td>1287.251085</td>\n",
       "      <td>1.340861</td>\n",
       "      <td>651.929963</td>\n",
       "      <td>961.152879</td>\n",
       "      <td>39.113873</td>\n",
       "      <td>4796.126793</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>13.500000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>58.250000</td>\n",
       "      <td>97.500000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>36.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>107632.000000</td>\n",
       "      <td>17233.000000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>13156.000000</td>\n",
       "      <td>20318.000000</td>\n",
       "      <td>1072.000000</td>\n",
       "      <td>133488.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              Clicks          Cost         CPC         Users      Sessions  \\\n",
       "count     860.000000    859.000000  859.000000    859.000000    859.000000   \n",
       "mean      285.746512    299.527357    1.937136    108.805588    139.481956   \n",
       "std      3731.935975   1287.251085    1.340861    651.929963    961.152879   \n",
       "min         0.000000      0.000000    0.000000      0.000000      0.000000   \n",
       "25%         3.000000      5.000000    1.000000      2.000000      2.000000   \n",
       "50%        13.500000     21.000000    2.000000      6.000000      6.000000   \n",
       "75%        58.250000     97.500000    2.000000     35.000000     36.500000   \n",
       "max    107632.000000  17233.000000   12.000000  13156.000000  20318.000000   \n",
       "\n",
       "       Transactions        Revenue  \n",
       "count    859.000000     859.000000  \n",
       "mean       2.916182     319.912689  \n",
       "std       39.113873    4796.126793  \n",
       "min        0.000000       0.000000  \n",
       "25%        0.000000       0.000000  \n",
       "50%        0.000000       0.000000  \n",
       "75%        0.000000       0.000000  \n",
       "max     1072.000000  133488.000000  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "baseraw.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "a74d5a15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count      859.000000\n",
      "mean       299.527357\n",
      "std       1287.251085\n",
      "min          0.000000\n",
      "25%          5.000000\n",
      "50%         21.000000\n",
      "75%         97.500000\n",
      "max      17233.000000\n",
      "Name: Cost, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "column_stats = baseraw['Cost'].describe()\n",
    "print(column_stats)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8306b12a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "column_stats = baseraw['Cost'].describe()\n",
    "\n",
    "index_str = column_stats.index.astype(str)\n",
    "values_str = column_stats.values.astype(str)\n",
    "\n",
    "plt.bar(index_str, values_str)\n",
    "\n",
    "plt.xlabel('Statistic')\n",
    "plt.ylabel('Value')\n",
    "plt.title('Summary Statistics')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "34e3c869",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "column_data = baseraw['Cost'].astype(str)\n",
    "\n",
    "plt.hist(column_data)\n",
    "\n",
    "plt.xlabel('Values')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "563e71af",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZIAAAEWCAYAAABMoxE0AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAABFvUlEQVR4nO3deXzcdZ348dc7d5rmTtqmSdqm95G0lKYphwLlkFLAgivYeoCuaxXx1lVQf+rqoi66urIu7KIgoEhBQAGhKNByYy+SNj3Su03Spp20OZo0zf3+/THfKdM0SdMmM9+Zyfv5eOSR73y+x7wnx7zn+zlFVTHGGGPOVZTbARhjjAlvlkiMMcYMiiUSY4wxg2KJxBhjzKBYIjHGGDMolkiMMcYMiiUSE/FE5Aci8ochutZoEXldRJpE5D/P4ryVInLrUMQQqkTkkyLypttxmOCzRGKCTkSWisgaETkuIh5n+/MiIm7HNgDLgSNAiqp+vedOEXlIRNpFpNnv6yOqeo2qPnwuTygiKiKT+9mfIyLPishB59gJPfbHi8iDInJMRA6JyNf6uE6uiHSKyKRe9v1ZRH5+LvGbyGeJxASViHwd+BXwM2AMMBr4HHAxENfHOdFBC/DMxgNbtf+RvHer6ki/r8f7u6CIxAwypm7gReCf+tj/A2AK3tgXAt8UkUU9D1LVA8ArwCd6xJcBLAbOKRGayGeJxASNiKQCPwQ+r6pPqmqTepWq6sdUtc057iERuU9EXhCR48BCEblWREqdT9VVIvIDv+tOcD6JL3c+ldc4CctfnIg84lRJbRGR4n7ivEhE1olIo/P9Il9cwK1434ibReTKs3jtr4rIvzjbnxSRt0TklyJSB/xARCaLyGvOcx4RkcedY193LrHRd3fT89qqelhV7wXW9fH0twA/UtV6Vd0G/Ab4ZB/HPkyPRAIsBbaoarmI3CEiu52f41YRubGP1+v7ncT4lZ38GTiP/1lEtolIvYj8TUTGO+Xi/Gw8zs9jk4gU9hGvCQGWSEwwXQjEA88M4NiPAncBycCbwHG8b4hpwLXAbSJyQ49zFuL95P0B4I4eb/QfBFY45z8L/Lq3J3U+fT8P3ANkAr8AnheRTFX9JPAo791xvDyA19GXBcAeYJTzOn8E/B1IB/KA/wZQ1Uuc4+cM5O6ml9eTDowFNvoVbwRm9XHKn4EsEXmfX9kngEec7d3A+4FU4N+AP4hIztnE5MR1A/Bt4ENANvAG8Jiz+wPAJcBUvL+vjwBHz/Y5TPBYIjHBlAUcUdVOX4GIvC0iDSJyQkQu8Tv2GVV9S1W7VbVVVV9V1XLn8Sa8bzqX9rj+v6nqcVUtB34HLPPb96aqvqCqXcDvgTl9xHgtsFNVf6+qnar6GFABXH8Wr/MbzmtqEJEjfRxzUFX/23mOE0AH3qqnsc7rHapG65HO90a/ska8Cfo0Tix/wpu0EZEpwDzgj87+P6nqQef38DiwEyg5h7g+C/xEVbc5fw8/Bs5z7ko6nPimA+IcU3MOz2GCxBKJCaajeD/tnqzuUNWLVDXN2ef/91jlf6KILBCR1SJSKyKNeNtVsnpc3/+c/Xg/ifsc8ttuARL6aJsY65zrbz+Q2+erOt3PVTXN+eoZY2+xAnwTEGCtU/X2z2fxfP1pdr6n+JWlAE39nPMwcLOIJOC9G3lRVT0AInKLiJT5EiVQyOm/h4EYD/zK7zp1eF9/rqquwnvH+D/AYRG5X0RS+r6UcZslEhNM7wBtwJIBHNuzMfuPeKuk8lU1FfhfvG88/vL9tscBB88hxoN43+T8jQMOnMO1+nPK61PVQ6r6GVUdi/fT+r3ST0+tAT+Jaj1Qw6l3YHOALf2c8wbexL4E+DhOtZZzt/Ab4AtApvMBYDOn/x7AWxUJMMKvbIzfdhXwWb+Em6aqiar6thPDPao6D28V3FTgXwf2io0bLJGYoFHVBrz16veKyIdFZKSIRInIeUDSGU5PBupUtVVESvC2ofT0/0RkhIjMAj4FnFV7guMFYKqIfFREYpzG7ZnAX8/hWgMmIjeJSJ7zsB5voulyHh8GJp7h/AS87U8A8c5jn0eA74pIuohMBz4DPHSGkB4B/gNvG8VzTlmSE1et85yfwntHchpVrcWbfD8uItHOHZZ/t+L/Be50fleISKqI3ORsz3fuQGPxJqRW3vtZmBBkicQElareDXwNb1WOB++b5P8B3wLe7ufUzwM/FJEm4HvAE70c8xqwC28X1p+r6t/PIb6jwHXA1/F+Kv8mcJ2q9tXWMVTmA2tEpBnvndeXVXWvs+8HwMNONdDNfZx/gveqsSqcxz7fx9tIvh/vz+hnqvriGeJ5BO+d2OO+3nSquhX4T7x3loeBIuCtfq7xGbx3Ekfx3lmc/P2q6p/xJqoVInIM753NNc7uFLx3PvVOzEcBG8MSwsQWtjLhTrwD8PYCsf4N+caY4LA7EmOMMYMSsEQi3ikZPCKy2a/sPBH5h9PrY71T1+3bd6eI7BKR7SJytV/5PBEpd/bdI+KdRkO80z487pSvkR7TQhhjjAmOQN6RPAT0nIbhbrx9/c/DW899N4CIzMQ7enaWc8698t60GPfhnd9oivPlu+angXpVnQz8Em99qxmGVHWfqopVaxnjjoAlElV9HW/f8FOKea8/eyrvdc9cAqxQ1TangXEXUOKMmE1R1XecuY0eAW7wO8c398+TwBW+uxVjjDHBM9jJ4s7WV4C/iXcW0SjgIqc8F/iH33HVTlmHs92z3HdOFYCqdjqD1DLxzszap6ysLJ0wYcKgXoQxxgw3GzZsOKKq2b3tC3YiuQ34qqo+5XRjfAC4kt4HNGk/5Zxh3ylEZDne6jHGjRvH+vXrzzZuY4wZ1kSk54wPJwW719atwNPO9p94b46eak4dlZyHt9qr2tnuWX7KOc5UF6mcXpUGgKrer6rFqlqcnd1rQjXGGHOOgp1IDvLeRHuX453wDbwDsJY6PbEK8Daqr3UmamsSkQuc9o9beG/m2GfxJiaADwOrzrBGhDHGmAAIWNWWiDwGXIZ3kr5qvKNrP4N3orYYvNMeLAdQ1S0i8gSwFegEbndmaQVvddhDQCKw0vkCb7XY70VkF947kaWBei3GGGP6NuxGthcXF6u1kRhjzNkRkQ2q2uuCcDay3RhjzKBYIjHGGDMolkiMMcYMiiUSE9ZeKK+hpvHEmQ80xgSMJRITtuqOt/P5R9/l3tW73Q7FmGHNEokJW2VV9QCs29frOFRjTJBYIjFhq7SyAYCKQ000tLS7G4wxw5glEhO2yqoaiI/x/gmv21fvcjTGDF+WSExY6u5WyqoauH7OWOJioli796jbIRkzbAV79l9jhsSeI800tXZSUpBBZV0La/daO4kxbrE7EhOWfO0j549LY0FBBpsPHqO5zRZINMYNlkhMWCqraiA5IYaJWSMpKcigq1t5d7+1kxjjBkskJiyVVjZwXn4aUVHC+ePSiY4Sq94yxiWWSEzYaWnvZPvhJs7LTwMgKT6GwtxUSyTGuMQSiQk75dWNdHXryUQCsKAgg7KqBlo7uvo+0RgTEJZITNgpq2oAOCWRlEzIoL2rm43OPmNM8FgiMWGnrKqBcRkjyBwZf7Js/oQMRLDqLWNcELBEIiIPiohHRDb3KP+iiGwXkS0icrdf+Z0issvZd7Vf+TwRKXf23eOs3Y6zvvvjTvkaEZkQqNdiQouvod1f6ohYpo1OZq3Nu2VM0AXyjuQhYJF/gYgsBJYAs1V1FvBzp3wm3jXXZznn3Csi0c5p9+Fd232K8+W75qeBelWdDPwS+I8AvhYTImoaT3DoWCtzx6Wdtm9BQQYb9tfT0dUd/MCMGcYClkhU9XWg58fD24Cfqmqbc4zHKV8CrFDVNlXdC+wCSkQkB0hR1XfUu7j8I8ANfuc87Gw/CVzhu1sxkavMGYjY844EoKQgk5b2LrYcPBbcoIwZ5oLdRjIVeL9TFfWaiMx3ynOBKr/jqp2yXGe7Z/kp56hqJ9AIZPb2pCKyXETWi8j62traIXsxJvjKqhqIi45i5tiU0/bNL0gHsHm3jAmyYCeSGCAduAD4V+AJ5y6itzsJ7aecM+w7tVD1flUtVtXi7Ozss4/ahIzSqgZmjk0hPib6tH2jkhOYmJVkDe7GBFmwE0k18LR6rQW6gSynPN/vuDzgoFOe10s5/ueISAyQyulVaSaCdHZ1U17d2Gu1lk9JQQZr99bR3d3rZwpjTAAEO5H8BbgcQESmAnHAEeBZYKnTE6sAb6P6WlWtAZpE5ALnzuUW4BnnWs8CtzrbHwZWOe0oJkJtP9zEiY6uXhvafeZPyOBYq3fkuzEmOAI2jbyIPAZcBmSJSDXwfeBB4EGnS3A7cKvz5r9FRJ4AtgKdwO2q6huifBveHmCJwErnC+AB4PcisgvvncjSQL0WExp8M/7OzU/v85iSggzAO55kRs7p7SjGmKEXsESiqsv62PXxPo6/C7irl/L1QGEv5a3ATYOJ0YSXsqoGMpPiyM9I7POYvPRExqYmsHZvHbdeNCF4wRkzjNnIdhM2yqq8AxH76+UtIpQUZLBmbx1W02lMcFgiMWGh8UQHuzzN/Ta0+5QUZHKkuY29R44HPjBjjCUSEx42VTcAMHdc3+0jPr52knU2XYoxQWGJxISF0soGRGB2fuoZj52UnURmUhxrbDyJMUFhicSEhbKqBiZnjyQlIfaMx/raSWxgojHBYYnEhDxVPdnQPlAlBRlU15/gQMOJwAVmjAEskZgwUFnXQt3xds7rZyBiTyfbSeyuxJiAs0RiQp5vRcT+BiL2NH1MCskJMdZOYkwQWCIxIa+0soHE2Gimjh454HOio4T5EzJsJmBjgsASiQl5pVUNzM5LJSb67P5cSwoy2F17nCPNbQGKzBgDlkhMiGvr7GLbwWNn1T7iY+0kxgSHJRIT0rYcPEZ7Vzdzz6LHlk/h2FQSY6OtncSYALNEYkKab2ndgYxo7ykuJorzx6fZeBJjAswSiQlppVUN5KQmMDol4ZzOL5mQybZDx2g80THEkRljfCyRmJBWVlV/VgMReyopyEAVNuy3uxJjAsUSiQlZR5rbqKo70e+KiGcyd1wasdFi7STGBFDAEomIPCgiHmc1xJ77viEiKiJZfmV3isguEdkuIlf7lc8TkXJn3z3Okrs4y/I+7pSvEZEJgXotxh2+9pHzzmIgYk8JsdHMybN2EmMCKZB3JA8Bi3oWikg+cBVQ6Vc2E+9SubOcc+4VkWhn933AcrzruE/xu+angXpVnQz8EviPgLwK45qyqgaio4Si3DPP+NufkoIMyqsbaWnvHKLIjDH+ApZIVPV1vGup9/RL4JuA//J1S4AVqtqmqnuBXUCJiOQAKar6jrO2+yPADX7nPOxsPwlcIf0tnWfCTmlVPdPHJJMYF33mg/tRUpBBZ7eeXPPdGDO0gtpGIiIfBA6o6sYeu3KBKr/H1U5ZrrPds/yUc1S1E2gEMvt43uUisl5E1tfW1g76dZjA6+5WNlU1Dqqh3Wfe+HSiBGsnMSZAgpZIRGQE8B3ge73t7qVM+ynv75zTC1XvV9ViVS3Ozs4eSLjGZbtrm2lq6zyn8SM9JSfEMnNsis27ZUyABPOOZBJQAGwUkX1AHvCuiIzBe6eR73dsHnDQKc/rpRz/c0QkBkil96o0E4ZKTza0pw3J9UomZFJa2UBbZ9eQXM8Y856gJRJVLVfVUao6QVUn4E0E56vqIeBZYKnTE6sAb6P6WlWtAZpE5AKn/eMW4Bnnks8CtzrbHwZWOe0oJgKUVjWQkhDDxKykIbleSUEGbZ3dlFc3Dsn1jDHvCWT338eAd4BpIlItIp/u61hV3QI8AWwFXgRuV1XfR8fbgN/ibYDfDax0yh8AMkVkF/A14I6AvBDjirKqBubkpxEVNTT9J+ZP8FaRWTuJMUMvJlAXVtVlZ9g/ocfju4C7ejluPVDYS3krcNPgojSh6HhbJ9sPHeOqhZOH7JqZI+OZMmoka/fWcfvCIbusMQYb2W5CUPmBRrr13CZq7E9JQQYb9tfT2dU9pNc1ZrizRGJCjq+hfc4QNbT7lBRk0NzWybaapiG9rjHDnSUSE3LKquqZkDmCjKS4Ib2ub6GrNdYN2JghZYnEhBRV7wj0oer26y8nNZFxGSNYt88a3I0ZSpZITEipaWzF09QWkEQC3ruStXvrsJ7ixgwdSyQmpJRVNQBD39DuU1KQQX1LB7s8zQG5vjHDkSUSE1JKK+uJi4liRk5KQK6/4GQ7iVVvGTNULJGYkFJW1UDh2BTiYgLzpzkuYwSjU+JtfRJjhpAlEhMyOrq6KT/QOKiFrM5ERCgpyLR2EmOGkCUSEzK2H2qitaOb8waxtO5AlBRkcOhYK1V1JwL6PMYMF5ZITMgo9TW0B6jHls8CG09izJCyRGJCRmllPVkj48hLTwzo80zOHkn6iFhrJzHDRmtHFx/45Ws8v6kmINe3RGJCRlmVdyBioFdMjooS5k/IYK0NTDTDxDt7jrLjcDNJ8YNbtrovlkhMSGhs6WBP7fGAjR/pqaQgg/1HWzjU2BqU5zPGTasrPCTGRnPBxF5XIx80SyQmJJRVNwBDtyLimSwo8P5D2V2JiXSqyqoKDxdPziQh1u5ITAQrq2xABGbnpQbl+WbkJDMyPsbWcTcRb3dtM9X1J1g4fVTAnsMSiQkJpVX1TBk1kuSE2KA8X0x0FPPGp1uDu4l4qyo8ACycFoaJREQeFBGPiGz2K/uZiFSIyCYR+bOIpPntu1NEdonIdhG52q98noiUO/vucdZux1nf/XGnfI2ITAjUazGBpapsrArMjL/9KSnIYMfhZuqOtwf1eY0JplUVHqaPSWZsWuB6QwbyjuQhYFGPspeAQlWdDewA7gQQkZnAUmCWc869IuKrzLsPWA5Mcb581/w0UK+qk4FfAv8RsFdiAmr/0RbqWzqC1tDu4xtPYtPKm0h1rLWD9fvquTyA1VoQwESiqq8DdT3K/q6qnc7DfwB5zvYSYIWqtqnqXmAXUCIiOUCKqr6j3vksHgFu8DvnYWf7SeAKCXS/URMQpVX1QPAa2n2K8lKJi4my6i0Tsd7YcYTObg1o+wi420byz8BKZzsXqPLbV+2U5TrbPctPOcdJTo1Ar33bRGS5iKwXkfW1tbVD9gLM0CirbGBEXDRTRycH9XnjY6KZm59micRErFUVHlITYwM+W4QriUREvgN0Ao/6ino5TPsp7++c0wtV71fVYlUtzs7OPttwTYCVVjUwOy+V6Kjg31AuKMhgy8FGmlo7gv7cxgRSd7fy2g4Pl07NJiY6sG/1QU8kInIrcB3wMX1v+tVqIN/vsDzgoFOe10v5KeeISAyQSo+qNBP6Wju62FZzLKAz/vanpCCTboUN++tdeX5jAqX8QCNHmtsD3j4CQU4kIrII+BbwQVVt8dv1LLDU6YlVgLdRfa2q1gBNInKB0/5xC/CM3zm3OtsfBlapzQsedrYcPEZHlzI3wDP+9uX88WnERIlVb5mIs6rCQ5TApVMDXwsTE6gLi8hjwGVAlohUA9/H20srHnjJaRf/h6p+TlW3iMgTwFa8VV63q2qXc6nb8PYAS8TbpuJrV3kA+L2I7MJ7J7I0UK/FBE5ppfdOINB1uH0ZERdDYW6qJZIItGF/Hd0K8ydkuB2KK1Zv9zB3XDrpSXEBf66AJRJVXdZL8QP9HH8XcFcv5euBwl7KW4GbBhOjcV9ZVQO5aYmMSklwLYYFBRk8+NZeWju6AjaFhAkuT1Mrn/rdOkbExfD2HZcT5UL7m5s8Ta1sqm7kGx+YGpTns5HtxlWllcEfiNhTSUEGHV1KaWWDq3GYofPD57ZyrLWTQ8daT65zM5y8ut3bOzXQ3X59LJEY19Q2tXGg4YTriaR4fAYiWPVWhFhd4eGvm2r4zPsLiIuO4oXywKzBEcpWV3gYk5LAzJyUoDyfJRLjmjLfioguNbT7pI6IZfqYFNbuswkcw11Leyff/ctmJo8ayTeunsb7p2SxsryG4dQPp6Ormzd2HmHh9OyAr+3jY4nEuKa0sp6YKKEwNzgz/vZnQUEG7+5voKOr2+1QzCD88qUdHGg4wU8+VER8TDSLi3I42Nh68kPLcLBuXx3NbZ0BnaSxJ0skxjVlVQ1Mz0kOiQbukoIMTnR0sflAo9uhmHO0+UAjD7y5l2Ul40721Lpy5mhio2VYVW+trvAQFx3FxZOzgvaclkiMK7q6lU3Vjcx1aSBiT743HmsnCU+dXd3c+XQ5GUnx3LFo+sny1MRY3jc5ixfKDw2b6q1VFR4WTMwgKT5gnXJPY4nEuGKXp5nmtk7XG9p9spPjmZidZIkkTD38zn7KDzTy/etnkjri1DVtFhflcKDhBJuqI/9us/JoC7trjwe1WgsskRiXlDkz/rrd0O5vQUEGa/fV0dU9PD65RooDDSf4z79vZ+G0bK6bnXPa/qtmjiYmSnhhc+RXb62qOAwQlGlR/FkiMa4orWwgNTGWgqwkt0M5qaQgg6bWTrYfanI7FDNAqsr3/rIZVfjhksJeeymljYjj4slZvDAMem+t2l7LxKwkJgT5/8oSiXFFWVUDc/LTgtY9cSBKCryrENg67uFj5eZDvFLh4WtXTSU/Y0Sfxy0uGkNV3Qm2HDwWxOiCq6W9k3/sORq0QYj+LJGYoGtu62TH4SbX5tfqS25aIrlpiay1FRPDQuOJDn7w7BZmjU3hUxdP6PfYD8wcQ3SU8HwE9956e9dR2ju7g16tBZZIjAs2VTfQrXBeCLWP+CwoyGDt3rqIrwKJBHe/WMGR5jZ++qHZZ1xvIz0pjosmZUZ09daq7R6S4qJdmaTSEokJOt/gsPPy0lyNozclBRkcaW5nz5Hjbodi+rFhfx2PrqnkkxcVUJQ3sAGti4ty2H+0ha01kVe9paqsrvDwvilZxMUE/23dEokJutLKBgqykoIyvfXZKimw8SShrr3TO2YkNy2Rr5/F7LZXz/JWb0Xi4MSKQ03UNLa6Uq0FlkhMkKkqZVXuz/jbl4KsJLJGxlsiCWH3v76bHYeb+eGSWWc16C4jKY4LJmZE5ODEVRUegKCPH/EZcCIRkdDpp2nC1sHGVmqb2kJq/Ig/ETnZTmJCz94jx7ln1S4WF43hihmjz/r8xUU57D1ynIoI6+L96nYPhbkprq3rc8ZEIiIXichWYJvzeI6I3DuA8x4UEY+IbPYryxCRl0Rkp/M93W/fnSKyS0S2i8jVfuXzRKTc2XePs+QuzrK8jzvla0Rkwtm9dOMG34qIoXpHAjB/QjoHGk5QXd9y5oNN0Kgq3366nPiYKH5w/axzusbVs8YQJbAygqq3Glra2bC/nstduhuBgd2R/BK4GjgKoKobgUsGcN5DwKIeZXcAr6jqFOAV5zEiMhPvUrmznHPuFRHfTH73AcvxruM+xe+anwbqVXWyE+N/DCAm47KyygbiY6KYPiY46ySci/fGk9hdSSh56t0DvLPnKN9aNP2cP3lnjYxnQUEmz0dQ763XdtTSrcFbxKo3A6raUtWqHkVdvR546jmv411L3d8S4GFn+2HgBr/yFarapqp7gV1AiYjkACmq+o56f+uP9DjHd60ngSt8dysmdJVWNVCYm+pKz5KBmjYmmZSEGEskIeRocxt3Pb+VeePT+WjJuEFda3HRGHbXHmfH4eYhis5dqys8ZCbFMcfFXpAD+W+uEpGLABWROBH5Bk411zkYrao1AM53XwrNBfyTVbVTluts9yw/5RxV7QQagczenlRElovIehFZX1tbe46hm8Hq6Opm84HGkK7WAoiOEuZPsHaSUHLX89tobuvkJx8qGvT661cXjkGEiOi91dWtvLajlkunZru6Lv1AEsnngNt57039POfxUOrtJ6D9lPd3zumFqverarGqFmdnZ59jiGawKmqaaOvsDtmGdn8lBRnsOXIcT1Or26EMe2/uPMLTpQf47CWTmDo6edDXG5WcwPwJGRGRSMqq6qlv6XC1WgsGkEhU9YiqfkxVR6vqKFX9uKqe62REh53qKpzvHqe8Gsj3Oy4POOiU5/VSfso5IhIDpHJ6VZoJIaVVod/Q7uMbT7Jub73LkQxvrR1dfOcv5RRkJfGFyycP2XWvLcphp6eZnYfDu/fWqgoP0VHCJVPd/YA8kF5bv3N6YJ3ydY7P9yxwq7N9K/CMX/lSpydWAd5G9bVO9VeTiFzgtH/c0uMc37U+DKzSSGk9i1BllQ1kJ8eTm5bodihnVJibSmJstE3g6LJ7XtnJ/qMt3HVD4ZCupLnoZPXWoSG7phtWV9Qyb3w6qYmxZz44gAZStfVX4Hnn6xUgBThjK5WIPAa8A0wTkWoR+TTwU+AqEdkJXOU8RlW3AE8AW4EXgdtV1degfxvwW7wN8LuBlU75A0CmiOwCvobTA8yErlJnIGI49ImIjY5i3vh01lg7iWsqDh3j/tf38E/n53HREC8bOzolgeLx6awM4zVKDjW2srXmmGuj2f2dcVioqj7l/9hJEC8P4Lxlfey6oo/j7wLu6qV8PVDYS3krcNOZ4jChoaGlnb1HjvPheXlnPjhElBRk8MuXd9DQ0k7aiNCbziWSdXcrdz5dTkpiLN+5dkZAnmNxUQ7/9txWdtc2Myl7ZECeI5BWb/e2DIRCIjmXPphTgMH1vzPDjm+ixnBoaPcpKchAFdbvs3aSYHt0zX5KKxv47rUzyAjQnGyLCscA4Ts4cVWFh9y0RKaMcj8JDqSNpElEjvm+A88B3wp8aCaSlFY2IAKzQ3DG376cl59GXHSUrU8SZIePtXL3i9u5eHImN87NPfMJ5ygnNZF549N5PgzbSdo6u3hr1xEWTs8OiarigfTaSlbVFL/vU3tWdxlzJmVVDUwdlczIs5hkz20JsdHMyU+1dpIg+8GzW2jv6uauG4oC/iZ5TeEYttUcY2+YLRuwZk8dLe1dIVGtBf0kEhE5v7+vYAZpwptvxt9wqtbyKSnIYPOBRo63dbodyrDw0tbDrNx8iC9dMSUo644vLsoBwm9w4urtHuJjorhw4tB2QjhX/X08/M9+9ilw+RDHYiLU3iPHaTzRERbjR3oqKcjkf1bvprSygfdNCY1/2kjV3NbJ957ZzLTRySy/ZGJQnnNsWiJzx6XxQnkNty8cunEqgba6wsNFkzJJjBu6LtGD0WciUdWFwQzERK73GtrT+z8wBM0bn06UwNq9Ry2RBNjP/7adQ8da+fVHzyf2DEvnDqXFhTnc9cI29h89zvjM0F8tY09tM/uOtvDp9xW4HcpJA/ptiUihiNwsIrf4vgIdmIkcpZUNJMVFMzkEepecrZHxMRTmWjtJoG2sauDhd/bx8QXjmTc+uB84riny9t4Kl8GJvkWsLnNx2vieBtJr6/vAfztfC4G7gQ8GOC4TQcqqGpidl0a0i5PKDUbJhAxKqxpo6zzjpNfmHHR0dXPH0+WMSo7nXxdNC/rz56WPYE5eatgMTly93cOUUSPJzxjhdignDeSO5MN4BxEeUtVPAXOA+IBGZSJGa0cX22qOhWVDu09JQQbtnd1sqm50O5SI9OCbe9lWc4x/++AsUhLcmepjcVEOm6obqaoL7cXMmts6Wbu3LmR6a/kMJJG0qmo30CkiKXgnWgxOS5gJe5sPNNLZrWHZ0O4zf4J3AkebVn7oVdW18MuXd3DljNFcPWuMa3GES++tN3fW0tGlrs/221N/3X9/LSIXA2tFJA34DbABeBdYG5zwTLjzNbSfF8Z3JOlJcUwbnWztJENMVfnuXzYTLcIPl8xydWBdfsYIinJTeWFzaLeTrK6oJTkhJujtSGfS3x3JTuDnwHXAncA/8E60eKtTxWXMGZVWNpCblsio5HNbGjVUlBRksGFfHZ1d3W6HEjGe3XiQ13bU8o2rpzE2BGaEvqZoDBurGqiuD83qLVVl9XYPl0zNDmqvtoHoMxpV/ZWqXoh3ffY64Hd4Z969QUSmBCk+E+bKqhrC+m7Ep6Qgg+PtXWytOeZ2KBGhoaWdH/11K3PyUrnlwgluhwN41ygBeDFE70q2HDyGp6mNy0Oot5bPQKZI2a+q/6Gqc4GPAjcCFQGPLMTsPNzE/7222+0wwornWCsHGk4wN4zbR3x8C11ZO8nQ+OnKCupbOvjxh4pCpjff+MwkZo1N4fkQbSdZVeFBBC6dFnqrvA6k+2+siFwvIo/ivSPZAfxTwCMLMa/tqOUnKyvYfii8V1QLptIwnPG3L6NTEhifOcLaSYbAmj1HWbGuin95XwGzxqa6Hc4pFhflUFrZwMGGE26HcppVFR5m56WRNTL0Os3219h+lbMSYjWwHHgBmKSqH1HVvwQpvpDxofPziIuO4rG1lW6HEjbKqhqIjZaQe7M4VyUTMli3r47ubluI81y1dXZx55/LyUtP5MtXhl4N+TW+qeVDrHrraHMbG6sbQrJaC/q/I/k23hUOZ6jq9ar6qKoOyRSZIvJVEdkiIptF5DERSRCRDBF5SUR2Ot/T/Y6/U0R2ich2Ebnar3yeiJQ7++6RAHb7yEiK4+rCMTz9bjWtHTYwbSBKK+uZkZMypEukuqmkIIOGlg52es64QKjpw72rd7On9jj/fkMhI+JCbyboidkjmT4mOeS6Ab+6vRbV0FjEqjf9NbYvVNXfqOqQ3suLSC7wJaBYVQuBaGAp3qVyX1HVKXiX9L3DOX6ms38WsAi4V0R870z34b1bmuJ8LRrKWHtaNj+fY62dYTMC1k1d3Up5dWNYjx/paUFBJoCt436Odnmaue/V3XxwztiQmt6jp2uLctiwv55Dja1uh3LS6u0espPjmTU2xe1QeuVWH7IYIFFEYoARwEFgCfCws/9h4AZnewmwQlXbVHUv3rXbS0QkB0hR1XdUVYFH/M4JiAsmZjI+cwSPra0K5NNEhJ2eJo63d0VE+4hPfkYiY1ISrJ3kHHR3K99+upyE2Cj+33Uz3Q6nX9c4vbdC5QNjZ1c3r++oZeG0bKJCpGNCT0FPJKp6AO/4lEqgBmhU1b8Do1W1xjmmBvB9ZMkF/N+5q52yXGe7Z/lpRGS5iKwXkfW1tbXnHHtUlPCR+fms3VvH7lqr3uhPaWUDAOflh9bAqcEQEUoKMli7tw7vZxczUE+sr2Ltvjq+c+0MspNDr7HY3+RRI5k2OpmVITKJ44b99Rxr7QzZai1wIZE4bR9LgAJgLJAkIh/v75ReyrSf8tMLVe9X1WJVLc7OHlzXuQ/PyyMmSnh8nd2V9KessoG0EbFMyAydieWGQklBBp6mNvYfDc1Ba6GotqmNH7+wjZKCDG4uznc7nAG5pmgM6/bX4TnmfvXWqu0eYqOFiyeH7jIGblRtXQnsVdVaVe0AngYuAg471VU43z3O8dWA/19fHt6qsGpnu2d5QI1KTuDKGaN5akM17Z02yrkvpVX1nJefFhLrSQ+lBTae5Kz96K9bae3o5sc3Bn7p3KFybVEOqvDiFvfvSlZXeJg/IYNklya0HAg3EkklcIGIjHB6WV0BbAOeBW51jrkVeMbZfhZYKiLxIlKAt1F9rVP91SQiFzjXucXvnIBaWpLP0ePtvLT1cDCeLuw0tXp7NkVSQ7vP5FEjyUiKs3aSAXp1u4dnNx7k8wsnhdV6NFNGJzNl1Eie3+RuO0l1fQs7DjeHdLUWuNNGsgZ4Eu/kj+VODPcDPwWuEpGdeOf0+qlz/BbgCWAr8CJwu6r6+t/eBvwWbwP8brwDJgPu/VOyyU1LZMU6G1PSm/LqRlTDc0XEMxER5k9IZ+0+67l1Ji3tnXz3L5uZlJ3EbZdNcjucs3ZNUQ5r99XhaXKvemv1dm+bbqjN9tuTK722VPX7qjpdVQtV9RNOj6yjqnqFqk5xvtf5HX+Xqk5S1WmqutKvfL1zjUmq+gUNUgtodJRwc3E+b+w8QqXVlZ/GN6L9vLw0V+MIlJKCTKrqToTk6OdQ8quXd1Jdf4If31hEfEz4jSXyVW/9bYt7NQ+rKzyMzxzBxKzQXgI4tKaQDCM3z88jSuDx9XZX0lNpZQMTs5JIHRG6dbqD4WsnWbfPqrf6suVgI799cy9L5+ezYGKm2+Gck6mjRzIxO4kXXKreau3o4u3dR1g4bVTIty1ZIjlHOamJXDZtFH9aX21Ti/tRVcqq6iNixt++zMhJYWR8jLWT9KGrW7nz6XLSR8Ry5zUz3A7nnIkI1xblsGbvUY40twX9+d/ZfZTWju6Qbx8BSySDsnR+Pp6mNlZVeM588DBRXX+CI83tETHjb1+io4TiCenWc6sXXd3KT1duY1N1I9+7flbY35VeU5hDt8LfXOi9tarCQ2Js9MmZp0OZJZJBuHz6KEYlx7PCxpScVHZyxt/Ia2j3V1KQwS5PsyufVENVbVMbn3hgDb95Yy/LSsZx/ewct0MatBk5yRRkJQV9cKKqsqrCw8WTs8JirjpLJIMQEx3FzcX5vLrdQ02jNbyCt30kPiaKaWOS3Q4loHztJOutnQTwTg1/7T1vsGF/PXd/eDY/+VD4jBnpj4iwuGgM7+w5St3x9qA9705PMwcaToRFtRZYIhm0j8zPp1vhiXXVZz54GCirqqcoNzXklgIdakW5acTHRLF2b73bobiqu1u599VdLPvNPxgZH8Nfbr84bEavD9Q1hTl0dWtQq7dWO9XlC6eH3iJWvYns//YgyM8YwfunZPH4ukq6hvk6Fe2d3Ww+eCyiJmrsS1xMFOePG97jSeqPt/Mvj6zn7he3c01RDs984WJm5ITm7LSDMWtsCuMzRwR1avlVFR5m5KSQk+r+WvYDYYlkCCydP46Dja28vvPcJ4SMBNtqjtHe2R1REzX2p6Qgg60Hj3GstcPtUIKutLKe6/77Td7YWcsPl8zi18vmhvQUHoMhIlxTmMPbu49SH4TqrcYTHazfX8/lYXI3ApZIhsRVM0eTmRTHimG+emJZBC2tOxALCjLoVu/srMOFqvLgm3u5+f/eQQSe/NxF3HLhhIhoD+nPtUXe6q1gTIv0xs5aurqVhSG8ZktPlkiGQFxMFP80L49XtnlcnU7BbaWV9YxKjicnNcHtUIJi7rh0YqJk2HQDPtbawecffZcf/nUrl04dxfNffD9zIribt7/C3BTy0hN5PgjVW6sqPKSNiA2rno+WSIbI0vn5dHYrT24Yvo3uZVUNETnjb18S46KZnZc6LBLJloONfPC/3+TvWw/z7cXT+c0t88J+jMjZ8A1OfGvXERpbAleV2d2tvLa9lkunZhMdootY9cYSyRCZmD2SBQUZPL6uiu5h2Ohed7ydfUdbwupT1FAoKchkU3UDJ9q7znxwGFJVHltbyY33vk1rRzePL7+A5ZdMGjYfFvxdU5RDZ7fy962B6721sbqBo8fbw6bbr48lkiG0rGQc+4+28I89w68nz0bfRI3DpKrDp6QgnY4upbQq8tpJWto7+foTG7nz6XIWFGTw/JfeR/GE0B9lHShz8lLJTUtk5ebAJZLV22uJErh0avg0tIMlkiG1qHAMqYmx/HEYNrqXVjUQJTA7L9XtUIJq3vgMRCJvoaudh5tY8uu3+HPZAb565VQe+lQJmSNDe4ncQPMNTnxjZy2NJwJTvbW6wsP549JJGxEXkOsHiiWSIZQQG82Nc3P5+5bDQR0FGwpKK+uZOjqZpPgYt0MJqtTEWGaMSYmoRPKX0gN88NdvUd/Szh8+vYAvXzklrOrrA+maohw6upSXA9B7y3OslfIDjSG/9khvLJEMsWUl42jv6ubpd4dPo3t3t7KxqmHYdPvtqaQgg3cr68N+6eXWji7ufLqcrzxeRlFeKs9/6f0hvU64G+bmpzE2NYGVm4e+99arvkWswqjbr48lkiE2bUwyc8el8djaSoK0zpbr9hw5zrHWTuYOk4GIPS0oyKC1o5ufrqxgl6fJ7XDOyb4jx/nQvW/z2NpKbrtsEn/8lwWMThke3bjPhoiwqDCH13ccGfKBqKsqPOSkJjAjJ/zmqXMlkYhImog8KSIVIrJNRC4UkQwReUlEdjrf0/2Ov1NEdonIdhG52q98noiUO/vukRDpSrJs/jh21x5n/TAZqOYbiBjJa5D059Jp2Vw+fRS/e3svV/7idRb91+v8z+pdYbN65sryGq7/7zc50HCCBz9ZzLcWTScmwudKG4xrZ4+hvaubVduGbvmI9s5u3tx1hMvCYBGr3rj11/Ir4EVVnQ7MAbYBdwCvqOoU4BXnMSIyE1gKzAIWAfeKiG9e5fuA5cAU52tRMF9EX66bk8PI+BgeGyaN7mVV9STHxzA5e6TbobhiRFwMD35yPmvuvIIfXD+TpPgYfva37Vzys9Us+Z+3+O0be0Jyduj2zm7+7bkt3Pbou0wcNZLnv/Q+Lp8+2u2wQt7c/HTGpCQM6eDE9fvqaG7rDLtuvz5BTyQikgJcAjwAoKrtqtoALAEedg57GLjB2V4CrHDWdd8L7AJKRCQHSFHVd5y12h/xO8dVI+JiWHLeWF4orwlY745QUlrZwOz8VKKGeYPsqJQEPnlxAU/ddhFvfmshd14zna7ubv79+W1c+JNV3Py/7/D7d/aFxBomBxpOcPP/vcPv3trHJy+awJ8+eyF56SPcDissREUJiwrH8NqOWprbOofkmqsqPMTFRHHx5PBcltiNO5KJQC3wOxEpFZHfikgSMFpVawCc777UnAv4rxxV7ZTlOts9y08jIstFZL2IrK+tDc7EistKxtHa0c0zZQeC8nxuOdHeRcWhpmE3fuRM8tJH8NlLJ/HXL76fVV+/lK9dNZW6lnb+3zNbKLnrZT7xwBqeWFcV0FHSfVld4eHae95gl6eZez92Pj/44CziYqwq62wsLsqhvbObV7YNTe+tVds9XDAxkxFx4dnr0Y2/nhjgfOA+VZ0LHMepxupDbx9ztZ/y0wtV71fVYlUtzs4OzkCfwtxUCnNT+OOayG50Lz/QSFe3DtuG9oGYmD2SL10xhZe+egkvfuX9fP6yyew/2sI3n9pE8V0v8S8Pr+OZsgMcH6JPt33p7Orm7hcr+NRD68hJTeS5L76PxUXhv4qhG4rHpzMqOX5Ippbff/Q4e2qPs3BaeA1C9OdG+qsGqlV1jfP4SbyJ5LCI5KhqjVNt5fE73n+lnDzgoFOe10t5yFg6fxzf/ctmNlY3Ruwn9jJnRPdwbWg/GyLC9DEpTB+Twtc/MJXyA408t/Egf91Uw8vbPCTERnHF9NFcPyeHy6aNGtIlVj3HWvniY6Ws2VvHspJ8vn/9rLBYwjVURUUJ1xSOYcW6Ko63dQ5q/NQqZxGrcG0fARfuSFT1EFAlItOcoiuArcCzwK1O2a3AM872s8BSEYkXkQK8jeprneqvJhG5wOmtdYvfOSFhyXljSYyNjujp5cuqGshLTyRrmI96Plsiwuy8NL5z7Uze+tbl/OlzF3JzcT5r9h7lc394l+J/f5mvPV7G6grPoMenvL3rCIvveZNN1Y384uY5/ORDsy2JDIFrinJo6+w+mQjO1aoKDxOzkxifmTREkQWfWxVyXwQeFZE4YA/wKbxJ7QkR+TRQCdwEoKpbROQJvMmmE7hdVX0z5N0GPAQkAiudr5CRnBDLdbNzeHbjQb573UxGRuCo79LKhmE9/9JQiIoS5k/IYP6EDL533Uz+saeO5zYeZOXmGp4uPUBqYizXFI7h+jljuWBi5oBHmXd3K79evYv/enkHE7NH8sfPLGDq6PAboxCq5k/IIGtkPCs313D9nLHndI3jbZ2s2VPHLReOH+LogsuVdzZVLQOKe9l1RR/H3wXc1Uv5eqBwSIMbYssWjONPG6p5buNBlpWMczucIXX4WCs1ja0RW23nhpjoKN43JYv3TcniRzcU8sbOWp7beJDnNh5kxboqskbGc22RN6mcPy69z55yR5vb+OoTG3l9Ry03nDeWu24sGnbT1wRadJSwqHA0T26opqW985wayt/efZT2ru6wrtYC9+5Iho25+WlMG53MirWVEZdISisbgOGzImKwxcVEccWM0VwxYzQn2rtYvd1zMqE8/M5+xqYmcN2csVw/eyyFuSknB7Jt2F/H7Y+WUtfSzo9vLGJZSX5YDnILB4uLcvjDPyp5dXvtOXVcWFXhYWR8TNjf1VsiCTARYWlJPv/23Fa2HGxk1tjImR23tKqe2GhhZk6K26FEvMS4aBYX5bC4KIem1g5e3naY5zbW8OCbe7n/9T1MyBzB9XPGEh8TxX+9vJOxaYk8fdtFFOZGzt9bKCqZkEFmUhzPl9ecdSJRVV7d7uH9U7LCvvu1JZIguHFuLj9ZWcGKtVX86IbI+ccuq2xgZk6KNdwGWXJCLDfOzePGuXk0tLTz4uZD/HVTDf+zehfdCotmjeHum2aTkjB8VjB0S0x0FFcXjuHP7x7gRHsXiXED/1/YVtNETWMrX70yvKu1wBJJUKSNiGNx4Rj+UnaAby+ecVZ/bKGqs6ubTdWNfGR+/pkPNgGTNiKOpSXjWFoyjtqmNirrjnP+uHSrygqia4ty+OOaSl7b4WFR4cDvSlZv9/b2umx6+I4f8Qnv+6kwsrRkHE2tnUM6P4+bdhxu5kRHlzW0h5Ds5HhnoS1LIsG0oCCDjKQ4ni8/u5UTV1V4KMpNZVRy+M+ybIkkSBYUZDAxKylixpT4Zvy1hnYz3MVER3H1rNGs2naY1o6uM58A1B9vp7SyPiwXseqNJZIgERE+Mj+f9fvr2Xk4PNes8FdaWU9GUhzjMmyiP2OuKczheHsXr+0Y2Fx+r++spVvDezS7P0skQfRP8/KIjRZWrKs688EhrKbxBK9UeDh/XJpVoxgDXDgpk7QRsawcYNX1qgoPWSPjmB0hveoskQRR1sh4PjBzDE+/Wz3gW+BQ09rRxfJHNtDW0cU3F013OxxjQkJsdBQfmDmal7d5zvi/3dWtvLajlkunjoqYpRcskQTZ0pJ86ls6+NuWs2uYCwWqyree2sTmg438aulcm27DGD+Li3JobuvkjZ1H+j2utLKehpYOFkZAby0fSyRBdvGkLPIzElmxNvyqt/73tT08U3aQb3xgGlfOtJX0jPF30aQsUhJizli9tarCQ3SU8P4plkjMOYqKEj5SnM87e46y78hxt8MZsFUVh7n7bxVcNzuHz182ye1wjAk5cTFRfGDWGF7aepi2zr6rt1ZVeCgen05qYuQMGLVE4oKbivOJjgqfRvddnia+/FgZM3NS+NmH51gDuzF9uLYoh6a2Tt7a1Xv1Vk3jCSoONUVMby0fSyQuGJ2SwMJpo3hyQzUdXYNbayLQGls6+MwjG4iPjeL+W4ojYlS+MYFy8eQskhNieH5T722gqyu83YMtkZgh8dEF+RxpbhuyNZ8DobOrmy889i7V9S3c9/F55KYluh2SMSEtLiaKq2aO5qWth3pdkGxVhYe89EQmjxrpQnSBY4nEJZdOHUVOagKPhXCj+09XVvDGziP8aEkh88N8mmtjgmVxYQ7HWjt5a/ep1VutHV28tesIC6eNirjqYdcSiYhEi0ipiPzVeZwhIi+JyE7ne7rfsXeKyC4R2S4iV/uVzxORcmffPRJGv53oKOGm4nxe31lLdX2L2+Gc5qkN1fz2zb3ceuF4lkbYOirGBNL7p2YxMj6GFzad2ntrzd46TnR0RVy1Frh7R/JlYJvf4zuAV1R1CvCK8xgRmQksBWYBi4B7RcRXUX8fsBzvOu5TnP1h4+biPACeCLFG99LKeu78czkXTszku9fNdDscY8JKfEw0V84Yxd+3Hj6lDXR1hYeE2CgunJTpYnSB4UoiEZE84Frgt37FS4CHne2HgRv8yleoapuq7gV2ASUikgOkqOo7qqrAI37nhIW89BFcMiWbJ9ZX0xkije6HGlv57O83MDolnns/dj6x0Vb7aczZWlyUQ+OJDt7efRTwDuZdVeHhoklZEbl+j1vvEv8FfBPwf/ccrao1AM533/1fLuD/kb3aKct1tnuWn0ZElovIehFZX1s7sEnVgmVZST6HjrUOeLK3QGrt6OKzv1/P8bZOfnvLfNKT4twOyZiwdMnUbJLiok8OTtxz5DiVdS0RM9tvT0FPJCJyHeBR1Q0DPaWXMu2n/PRC1ftVtVhVi7OzQ2s06RUzRpM1Mt71RndV5c6ny9lY3cgvP3Ie08bY9CfGnKuE2GiumDGav205REdXN6srvItYRWL7CLhzR3Ix8EER2QesAC4XkT8Ah53qKpzvHuf4asB/Gb484KBTntdLeViJjY7ipuI8Vm/3cPhYq2tx/OaNPfy59ABfu2oqH5g1xrU4jIkUi4tyqG/pYM2eOlZVeJg2Ojliu9AHPZGo6p2qmqeqE/A2oq9S1Y8DzwK3OofdCjzjbD8LLBWReBEpwNuovtap/moSkQuc3lq3+J0TVpbOz6erW/nTenfuSl7d7uGnKyu4tiiHL14+2ZUYjIk0l03LZkRcNI+vr2Lt3rqIWFK3L6HUkvpT4CoR2Qlc5TxGVbcATwBbgReB21XVN5HNbXgb7HcBu4GVwQ56KIzPTOKiSZmsWFdFd3evtXMBs7u2mS8+Vsr0MSn87KbZEde/3Ri3JMRGc/n0UTy38SCd3crl0yKzWgtcTiSq+qqqXudsH1XVK1R1ivO9zu+4u1R1kqpOU9WVfuXrVbXQ2fcFp/dWWFpaMo7q+hO82cccPYHQeKKDzzy8nrjoKO6/ZR4j4mKC9tzGDAeLi3IASEmIYd749DMcHb5C6Y5kWLt61mjSR8SyYl1w1nTv6la+9FgplXXe6U/y0m3JXGOG2sJpoxgRF81l00YRE8Fd6e0jaIiIj4nmQ+fn8cg7+zjS3EbWyPiAPt/dL1bw2o5afnxjESUFNv2JMYGQGBfNnz53IaOSE9wOJaAiN0WGoWUl+XR0KU9tqD7zwYPw59Jq/u/1PXzigvF8dIFNf2JMIM0am0p2cmA/GLrNEkkImTwqmeLx6Ty+ropANfeUVTXwrafKuWBiBt+73qY/McYMniWSELOsZBx7jhxnzd66Mx98ljzHWvns79czKjmeez82z6Y/McYMCXsnCTGLi3JITohhxdqhbXRv7ehi+e830NTayW9uKSbDpj8xxgwRSyQhJjEumhvn5vLC5kM0tLQPyTVVle/8eTNlVQ384uY5zMhJGZLrGmMMWCIJSUvnj6O9s5un3z0wJNd74M29PPVuNV+5cgqLCnOG5JrGGONjiSQEzRybwpy8VFasqxx0o/trO2r58QvbuKZwDF+6fMoQRWiMMe+xRBKilpaMY8fhZt6tbDjna+w9cpwv/vFdpo5O5uc3zSEqyqY/McYMPUskIer6OWMZERd9zo3ux1o7+JeH1xETHcVvbikmKd7GnhpjAsMSSYgaGR/DkvPG8tdNNTS1dpzVuV3dyldWlLH/aAv3fux88jNs+hNjTOBYIglhS+eP40RHF8+Und0yKz/723ZWVXj4/gdnccHEyFsf2hgTWiyRhLDZeanMyEk5q4kcnyk7wP++tpuPLhjHJy4YH8DojDHGyxJJCBMRlpXks/nAMcqrG894/KbqBr755CZKCjL4wfWzghChMcZYIgl5S87LJSE2isfOcFfiaWpl+SMbyBoZz30fO5+4GPvVGmOCI+jvNiKSLyKrRWSbiGwRkS875Rki8pKI7HS+p/udc6eI7BKR7SJytV/5PBEpd/bdIxG4vF9qYiyLi3J4tuwgx9s6ez2mrbOLz/1+A40nOvjNLcVkBngKemOM8efGx9ZO4OuqOgO4ALhdRGYCdwCvqOoU4BXnMc6+pcAsYBFwr4hEO9e6D1iOdx33Kc7+iLOsZBzNbZ08v6nmtH2qynf/vJl3Kxv4z5vnMHOsTX9ijAmuoCcSVa1R1Xed7SZgG5ALLAEedg57GLjB2V4CrFDVNlXdi3d99hIRyQFSVPUdZ4ndR/zOiSjF49OZPGpkr9Vbv3trH3/aUM2XrphycllPY4wJJlcr0kVkAjAXWAOMVtUa8CYbYJRzWC5Q5XdatVOW62z3LI84IsLS+fmUVjaw/VDTyfI3dx7hrhe2cfWs0XzlCpv+xBjjDtcSiYiMBJ4CvqKqx/o7tJcy7ae8t+daLiLrRWR9bW3t2QcbAj50fh5x0VE85ox033fkOLf/8V0mZ4/kFzefZ9OfGGNc40oiEZFYvEnkUVV92ik+7FRX4Xz3OOXVQL7f6XnAQac8r5fy06jq/aparKrF2dnZQ/dCgigjKY6rC8fw9LvVHGlu4zOPrEcEm/7EGOM6N3ptCfAAsE1Vf+G361ngVmf7VuAZv/KlIhIvIgV4G9XXOtVfTSJygXPNW/zOiUjL5udzrLWTJb9+iz1HjnPvx85nXKZNf2KMcZcbH2UvBj4BlItImVP2beCnwBMi8mmgErgJQFW3iMgTwFa8Pb5uV9Uu57zbgIeARGCl8xWxLpiYyfjMEew/2sIPl8zioklZbodkjDHIYNe7CDfFxcW6fv16t8M4Z2/vOsKOw03cetEEInDYjDEmRInIBlUt7m2fVa6HmYsmZ3HRZLsTMcaEDptHwxhjzKBYIjHGGDMolkiMMcYMiiUSY4wxg2KJxBhjzKBYIjHGGDMolkiMMcYMiiUSY4wxgzLsRraLSC2w/xxPzwKODGE44c5+Hqeyn8d77Gdxqkj4eYxX1V5nvR12iWQwRGR9X1MEDEf28ziV/TzeYz+LU0X6z8OqtowxxgyKJRJjjDGDYonk7NzvdgAhxn4ep7Kfx3vsZ3GqiP55WBuJMcaYQbE7EmOMMYNiicQYY8ygWCIZIBFZJCLbRWSXiNzhdjxuEZF8EVktIttEZIuIfNntmEKBiESLSKmI/NXtWNwmImki8qSIVDh/Jxe6HZNbROSrzv/JZhF5TEQS3I4pECyRDICIRAP/A1wDzASWichMd6NyTSfwdVWdAVwA3D6Mfxb+vgxsczuIEPEr4EVVnQ7MYZj+XEQkF/gSUKyqhUA0sNTdqALDEsnAlAC7VHWPqrYDK4AlLsfkClWtUdV3ne0mvG8Sue5G5S4RyQOuBX7rdixuE5EU4BLgAQBVbVfVBleDclcMkCgiMcAI4KDL8QSEJZKByQWq/B5XM8zfPAFEZAIwF1jjcihu+y/gm0C3y3GEgolALfA7p6rvtyKS5HZQblDVA8DPgUqgBmhU1b+7G1VgWCIZGOmlbFj3mxaRkcBTwFdU9Zjb8bhFRK4DPKq6we1YQkQMcD5wn6rOBY4Dw7JNUUTS8dZcFABjgSQR+bi7UQWGJZKBqQby/R7nEaG3qAMhIrF4k8ijqvq02/G47GLggyKyD2+V5+Ui8gd3Q3JVNVCtqr671CfxJpbh6Epgr6rWqmoH8DRwkcsxBYQlkoFZB0wRkQIRicPbYPasyzG5QkQEb/33NlX9hdvxuE1V71TVPFWdgPfvYpWqRuSnzoFQ1UNAlYhMc4quALa6GJKbKoELRGSE839zBRHa8SDG7QDCgap2isgXgL/h7XnxoKpucTkst1wMfAIoF5Eyp+zbqvqCeyGZEPNF4FHnQ9ce4FMux+MKVV0jIk8C7+Lt7VhKhE6VYlOkGGOMGRSr2jLGGDMolkiMMcYMiiUSY4wxg2KJxBhjzKBYIjHGGDMolkiMCRARaT7L4y+z2YNNOLJEYowxZlAskRgTYM6dxqt+a3Q86ox09q1zUyEibwIf8jsnSUQeFJF1zuSHS5zye0Tke8721SLyuojY/7FxlY1sNyY45gKz8M7R9hZwsYisB34DXA7sAh73O/47eKdb+WcRSQPWisjLeCdAXCcibwD3AItV1WYdNq6yTzLGBMdaVa123vTLgAnAdLyT+u1U7xQT/pM9fgC4w5mG5lUgARinqi3AZ4CXgF+r6u6gvQJj+mB3JMYER5vfdhfv/e/1NUeRAP+kqtt72VcEHMU7NbkxrrM7EmPcUwEUiMgk5/Eyv31/A77o15Yy1/k+Hvg63qqya0RkQRDjNaZXlkiMcYmqtgLLgeedxvb9frt/BMQCm0RkM/Ajvyn8v6GqB4FPA78VkYQgh27MKWz2X2OMMYNidyTGGGMGxRKJMcaYQbFEYowxZlAskRhjjBkUSyTGGGMGxRKJMcaYQbFEYowxZlD+P2Kgf8yKy77iAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "column_data = baseraw['Cost']\n",
    "first_10_values = column_data.head(10)\n",
    "\n",
    "plt.plot(first_10_values)\n",
    "\n",
    "plt.xlabel('Index')\n",
    "plt.ylabel('Value')\n",
    "plt.title('Graph of First 10 Values')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a2fa843b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     Keyword   Clicks     Cost  CPC    Users  Sessions  \\\n",
      "0                    hoodies  10184.0   8404.0  1.0   4502.0    4740.0   \n",
      "1   Google Merchandise Store   9330.0   1660.0  0.0  10301.0   20318.0   \n",
      "2                      hoody   6754.0   4920.0  1.0   2674.0    2823.0   \n",
      "3        youtube merchandise   6279.0  17233.0  3.0   2958.0    3566.0   \n",
      "4  YouTube Merchandise Store   4711.0   6225.0  1.0   3271.0    3908.0   \n",
      "\n",
      "  Bounce Rate Pages / Session Ecommerce Conversion Rate  Transactions  \\\n",
      "0         87%            1,48                        0%           7.0   \n",
      "1         26%            7,47                        5%        1072.0   \n",
      "2         88%            1,45                        0%           2.0   \n",
      "3         51%            3,49                        1%          24.0   \n",
      "4         46%            3,88                        1%          44.0   \n",
      "\n",
      "    Revenue   ROAS  \n",
      "0     884.0   -89%  \n",
      "1  133488.0  7943%  \n",
      "2     109.0   -98%  \n",
      "3    1287.0   -93%  \n",
      "4    2705.0   -57%  \n",
      "(1595, 12)\n",
      "              Clicks          Cost         CPC         Users      Sessions  \\\n",
      "count     860.000000    859.000000  859.000000    859.000000    859.000000   \n",
      "mean      285.746512    299.527357    1.937136    108.805588    139.481956   \n",
      "std      3731.935975   1287.251085    1.340861    651.929963    961.152879   \n",
      "min         0.000000      0.000000    0.000000      0.000000      0.000000   \n",
      "25%         3.000000      5.000000    1.000000      2.000000      2.000000   \n",
      "50%        13.500000     21.000000    2.000000      6.000000      6.000000   \n",
      "75%        58.250000     97.500000    2.000000     35.000000     36.500000   \n",
      "max    107632.000000  17233.000000   12.000000  13156.000000  20318.000000   \n",
      "\n",
      "       Transactions        Revenue  \n",
      "count    859.000000     859.000000  \n",
      "mean       2.916182     319.912689  \n",
      "std       39.113873    4796.126793  \n",
      "min        0.000000       0.000000  \n",
      "25%        0.000000       0.000000  \n",
      "50%        0.000000       0.000000  \n",
      "75%        0.000000       0.000000  \n",
      "max     1072.000000  133488.000000  \n",
      "Keyword                       object\n",
      "Clicks                       float64\n",
      "Cost                         float64\n",
      "CPC                          float64\n",
      "Users                        float64\n",
      "Sessions                     float64\n",
      "Bounce Rate                   object\n",
      "Pages / Session               object\n",
      "Ecommerce Conversion Rate     object\n",
      "Transactions                 float64\n",
      "Revenue                      float64\n",
      "ROAS                          object\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(baseraw.head())\n",
    "\n",
    "print(baseraw.shape)\n",
    "\n",
    "print(baseraw.describe())\n",
    "\n",
    "print(baseraw.dtypes)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee4b1d84",
   "metadata": {},
   "source": [
    "### Base Raw - Matriz de Correlação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "9541e0be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Keyword                      736\n",
      "Clicks                       735\n",
      "Cost                         736\n",
      "CPC                          736\n",
      "Users                        736\n",
      "Sessions                     736\n",
      "Bounce Rate                  736\n",
      "Pages / Session              736\n",
      "Ecommerce Conversion Rate    736\n",
      "Transactions                 736\n",
      "Revenue                      736\n",
      "ROAS                         736\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Correlation Matrix - Base Raw')"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "baseraw = pd.read_csv('advertising-adwords-keywords-raw.csv', sep =';')\n",
    "print(baseraw.isnull().sum())\n",
    "\n",
    "baseraw = baseraw.dropna()  \n",
    "\n",
    "plt.hist(baseraw['Cost'])\n",
    "plt.xlabel('Variable')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram')\n",
    "\n",
    "plt.scatter(baseraw['Cost'], baseraw['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Scatter Plot')\n",
    "\n",
    "sns.boxplot(x=baseraw['Cost'], y=baseraw['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Box Plot')\n",
    "\n",
    "correlation_matrix = baseraw.corr()\n",
    "sns.heatmap(correlation_matrix, annot=True)\n",
    "plt.title('Correlation Matrix - Base Raw')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0bcc5594",
   "metadata": {},
   "source": [
    "### Base cooked"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c18142f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>search</th>\n",
       "      <th>Clicks</th>\n",
       "      <th>Cost</th>\n",
       "      <th>CPC</th>\n",
       "      <th>Users</th>\n",
       "      <th>Sessions</th>\n",
       "      <th>Bounce Rate</th>\n",
       "      <th>Pages / Session</th>\n",
       "      <th>Ecommerce Conversion Rate</th>\n",
       "      <th>Transactions</th>\n",
       "      <th>Revenue</th>\n",
       "      <th>ROAS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1 4 zip sweatshirt</td>\n",
       "      <td>1</td>\n",
       "      <td>1,00</td>\n",
       "      <td>1,23</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0,00</td>\n",
       "      <td>-100%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>100 cotton long sleeve shirts</td>\n",
       "      <td>1</td>\n",
       "      <td>1,00</td>\n",
       "      <td>1,14</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0,00</td>\n",
       "      <td>-100%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>100 cotton mens shirts</td>\n",
       "      <td>2</td>\n",
       "      <td>2,00</td>\n",
       "      <td>0,91</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0,00</td>\n",
       "      <td>-100%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>100 percent cotton t shirts</td>\n",
       "      <td>3</td>\n",
       "      <td>4,00</td>\n",
       "      <td>1,28</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0,00</td>\n",
       "      <td>-100%</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>20 oz stainless steel tumblers</td>\n",
       "      <td>1</td>\n",
       "      <td>3,00</td>\n",
       "      <td>3,42</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0,00</td>\n",
       "      <td>-100%</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           search  Clicks  Cost   CPC  Users   Sessions  \\\n",
       "0              1 4 zip sweatshirt       1  1,00  1,23      0          0   \n",
       "1   100 cotton long sleeve shirts       1  1,00  1,14      1          1   \n",
       "2          100 cotton mens shirts       2  2,00  0,91      1          1   \n",
       "3     100 percent cotton t shirts       3  4,00  1,28      3          3   \n",
       "4  20 oz stainless steel tumblers       1  3,00  3,42      0          0   \n",
       "\n",
       "   Bounce Rate Pages / Session Ecommerce Conversion Rate   Transactions  \\\n",
       "0            0               0                         0              0   \n",
       "1            1               1                         0              0   \n",
       "2            1               1                         0              0   \n",
       "3            1               1                         0              0   \n",
       "4            0               0                         0              0   \n",
       "\n",
       "   Revenue   ROAS  \n",
       "0     0,00  -100%  \n",
       "1     0,00  -100%  \n",
       "2     0,00  -100%  \n",
       "3     0,00  -100%  \n",
       "4     0,00  -100%  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "basecooked = pd.read_csv('advertising-adwords-keywords-cooked.csv', sep =';')\n",
    "basecooked.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9d699089",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Clicks</th>\n",
       "      <th>Users</th>\n",
       "      <th>Sessions</th>\n",
       "      <th>Transactions</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "      <td>768.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>179.830729</td>\n",
       "      <td>110.855469</td>\n",
       "      <td>128.386719</td>\n",
       "      <td>27.401042</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>906.837009</td>\n",
       "      <td>665.339110</td>\n",
       "      <td>735.715687</td>\n",
       "      <td>498.915283</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2.750000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>13.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>53.000000</td>\n",
       "      <td>34.250000</td>\n",
       "      <td>36.250000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>13976.000000</td>\n",
       "      <td>12520.000000</td>\n",
       "      <td>12641.000000</td>\n",
       "      <td>10184.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Clicks         Users      Sessions   Transactions\n",
       "count    768.000000    768.000000    768.000000     768.000000\n",
       "mean     179.830729    110.855469    128.386719      27.401042\n",
       "std      906.837009    665.339110    735.715687     498.915283\n",
       "min        1.000000      0.000000      0.000000       0.000000\n",
       "25%        2.750000      2.000000      2.000000       0.000000\n",
       "50%       13.000000      6.000000      6.000000       0.000000\n",
       "75%       53.000000     34.250000     36.250000       0.000000\n",
       "max    13976.000000  12520.000000  12641.000000   10184.000000"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "basecooked.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "d3850e4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "count       46.000000\n",
      "mean      3532.913043\n",
      "std       5668.779472\n",
      "min          3.000000\n",
      "25%        340.500000\n",
      "50%        995.500000\n",
      "75%       4373.500000\n",
      "max      28794.000000\n",
      "Name: Cost, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "column_stats = basecooked['Cost'].describe()\n",
    "print(column_stats)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "14b221e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "column_stats = basecooked['Cost'].describe()\n",
    "\n",
    "index_str = column_stats.index.astype(str)\n",
    "values_str = column_stats.values.astype(str)\n",
    "\n",
    "plt.bar(index_str, values_str)\n",
    "\n",
    "plt.xlabel('Statistic')\n",
    "plt.ylabel('Value')\n",
    "plt.title('Summary Statistics')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "50b5c1f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "column_data = basecooked['Cost'].astype(str)\n",
    "\n",
    "plt.hist(column_data)\n",
    "\n",
    "plt.xlabel('Values')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "db3ee2f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "column_data = basecooked['Cost']\n",
    "first_10_values = column_data.head(10)\n",
    "\n",
    "plt.plot(first_10_values)\n",
    "\n",
    "plt.xlabel('Index')\n",
    "plt.ylabel('Value')\n",
    "plt.title('Graph of First 10 Values')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "452f5b48",
   "metadata": {},
   "source": [
    "### Base Cooked - Matriz de Correlação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "730a50f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 search  Clicks  Cost  CPC  Users  Sessions Bounce Rate  \\\n",
      "0   all youtubers merch      82    83    1     69        80        0,51   \n",
      "1       Android Apparel      89   224    4     62        74        0,95   \n",
      "2  Android Collectibles      72   148    4     61        68        1,27   \n",
      "3        Android Figure     210   354    3    127       167        0,96   \n",
      "4   Android Merchandise     326   441    3    211       374        0,67   \n",
      "\n",
      "   Pages / Session  Conversion Rate  Transactions  Revenue   ROAS  \n",
      "0                4                0             2       23  -0,73  \n",
      "1                9                0             1       16  -0,93  \n",
      "2                7                0             1      155   0,05  \n",
      "3               12                0             5      527   0,49  \n",
      "4               11                0             6      210  -0,52  \n",
      "(46, 12)\n",
      "             Clicks          Cost           CPC         Users      Sessions  \\\n",
      "count     46.000000     46.000000     46.000000     46.000000     46.000000   \n",
      "mean    1866.478261   3532.913043    433.108696   1260.347826   1519.565217   \n",
      "std     3053.672490   5668.779472   2012.433190   2412.056064   2606.156503   \n",
      "min        3.000000      3.000000      1.000000      2.000000      2.000000   \n",
      "25%      143.250000    340.500000      3.000000     74.750000    102.500000   \n",
      "50%      368.500000    995.500000      4.000000    260.000000    370.500000   \n",
      "75%     2419.000000   4373.500000      6.000000   1647.500000   1797.750000   \n",
      "max    13976.000000  28794.000000  10186.000000  12520.000000  12641.000000   \n",
      "\n",
      "       Pages / Session  Conversion Rate  Transactions       Revenue  \n",
      "count        46.000000        46.000000     46.000000     46.000000  \n",
      "mean        436.282609       429.130435    457.478261   3211.217391  \n",
      "std        2012.249903      2012.968517   2010.353089   7598.650997  \n",
      "min           2.000000         0.000000      1.000000      2.000000  \n",
      "25%           4.250000         0.000000      1.250000     79.500000  \n",
      "50%           7.000000         0.000000      5.000000    227.500000  \n",
      "75%          12.000000         0.000000     26.250000   1548.750000  \n",
      "max       10185.000000     10184.000000  10184.000000  38219.000000  \n",
      "search             object\n",
      "Clicks              int64\n",
      "Cost                int64\n",
      "CPC                 int64\n",
      "Users               int64\n",
      "Sessions            int64\n",
      "Bounce Rate        object\n",
      "Pages / Session     int64\n",
      "Conversion Rate     int64\n",
      "Transactions        int64\n",
      "Revenue             int64\n",
      "ROAS               object\n",
      "dtype: object\n",
      "search             0\n",
      "Clicks             0\n",
      "Cost               0\n",
      "CPC                0\n",
      "Users              0\n",
      "Sessions           0\n",
      "Bounce Rate        0\n",
      "Pages / Session    0\n",
      "Conversion Rate    0\n",
      "Transactions       0\n",
      "Revenue            0\n",
      "ROAS               0\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Correlation Matrix - Base Cooked')"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "basecooked = pd.read_csv('advertising-adwords-keywords-cooked.csv', sep =';')\n",
    "\n",
    "print(basecooked.head())\n",
    "\n",
    "print(basecooked.shape)\n",
    "\n",
    "print(basecooked.describe())\n",
    "\n",
    "print(basecooked.dtypes)\n",
    "\n",
    "print(basecooked.isnull().sum())\n",
    "\n",
    "basecooked = basecooked.dropna()  \n",
    "\n",
    "plt.hist(basecooked['Cost'])\n",
    "plt.xlabel('Variable')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram')\n",
    "\n",
    "plt.scatter(basecooked['Cost'], basecooked['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Scatter Plot')\n",
    "\n",
    "sns.boxplot(x=basecooked['Cost'], y=basecooked['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Box Plot')\n",
    "\n",
    "correlation_matrix = basecooked.corr()\n",
    "sns.heatmap(correlation_matrix, annot=True)\n",
    "plt.title('Correlation Matrix - Base Cooked')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c3ead79",
   "metadata": {},
   "source": [
    "### ROAS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "d0c9ad07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            search-neg  Cost  Revenue\n",
      "0  all youtubers merch    83       23\n",
      "1      Android Apparel   224       16\n",
      "2       Android Figure   107       16\n",
      "3  Android Merchandise   441      210\n",
      "4     coffee drinkware  2445       75\n",
      "(34, 3)\n",
      "               Cost      Revenue\n",
      "count     34.000000    34.000000\n",
      "mean    3898.235294   811.705882\n",
      "std     6130.003411  1845.770424\n",
      "min       83.000000    12.000000\n",
      "25%      475.750000    27.500000\n",
      "50%      995.500000   147.500000\n",
      "75%     4911.750000   374.000000\n",
      "max    28794.000000  9744.000000\n",
      "search-neg    object\n",
      "Cost           int64\n",
      "Revenue        int64\n",
      "dtype: object\n",
      "search-neg    0\n",
      "Cost          0\n",
      "Revenue       0\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Correlation Matrix - ROAS Negativo')"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "baseneg = pd.read_csv('roasneg.csv', sep =';')\n",
    "\n",
    "print(baseneg.head())\n",
    "\n",
    "print(baseneg.shape)\n",
    "\n",
    "print(baseneg.describe())\n",
    "\n",
    "print(baseneg.dtypes)\n",
    "\n",
    "print(baseneg.isnull().sum())\n",
    "\n",
    "basepos = basepos.dropna()  \n",
    "\n",
    "plt.hist(baseneg['Cost'])\n",
    "plt.xlabel('Variable')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram')\n",
    "\n",
    "plt.scatter(baseneg['Cost'], baseneg['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Scatter Plot')\n",
    "\n",
    "sns.boxplot(x=baseneg['Cost'], y=baseneg['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Box Plot')\n",
    "\n",
    "correlation_matrix = baseneg.corr()\n",
    "sns.heatmap(correlation_matrix, annot=True)\n",
    "plt.title('Correlation Matrix - ROAS Negativo')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "e8acd379",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   search-pos  Cost  Revenue\n",
      "0        Android Collectibles   127      155\n",
      "1              Android Figure   247      511\n",
      "2              Google Apparel  6834    31474\n",
      "3      Google Branded Apparel   368     1384\n",
      "4  Google Branded Merchandise   344     1847\n",
      "(13, 3)\n",
      "              Cost        Revenue\n",
      "count    13.000000      13.000000\n",
      "mean   1547.538462   18057.692308\n",
      "std    2007.988488   37524.819441\n",
      "min      14.000000     140.000000\n",
      "25%     127.000000     511.000000\n",
      "50%     368.000000    1847.000000\n",
      "75%    2638.000000   11333.000000\n",
      "max    6834.000000  135917.000000\n",
      "search-pos    object\n",
      "Cost           int64\n",
      "Revenue        int64\n",
      "dtype: object\n",
      "search-pos    0\n",
      "Cost          0\n",
      "Revenue       0\n",
      "dtype: int64\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Correlation Matrix - ROAS Positivo')"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "baseposi = pd.read_csv('roasposi.csv', sep =';')\n",
    "\n",
    "print(baseposi.head())\n",
    "\n",
    "print(baseposi.shape)\n",
    "\n",
    "print(baseposi.describe())\n",
    "\n",
    "print(baseposi.dtypes)\n",
    "\n",
    "print(baseposi.isnull().sum())\n",
    "\n",
    "basepos = baseposi.dropna()  \n",
    "\n",
    "plt.hist(baseposi['Cost'])\n",
    "plt.xlabel('Variable')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram')\n",
    "\n",
    "plt.scatter(baseposi['Cost'], baseposi['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Scatter Plot')\n",
    "\n",
    "sns.boxplot(x=baseposi['Cost'], y=baseposi['Revenue'])\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('Box Plot')\n",
    "\n",
    "correlation_matrix = baseposi.corr()\n",
    "sns.heatmap(correlation_matrix, annot=True)\n",
    "plt.title('Correlation Matrix - ROAS Positivo')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "01d7c2f4",
   "metadata": {},
   "source": [
    "## Regressão Linear do ROAS Positivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "971e429e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Squared Error: 4157900642.4601736\n",
      "R^2 Score: -0.3491329612333476\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.model_selection import train_test_split\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "basepos = pd.read_csv('roasposi.csv', sep =';')\n",
    "\n",
    "X = basepos[['Cost']]  # Independent variable(s)\n",
    "y = basepos['Revenue']  # Dependent variable\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "\n",
    "model = LinearRegression()\n",
    "model.fit(X_train, y_train)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "r2 = r2_score(y_test, y_pred)\n",
    "print('Mean Squared Error:', mse)\n",
    "print('R^2 Score:', r2)\n",
    "\n",
    "plt.scatter(X_test, y_test, color='black')\n",
    "plt.plot(X_test, y_pred, color='blue', linewidth=3)\n",
    "plt.xlabel('Cost Positivo')\n",
    "plt.ylabel('Revenue Positivo')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "935c1a3b",
   "metadata": {},
   "source": [
    "### Regresão Linear do ROAS Negativo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e1656603",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Squared Error: 960382.7413934662\n",
      "R^2 Score: -89.38903420332025\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.model_selection import train_test_split\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "baseneg = pd.read_csv('roasneg.csv', sep =';')\n",
    "\n",
    "X = baseneg[['Cost']]  # Independent variable(s)\n",
    "y = baseneg['Revenue']  # Dependent variable\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "\n",
    "model = LinearRegression()\n",
    "model.fit(X_train, y_train)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "r2 = r2_score(y_test, y_pred)\n",
    "print('Mean Squared Error:', mse)\n",
    "print('R^2 Score:', r2)\n",
    "\n",
    "plt.scatter(X_test, y_test, color='black')\n",
    "plt.plot(X_test, y_pred, color='blue', linewidth=3)\n",
    "plt.xlabel('Cost Negativo')\n",
    "plt.ylabel('Revenue Negativo')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "825a8cc5",
   "metadata": {},
   "source": [
    "## K-means Geral"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "45e7905b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.cluster import KMeans\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load data from a CSV file\n",
    "data1 = pd.read_csv('advertising-adwords-keywords-cooked.csv', sep=';')\n",
    "\n",
    "# Extract features\n",
    "X = data1[['Clicks','Cost', 'Revenue', 'CPC', 'Users', 'Conversion Rate', 'Transactions']].values  # Replace feature1, feature2 with your feature column names\n",
    "\n",
    "# Perform k-means clustering\n",
    "k = 5  # Number of clusters\n",
    "kmeans = KMeans(n_clusters=k, random_state=60)\n",
    "kmeans.fit(X)\n",
    "\n",
    "# Get cluster labels and centroids\n",
    "labels = kmeans.labels_\n",
    "centroids = kmeans.cluster_centers_\n",
    "\n",
    "# Visualize the clusters\n",
    "plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')\n",
    "plt.scatter(centroids[:, 0], centroids[:, 3], marker='x', color='red')\n",
    "plt.xlabel('Cost')\n",
    "plt.ylabel('Revenue')\n",
    "plt.title('K-means Clustering Cooked')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95370e2d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da66e06f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "822f5bf4",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b6c095c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ffb3b1e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
