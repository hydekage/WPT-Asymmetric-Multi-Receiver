import sympy as sp

def named_expression(symbol, expr):

    class NamedExpression(type(expr)):

        def __new__(cls, sym, ex):
            # NB: we don't call the base class' __new__()!
            self = object.__new__(cls)
            if isinstance(sym, sp.Symbol):
                self._symbol = sym
            else:
                self._symbol = sp.Symbol(sym)
            self._expr = ex
            return self

        def __getattribute__(self, name):
            if name in ['_symbol', '_expr', 'as_symbol', 'as_eq']:
                return super().__getattribute__(name)
            return self._expr.__getattribute__(name)

        def as_symbol(self):
            return self._symbol

        def as_eq(self):
            return sp.Eq(self._symbol, self._expr)

    return NamedExpression(symbol, expr)