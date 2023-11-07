# fourFn.py
#
# Demonstration of the pyparsing module, implementing a simple 4-function expression parser,
# with support for scientific notation, and symbols for e and pi.
# Extended to add exponentiation and simple built-in functions.
# Extended test cases, simplified pushFirst method.
# Removed unnecessary expr.suppress() call (thanks Nathaniel Peterson!), and added Group
# Changed fnumber to use a Regex, which is now the preferred method
# Reformatted to latest pypyparsing features, support multiple and variable args to functions
#
# Copyright 2003-2019 by Paul McGuire
#
#%%
from pyparsing import (
    Literal,
    Word,
    Group,
    Forward,
    alphas,
    alphanums,
    Regex,
    ParseException,
    CaselessKeyword,
    Suppress,
    delimitedList,
)
import math
import operator
from typing import Any
import numpy as np

# map operator symbols to corresponding arithmetic operations
epsilon = 1e-12
opn = {
    "**": operator.pow,
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}

# NumPy ufuncs with one argument
fn = {key: val for (key, val) in np.__dict__.items() 
      if isinstance(val, np.ufunc) 
      if "e->e" in val.types}
    
    
    
class MathParser:
    def __init__(self):
        self.exprStack = []
        self.bnf = None
        self.init_BNF()

    def push_first(self, toks):
        self.exprStack.append(toks[0])


    def push_unary_minus(self, toks):
        for t in toks:
            if t == "-":
                self.exprStack.append("unary -")
            else:
                break
            

    def init_BNF(self):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        if self.bnf is None:
            # use CaselessKeyword for e and pi, to avoid accidentally matching
            # functions that start with 'e' or 'pi' (such as 'exp'); Keyword
            # and CaselessKeyword only match whole words
            e = CaselessKeyword("E")
            pi = CaselessKeyword("PI")
            # fnumber = Combine(Word("+-"+nums, nums) +
            #                    Optional("." + Optional(Word(nums))) +
            #                    Optional(e + Word("+-"+nums, nums)))
            # or use provided pyparsing_common.number, but convert back to str:
            # fnumber = ppc.number().addParseAction(lambda t: str(t[0]))
            fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
            ident = Word(alphas, alphanums + "_$")

            plus, minus, mult, div = map(Literal, "+-*/")
            lpar, rpar = map(Suppress, "()")
            addop = plus | minus
            multop = mult | div
            expop = Literal("^") | Literal("**")

            expr = Forward()
            expr_list = delimitedList(Group(expr))
            # add parse action that replaces the function identifier with a (name, number of args) tuple
            def insert_fn_argcount_tuple(t):
                fn = t.pop(0)
                num_args = len(t[0])
                t.insert(0, (fn, num_args))

            fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(
                insert_fn_argcount_tuple
            )
            atom = (
                addop[...]
                + (
                    (fn_call | pi | e | fnumber | ident).setParseAction(self.push_first)
                    | Group(lpar + expr + rpar)
                )
            ).setParseAction(self.push_unary_minus)

            # by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left
            # exponents, instead of left-to-right that is, 2^3^2 = 2^(3^2), not (2^3)^2.
            factor = Forward()
            factor <<= atom + (expop + factor).setParseAction(self.push_first)[...]
            term = factor + (multop + factor).setParseAction(self.push_first)[...]
            expr <<= term + (addop + term).setParseAction(self.push_first)[...]
            self.bnf = expr

    def init_BNF_(self):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        if self.bnf is None:
            # use CaselessKeyword for e and pi, to avoid accidentally matching
            # functions that start with 'e' or 'pi' (such as 'exp'); Keyword
            # and CaselessKeyword only match whole words
            e = CaselessKeyword("E")
            pi = CaselessKeyword("PI")
            # fnumber = Combine(Word("+-"+nums, nums) +
            #                    Optional("." + Optional(Word(nums))) +
            #                    Optional(e + Word("+-"+nums, nums)))
            # or use provided pyparsing_common.number, but convert back to str:
            # fnumber = ppc.number().addParseAction(lambda t: str(t[0]))
            fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
            ident = Word(alphas, alphanums + "_$")

            plus, minus, mult, div = map(Literal, "+-*/")
            lpar, rpar = map(Suppress, "()")
            addop = plus | minus
            multop = mult | div
            expop = Literal("^") | Literal("**")

            expr = Forward()
            expr_list = delimitedList(Group(expr))
            # add parse action that replaces the function identifier with a (name, number of args) tuple
            def insert_fn_argcount_tuple(t):
                fn = t.pop(0)
                num_args = len(t[0])
                t.insert(0, (fn, num_args))

            fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(
                insert_fn_argcount_tuple
            )
            
            atom_inner = (fn_call | pi | e | fnumber | ident)
            atom_inner.setParseAction(self.push_first)
            
            atom = (
                addop[...]
                + (
                    atom_inner
                    | Group(lpar + expr + rpar)
                )
            )

            # by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left
            # exponents, instead of left-to-right that is, 2^3^2 = 2^(3^2), not (2^3)^2.
            factor = Forward()
            expop_factor = expop + factor
            factor <<= atom + expop_factor[...]
            multop_factor = multop + factor
            term = factor + multop_factor[...]
            addop_term = addop + term
            expr <<= term + addop_term[...]

            atom.setParseAction(self.push_unary_minus)
            expop_factor.setParseAction(self.push_first)
            multop_factor.setParseAction(self.push_first)
            addop_term.setParseAction(self.push_first)
            self.bnf = expr




    def evaluate_stack(self, s, var_dict: dict[str, Any]| None = None):
        if var_dict is None:
            var_dict = dict()
        op, num_args = s.pop(), 0
        if isinstance(op, tuple):
            op, num_args = op
        if op == "unary -":
            return -self.evaluate_stack(s, var_dict)
        if op in opn:
            # note: operands are pushed onto the stack in reverse order
            op2 = self.evaluate_stack(s, var_dict)
            op1 = self.evaluate_stack(s, var_dict)
            return opn[op](op1, op2)
        elif op.lower() == "pi":
            return math.pi  # 3.1415926535
        elif op.lower() == "e":
            return math.e  # 2.718281828
        elif op in fn:
            # note: args are pushed onto the stack in reverse order
            args = reversed([self.evaluate_stack(s, var_dict) for _ in range(num_args)])
            return fn[op](*args)
        elif op.isidentifier():
            try:
                return var_dict[op]
            except KeyError:
                raise KeyError(f"unknown variable {op}")
        elif op[0].isalpha():
            raise Exception("invalid identifier '%s'" % op)
        else:
            # try to evaluate as int first, then as float if int fails
            try:
                return int(op)
            except ValueError:
                return float(op)
    def evaluate_expression(self, s: str, var_dict:dict[str, Any]| None = None):
        self.exprStack[:] = []
        self.results = self.bnf.parseString(s, parseAll=True)
        val = self.evaluate_stack(self.exprStack[:], var_dict)
        return val
    
    
parser=MathParser()
#%%

if __name__ == "__main__":
    import numpy as np
    p = MathParser()
    x = np.linspace(-1,1,10)
    print(p.evaluate_expression("sin(x_1222see)", dict(x_1222see=x)))


    def test(s, expected):
        try:
            val = p.evaluate_expression(s)
        except ParseException as pe:
            print(s, "failed parse:", str(pe))
        except Exception as e:
            print(s, "failed eval:", str(e), p.exprStack)
        else:
            if val == expected:
                print(s, "=", val, p.results, "=>", p.exprStack)
            else:
                1/0
                print(s + "!!!", val, "!=", expected, p.results, "=>", p.exprStack)

    test("9", 9)
    test("-9", -9)
    test("--9", 9)
    test("-E", -math.e)
    test("9 + 3 + 6", 9 + 3 + 6)
    test("9 + 3 / 11", 9 + 3.0 / 11)
    test("(9 + 3)", (9 + 3))
    test("(9+3) / 11", (9 + 3.0) / 11)
    test("9 - 12 - 6", 9 - 12 - 6)
    test("9 - (12 - 6)", 9 - (12 - 6))
    test("2*3.14159", 2 * 3.14159)

