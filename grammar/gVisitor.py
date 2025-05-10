# Generated from grammar/g.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete generic visitor for a parse tree produced by gParser.

class gVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gParser#program.
    def visitProgram(self, ctx:gParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#line.
    def visitLine(self, ctx:gParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#assignmentLabel.
    def visitAssignmentLabel(self, ctx:gParser.AssignmentLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#specialBinaryExpr.
    def visitSpecialBinaryExpr(self, ctx:gParser.SpecialBinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#sizeExpr.
    def visitSizeExpr(self, ctx:gParser.SizeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#negativeExpr.
    def visitNegativeExpr(self, ctx:gParser.NegativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#atomExpr.
    def visitAtomExpr(self, ctx:gParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#binaryExpr.
    def visitBinaryExpr(self, ctx:gParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#relationalExpr.
    def visitRelationalExpr(self, ctx:gParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#parenExpr.
    def visitParenExpr(self, ctx:gParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#modifiedExpr.
    def visitModifiedExpr(self, ctx:gParser.ModifiedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#identityExpr.
    def visitIdentityExpr(self, ctx:gParser.IdentityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#flippedBinaryExpr.
    def visitFlippedBinaryExpr(self, ctx:gParser.FlippedBinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#composeExpr.
    def visitComposeExpr(self, ctx:gParser.ComposeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#functionCallExpr.
    def visitFunctionCallExpr(self, ctx:gParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#iotiExpr.
    def visitIotiExpr(self, ctx:gParser.IotiExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#foldlExpr.
    def visitFoldlExpr(self, ctx:gParser.FoldlExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#listAtom.
    def visitListAtom(self, ctx:gParser.ListAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#variableAtom.
    def visitVariableAtom(self, ctx:gParser.VariableAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#identityFuncExpr.
    def visitIdentityFuncExpr(self, ctx:gParser.IdentityFuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#sizeFuncExpr.
    def visitSizeFuncExpr(self, ctx:gParser.SizeFuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#iotiFuncExpr.
    def visitIotiFuncExpr(self, ctx:gParser.IotiFuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#modifiedFuncExpr.
    def visitModifiedFuncExpr(self, ctx:gParser.ModifiedFuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#foldlFuncExpr.
    def visitFoldlFuncExpr(self, ctx:gParser.FoldlFuncExprContext):
        return self.visitChildren(ctx)



del gParser