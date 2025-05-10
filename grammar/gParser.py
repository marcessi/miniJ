# Generated from grammar/g.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,
        0,10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,3,1,21,8,1,1,1,1,1,1,1,1,1,3,
        1,27,8,1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,80,8,3,10,3,12,3,83,9,3,1,4,4,4,86,
        8,4,11,4,12,4,87,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,98,8,4,1,4,
        0,1,6,5,0,2,4,6,8,0,4,1,0,8,13,2,0,6,6,17,18,1,0,19,24,1,0,26,27,
        120,0,13,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,61,1,0,0,0,8,97,1,0,
        0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,
        1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,
        20,3,4,2,0,19,21,5,31,0,0,20,19,1,0,0,0,20,21,1,0,0,0,21,22,1,0,
        0,0,22,23,5,30,0,0,23,34,1,0,0,0,24,26,3,6,3,0,25,27,5,31,0,0,26,
        25,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,29,5,30,0,0,29,34,1,0,
        0,0,30,31,5,31,0,0,31,34,5,30,0,0,32,34,5,30,0,0,33,18,1,0,0,0,33,
        24,1,0,0,0,33,30,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,5,28,0,
        0,36,37,5,1,0,0,37,38,3,6,3,0,38,5,1,0,0,0,39,40,6,3,-1,0,40,62,
        3,8,4,0,41,42,5,2,0,0,42,62,3,8,4,0,43,44,5,3,0,0,44,45,3,6,3,0,
        45,46,5,4,0,0,46,62,1,0,0,0,47,48,5,5,0,0,48,62,3,6,3,11,49,50,5,
        6,0,0,50,62,3,6,3,10,51,52,5,7,0,0,52,62,3,6,3,9,53,54,7,0,0,0,54,
        55,5,14,0,0,55,62,3,6,3,8,56,57,7,0,0,0,57,58,5,15,0,0,58,62,3,6,
        3,7,59,60,5,28,0,0,60,62,3,6,3,2,61,39,1,0,0,0,61,41,1,0,0,0,61,
        43,1,0,0,0,61,47,1,0,0,0,61,49,1,0,0,0,61,51,1,0,0,0,61,53,1,0,0,
        0,61,56,1,0,0,0,61,59,1,0,0,0,62,81,1,0,0,0,63,64,10,6,0,0,64,65,
        7,0,0,0,65,80,3,6,3,6,66,67,10,5,0,0,67,68,7,0,0,0,68,69,5,16,0,
        0,69,80,3,6,3,6,70,71,10,4,0,0,71,72,7,1,0,0,72,80,3,6,3,4,73,74,
        10,3,0,0,74,75,7,2,0,0,75,80,3,6,3,3,76,77,10,1,0,0,77,78,5,25,0,
        0,78,80,3,6,3,1,79,63,1,0,0,0,79,66,1,0,0,0,79,70,1,0,0,0,79,73,
        1,0,0,0,79,76,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,
        82,7,1,0,0,0,83,81,1,0,0,0,84,86,7,3,0,0,85,84,1,0,0,0,86,87,1,0,
        0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,98,1,0,0,0,89,98,5,28,0,0,90,
        98,5,5,0,0,91,98,5,6,0,0,92,98,5,7,0,0,93,94,7,0,0,0,94,98,5,14,
        0,0,95,96,7,0,0,0,96,98,5,15,0,0,97,85,1,0,0,0,97,89,1,0,0,0,97,
        90,1,0,0,0,97,91,1,0,0,0,97,92,1,0,0,0,97,93,1,0,0,0,97,95,1,0,0,
        0,98,9,1,0,0,0,9,13,20,26,33,61,79,81,87,97
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=:'", "'_'", "'('", "')'", "']'", "'#'", 
                     "'i.'", "'+'", "'-'", "'*'", "'%'", "'|'", "'^'", "':'", 
                     "'/'", "'~'", "','", "'{'", "'>'", "'<'", "'>='", "'<='", 
                     "'='", "'<>'", "'@:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "NEG_INT", "WORD", 
                      "WS", "NL", "COMMENT" ]

    RULE_program = 0
    RULE_line = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_atom = 4

    ruleNames =  [ "program", "line", "assignment", "expression", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    INT=26
    NEG_INT=27
    WORD=28
    WS=29
    NL=30
    COMMENT=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.LineContext)
            else:
                return self.getTypedRuleContext(gParser.LineContext,i)


        def getRuleIndex(self):
            return gParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3691003884) != 0):
                self.state = 10
                self.line()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(gParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(gParser.AssignmentContext,0)


        def NL(self):
            return self.getToken(gParser.NL, 0)

        def COMMENT(self):
            return self.getToken(gParser.COMMENT, 0)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def getRuleIndex(self):
            return gParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = gParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.assignment()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 19
                    self.match(gParser.COMMENT)


                self.state = 22
                self.match(gParser.NL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.expression(0)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 25
                    self.match(gParser.COMMENT)


                self.state = 28
                self.match(gParser.NL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(gParser.COMMENT)
                self.state = 31
                self.match(gParser.NL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(gParser.NL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentLabelContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(gParser.WORD, 0)
        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentLabel" ):
                return visitor.visitAssignmentLabel(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = gParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            localctx = gParser.AssignmentLabelContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(gParser.WORD)
            self.state = 36
            self.match(gParser.T__0)
            self.state = 37
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SpecialBinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecialBinaryExpr" ):
                return visitor.visitSpecialBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class SizeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeExpr" ):
                return visitor.visitSizeExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegativeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(gParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativeExpr" ):
                return visitor.visitNegativeExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(gParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModifiedExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifiedExpr" ):
                return visitor.visitModifiedExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdentityExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentityExpr" ):
                return visitor.visitIdentityExpr(self)
            else:
                return visitor.visitChildren(self)


    class FlippedBinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlippedBinaryExpr" ):
                return visitor.visitFlippedBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComposeExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposeExpr" ):
                return visitor.visitComposeExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(gParser.WORD, 0)
        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class IotiExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIotiExpr" ):
                return visitor.visitIotiExpr(self)
            else:
                return visitor.visitChildren(self)


    class FoldlExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFoldlExpr" ):
                return visitor.visitFoldlExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = gParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 40
                self.atom()
                pass

            elif la_ == 2:
                localctx = gParser.NegativeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(gParser.T__1)
                self.state = 42
                self.atom()
                pass

            elif la_ == 3:
                localctx = gParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(gParser.T__2)
                self.state = 44
                self.expression(0)
                self.state = 45
                self.match(gParser.T__3)
                pass

            elif la_ == 4:
                localctx = gParser.IdentityExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(gParser.T__4)
                self.state = 48
                self.expression(11)
                pass

            elif la_ == 5:
                localctx = gParser.SizeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(gParser.T__5)
                self.state = 50
                self.expression(10)
                pass

            elif la_ == 6:
                localctx = gParser.IotiExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(gParser.T__6)
                self.state = 52
                self.expression(9)
                pass

            elif la_ == 7:
                localctx = gParser.ModifiedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54
                self.match(gParser.T__13)
                self.state = 55
                self.expression(8)
                pass

            elif la_ == 8:
                localctx = gParser.FoldlExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                self.match(gParser.T__14)
                self.state = 58
                self.expression(7)
                pass

            elif la_ == 9:
                localctx = gParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(gParser.WORD)
                self.state = 60
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = gParser.BinaryExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = gParser.FlippedBinaryExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 66
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.match(gParser.T__15)
                        self.state = 69
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = gParser.SpecialBinaryExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 70
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 71
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 393280) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = gParser.RelationalExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 74
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 75
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = gParser.ComposeExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 77
                        self.match(gParser.T__24)
                        self.state = 78
                        self.expression(1)
                        pass

             
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentityFuncExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentityFuncExpr" ):
                return visitor.visitIdentityFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class ListAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.INT)
            else:
                return self.getToken(gParser.INT, i)
        def NEG_INT(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NEG_INT)
            else:
                return self.getToken(gParser.NEG_INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListAtom" ):
                return visitor.visitListAtom(self)
            else:
                return visitor.visitChildren(self)


    class VariableAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(gParser.WORD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAtom" ):
                return visitor.visitVariableAtom(self)
            else:
                return visitor.visitChildren(self)


    class SizeFuncExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeFuncExpr" ):
                return visitor.visitSizeFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class IotiFuncExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIotiFuncExpr" ):
                return visitor.visitIotiFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class FoldlFuncExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFoldlFuncExpr" ):
                return visitor.visitFoldlFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class ModifiedFuncExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifiedFuncExpr" ):
                return visitor.visitModifiedFuncExpr(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = gParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = gParser.ListAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 85 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 84
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 87 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 2:
                localctx = gParser.VariableAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(gParser.WORD)
                pass

            elif la_ == 3:
                localctx = gParser.IdentityFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(gParser.T__4)
                pass

            elif la_ == 4:
                localctx = gParser.SizeFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(gParser.T__5)
                pass

            elif la_ == 5:
                localctx = gParser.IotiFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.match(gParser.T__6)
                pass

            elif la_ == 6:
                localctx = gParser.ModifiedFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 94
                self.match(gParser.T__13)
                pass

            elif la_ == 7:
                localctx = gParser.FoldlFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 96
                self.match(gParser.T__14)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




