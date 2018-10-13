{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2018\n",
      "n=2018\n",
      "F(n)はn番目のフィボナッチ数\n",
      "F(n)=39496686472772163397874981928532586937785000709985018165227544505583956123892491583992043369010510473852474871823919949628656144692626488180105707977212947225784927555125847822065435826037363716924714565553298478909956798245598759168652339244838488670328632476925440191393691741920312935346241800034867950746972804090992175422630866247531341721589487617557085576900215798341862472548933587106152708259589526498478046850306\n"
     ]
    }
   ],
   "source": [
    "def fib(n):\n",
    "    a, b = 0, 1\n",
    "    for i in range(n):\n",
    "        a, b = b, a + b\n",
    "    return b\n",
    "\n",
    "#print([fib(i) for i in range(num)])  #n =整数\n",
    "num=int(input())\n",
    "print(\"n=\" + str(num))\n",
    "print(\"F(n)はn番目のフィボナッチ数\")\n",
    "print(\"F(n)=\" +str(fib(num)))"
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
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
