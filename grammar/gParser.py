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
        4,1,31,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,3,0,20,8,0,1,0,1,0,1,1,1,1,3,1,26,
        8,1,1,1,3,1,29,8,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,3,2,40,
        8,2,1,2,3,2,43,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,71,
        8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,5,4,5,95,8,5,11,5,12,5,96,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,107,8,5,1,5,0,1,8,6,0,2,4,6,8,10,
        0,5,1,0,8,19,1,0,8,13,2,0,6,6,23,24,1,0,14,19,1,0,26,27,130,0,15,
        1,0,0,0,2,35,1,0,0,0,4,39,1,0,0,0,6,44,1,0,0,0,8,70,1,0,0,0,10,106,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,18,20,3,4,2,0,19,18,1,
        0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,
        26,3,6,3,0,24,26,3,8,4,0,25,23,1,0,0,0,25,24,1,0,0,0,26,28,1,0,0,
        0,27,29,5,31,0,0,28,27,1,0,0,0,28,29,1,0,0,0,29,30,1,0,0,0,30,31,
        5,30,0,0,31,36,1,0,0,0,32,33,5,31,0,0,33,36,5,30,0,0,34,36,5,30,
        0,0,35,25,1,0,0,0,35,32,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,40,
        3,6,3,0,38,40,3,8,4,0,39,37,1,0,0,0,39,38,1,0,0,0,40,42,1,0,0,0,
        41,43,5,31,0,0,42,41,1,0,0,0,42,43,1,0,0,0,43,5,1,0,0,0,44,45,5,
        28,0,0,45,46,5,1,0,0,46,47,3,8,4,0,47,7,1,0,0,0,48,49,6,4,-1,0,49,
        71,3,10,5,0,50,51,5,2,0,0,51,71,3,10,5,0,52,53,5,3,0,0,53,54,3,8,
        4,0,54,55,5,4,0,0,55,71,1,0,0,0,56,57,5,5,0,0,57,71,3,8,4,11,58,
        59,5,6,0,0,59,71,3,8,4,10,60,61,5,7,0,0,61,71,3,8,4,9,62,63,7,0,
        0,0,63,64,5,20,0,0,64,71,3,8,4,8,65,66,7,0,0,0,66,67,5,21,0,0,67,
        71,3,8,4,7,68,69,5,28,0,0,69,71,3,8,4,2,70,48,1,0,0,0,70,50,1,0,
        0,0,70,52,1,0,0,0,70,56,1,0,0,0,70,58,1,0,0,0,70,60,1,0,0,0,70,62,
        1,0,0,0,70,65,1,0,0,0,70,68,1,0,0,0,71,90,1,0,0,0,72,73,10,6,0,0,
        73,74,7,1,0,0,74,89,3,8,4,6,75,76,10,5,0,0,76,77,7,1,0,0,77,78,5,
        22,0,0,78,89,3,8,4,6,79,80,10,4,0,0,80,81,7,2,0,0,81,89,3,8,4,4,
        82,83,10,3,0,0,83,84,7,3,0,0,84,89,3,8,4,3,85,86,10,1,0,0,86,87,
        5,25,0,0,87,89,3,8,4,1,88,72,1,0,0,0,88,75,1,0,0,0,88,79,1,0,0,0,
        88,82,1,0,0,0,88,85,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,
        0,0,0,91,9,1,0,0,0,92,90,1,0,0,0,93,95,7,4,0,0,94,93,1,0,0,0,95,
        96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,107,1,0,0,0,98,107,5,28,
        0,0,99,107,5,5,0,0,100,107,5,6,0,0,101,107,5,7,0,0,102,103,7,0,0,
        0,103,107,5,20,0,0,104,105,7,0,0,0,105,107,5,21,0,0,106,94,1,0,0,
        0,106,98,1,0,0,0,106,99,1,0,0,0,106,100,1,0,0,0,106,101,1,0,0,0,
        106,102,1,0,0,0,106,104,1,0,0,0,107,11,1,0,0,0,12,15,19,25,28,35,
        39,42,70,88,90,96,106
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=:'", "'_'", "'('", "')'", "']'", "'#'", 
                     "'i.'", "'+'", "'-'", "'*'", "'%'", "'|'", "'^'", "'>'", 
                     "'<'", "'>='", "'<='", "'='", "'<>'", "':'", "'/'", 
                     "'~'", "','", "'{'", "'@:'" ]

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
    RULE_lastLine = 2
    RULE_assignment = 3
    RULE_expression = 4
    RULE_atom = 5

    ruleNames =  [ "program", "line", "lastLine", "assignment", "expression", 
                   "atom" ]

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


        def lastLine(self):
            return self.getTypedRuleContext(gParser.LastLineContext,0)


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
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 12
                    self.line() 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 470810604) != 0):
                self.state = 18
                self.lastLine()


            self.state = 21
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

        def NL(self):
            return self.getToken(gParser.NL, 0)

        def assignment(self):
            return self.getTypedRuleContext(gParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def COMMENT(self):
            return self.getToken(gParser.COMMENT, 0)

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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.assignment()
                    pass

                elif la_ == 2:
                    self.state = 24
                    self.expression(0)
                    pass


                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 27
                    self.match(gParser.COMMENT)


                self.state = 30
                self.match(gParser.NL)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(gParser.COMMENT)
                self.state = 33
                self.match(gParser.NL)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(gParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LastLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(gParser.AssignmentContext,0)


        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def COMMENT(self):
            return self.getToken(gParser.COMMENT, 0)

        def getRuleIndex(self):
            return gParser.RULE_lastLine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLastLine" ):
                return visitor.visitLastLine(self)
            else:
                return visitor.visitChildren(self)




    def lastLine(self):

        localctx = gParser.LastLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lastLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 37
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 38
                self.expression(0)
                pass


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 41
                self.match(gParser.COMMENT)


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
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            localctx = gParser.AssignmentLabelContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(gParser.WORD)
            self.state = 45
            self.match(gParser.T__0)
            self.state = 46
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


    class SeqExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(gParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqExpr" ):
                return visitor.visitSeqExpr(self)
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = gParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 49
                self.atom()
                pass

            elif la_ == 2:
                localctx = gParser.NegativeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(gParser.T__1)
                self.state = 51
                self.atom()
                pass

            elif la_ == 3:
                localctx = gParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(gParser.T__2)
                self.state = 53
                self.expression(0)
                self.state = 54
                self.match(gParser.T__3)
                pass

            elif la_ == 4:
                localctx = gParser.IdentityExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(gParser.T__4)
                self.state = 57
                self.expression(11)
                pass

            elif la_ == 5:
                localctx = gParser.SizeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(gParser.T__5)
                self.state = 59
                self.expression(10)
                pass

            elif la_ == 6:
                localctx = gParser.SeqExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(gParser.T__6)
                self.state = 61
                self.expression(9)
                pass

            elif la_ == 7:
                localctx = gParser.ModifiedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048320) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 63
                self.match(gParser.T__19)
                self.state = 64
                self.expression(8)
                pass

            elif la_ == 8:
                localctx = gParser.FoldlExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048320) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 66
                self.match(gParser.T__20)
                self.state = 67
                self.expression(7)
                pass

            elif la_ == 9:
                localctx = gParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(gParser.WORD)
                self.state = 69
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = gParser.BinaryExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 72
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = gParser.FlippedBinaryExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.match(gParser.T__21)
                        self.state = 78
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = gParser.SpecialBinaryExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 79
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 80
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25165888) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = gParser.RelationalExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 83
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = gParser.ComposeExprContext(self, gParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 85
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 86
                        self.match(gParser.T__24)
                        self.state = 87
                        self.expression(1)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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


    class SeqFuncExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqFuncExpr" ):
                return visitor.visitSeqFuncExpr(self)
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
        self.enterRule(localctx, 10, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = gParser.ListAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 94 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 93
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 96 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass

            elif la_ == 2:
                localctx = gParser.VariableAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(gParser.WORD)
                pass

            elif la_ == 3:
                localctx = gParser.IdentityFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.match(gParser.T__4)
                pass

            elif la_ == 4:
                localctx = gParser.SizeFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.match(gParser.T__5)
                pass

            elif la_ == 5:
                localctx = gParser.SeqFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.match(gParser.T__6)
                pass

            elif la_ == 6:
                localctx = gParser.ModifiedFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 102
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048320) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 103
                self.match(gParser.T__19)
                pass

            elif la_ == 7:
                localctx = gParser.FoldlFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 104
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048320) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 105
                self.match(gParser.T__20)
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
        self._predicates[4] = self.expression_sempred
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
         




