{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from statsmodels.stats.weightstats import _tconfint_generic as t_stat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    #1.Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks),
    "zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]",
    "ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]."
    #Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy,
    #Полученные значения должны быть равны.
    #Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков",
    #а затем с использованием функций из библиотек numpy и pandas.
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])",
    "ks = np.array( [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "M_X = zp.mean()\n",
    "M_Y = ks.mean()\n",
    "M_XY = (zp * ks).mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9157.839999999997"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cov_ks = M_XY - M_X * M_Y\n",
    "cov_ks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 3494.64, 9157.84],\n",
       "       [ 9157.84, 30468.89]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.cov(zp, ks, ddof=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9157.84"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cov_ks2 = ((zp - zp.mean()) * (ks - ks.mean())).mean()\n",
    "cov_ks2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "std_X = zp.std()\n",
    "std_Y = ks.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8874900920739158"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_ks = cov_ks / (std_X * std_Y)\n",
    "corr_ks"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.        , 0.88749009],\n",
       "       [0.88749009, 1.        ]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.corrcoef(zp, ks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    #2. Измерены значения IQ выборки студентов, 
    #обучающихся в местных технических вузах:",
    #131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
    #Известно, что в генеральной совокупности IQ распределен нормально.
    #Найдите доверительный интервал для математического ожидания с надежностью 0.95."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = np.array([131.0, 125.0, 115.0, 122.0, 131.0, 115.0, 107.0, 99.0, 125.0, 111.0])\n",
    "mean_X = X.mean()\n",
    "std_X = X.std(ddof=1)\n",
    "mean_std_X = std_X / (np.sqrt(len(X)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(110.55608365158724, 125.64391634841274)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t_stat(mean_X, mean_std_X,len(X) - 1, 0.05, 'two-sided')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    #3.Известно, что рост футболистов в сборной распределен нормально,
    #с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,",
    #среднее выборочное составляет 174.2. Найдите доверительный интервал для математического,
    #ожидания с надежностью 0.95."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "mean_X = 174.2\n",
    "std_X = np.sqrt(25)\n",
    "mean_std_X = std_X / np.sqrt(27)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(172.2220658754539, 176.17793412454608)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t_stat(mean_X, mean_std_X,27 - 1, 0.05, 'two-sided')"
    ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
}
