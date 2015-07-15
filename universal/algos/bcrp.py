# -*- coding: utf-8 -*-
from universal.algo import Algo
from universal.algos import CRP
import universal.tools as tools
import numpy as np


class BCRP(CRP):
    """ Best Constant Rebalanced Portfolio = Constant Rebalanced Portfolio constructed
    with hindsight. It is often used as benchmark.

    Reference:
        T. Cover. Universal Portfolios, 1991.
        http://www-isl.stanford.edu/~cover/papers/paper93.pdf
    """

    def __init__(self, **kwargs):
        self.opt_weights_kwargs = kwargs

    def weights(self, X):
        """ Find weights which maximize return on X in hindsight! """
        # update frequency
        self.opt_weights_kwargs['freq'] = tools.freq(X.index)

        self.b = tools.opt_weights(X, **self.opt_weights_kwargs)

        return super(BCRP, self).weights(X)


if __name__ == '__main__':
    tools.quickrun(BCRP())

