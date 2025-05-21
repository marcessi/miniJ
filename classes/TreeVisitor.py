import numpy as np
from grammar.gVisitor import gVisitor

class TreeVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.results = []
        self.variables = {}
        
    def visitProgram(self, ctx):
        # Procesar líneas normales (con salto de línea)
        for line_ctx in ctx.line():
            if line_ctx.assignment():
                assign_stmt_node = line_ctx.assignment()
                self.visit(assign_stmt_node)
            elif line_ctx.expression():
                result = self.visit(line_ctx.expression())
                if result is not None:
                    self.results.append(result)
                    self.print_result(result)
        
        # Procesar la última línea (sin salto de línea)
        if ctx.lastLine():
            last_line = ctx.lastLine()
            if last_line.assignment():
                assign_stmt_node = last_line.assignment()
                self.visit(assign_stmt_node)
            elif last_line.expression():
                result = self.visit(last_line.expression())
                if result is not None:
                    self.results.append(result)
                    self.print_result(result)
        
        return self.results
    
    def print_result(self, result):
        if isinstance(result, np.ndarray):
            result_str = ' '.join(str(x) if x >= 0 else f"_{abs(x)}" for x in result)
        else:
            if result >= 0:
                result_str = str(result)
            else:
                result_str = f"_{abs(result)}"
        print(result_str)

    # Assignment
    def visitAssignmentLabel(self, ctx):
        var_name = ctx.WORD().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return None
    
    # Atomic expressions
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())
    
    def visitNegativeExpr(self, ctx):
        result = self.visit(ctx.atom())
        return -result
    
    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    # Unary operations
    def visitIdentityExpr(self, ctx):
        # ]
        expr = self.visit(ctx.expression())
        # expression is a function
        if callable(expr) and isinstance(expr, type(lambda: None)):
            def identity_composition(x):
                result = expr(x)
                return result
            
            return identity_composition
        # normal case
        return expr

    def visitSizeExpr(self, ctx):
        # # size
        expr = self.visit(ctx.expression())
        # expression is a function
        if callable(expr) and isinstance(expr, type(lambda: None)):
            def size_composition(x):
                result = expr(x)
                
                if isinstance(result, np.ndarray):
                    return len(result)
                else:
                    return 1
            
            return size_composition
        # normal case
        if isinstance(expr, np.ndarray):
            return len(expr)
        else:
            return 1

    def visitSeqExpr(self, ctx):
        # i.
        expr = self.visit(ctx.expression())
        # expression is a function
        if callable(expr) and isinstance(expr, type(lambda: None)):
            def seq_composition(x):
                n = expr(x)
                
                if isinstance(n, np.ndarray):
                    if len(n) == 0:
                        return np.array([])
                    n = n[0]
                
                if n < 0:
                    raise ValueError("i. requiere un argumento no negativo")
                
                return np.arange(n)
            
            return seq_composition
        # normal case
        if isinstance(expr, np.ndarray):
            n = expr[0]
        else:
            n = expr
            
        if n < 0:
            raise ValueError("i. requiere un argumento no negativo")
            
        return np.arange(n)

    def visitModifiedExpr(self, ctx):
        # :op
        expr = self.visit(ctx.expression())
        op = ctx.op.text
        
        def modified_operator(x):
            scalar_input = not isinstance(x, np.ndarray)
            if scalar_input:
                x = np.array([x])
            
            # Evaluar función si lo es
            result = expr(x) if callable(expr) else expr
            
            if not isinstance(result, np.ndarray):
                result = np.array([result])
            
            if op == '+':
                modified = result + result
            elif op == '-':
                modified = result - result
            elif op == '*':
                modified = result * result
            elif op == '%':
                modified = result // result
            elif op == '|':
                modified = result % result
            elif op == '^':
                modified = result ** result
            elif op == '>':
                modified = np.where(result > result, 1, 0)
            elif op == '<':
                modified = np.where(result < result, 1, 0)
            elif op == '>=':
                modified = np.where(result >= result, 1, 0)
            elif op == '<=':
                modified = np.where(result <= result, 1, 0)
            elif op == '=':
                modified = np.where(result == result, 1, 0)
            elif op == '<>':
                modified = np.where(result != result, 1, 0)
            
            if scalar_input and len(modified) == 1:
                return modified[0]
            return modified
        
        # Si la expresión es función, devolvemos una función. Si no, ejecutamos.
        if callable(expr):
            return modified_operator
        else:
            return modified_operator(np.array([0]))

    def visitFoldlExpr(self, ctx):
        expr = self.visit(ctx.expression())
        op = ctx.op.text
        
        def fold_operator(x):
            if not isinstance(x, np.ndarray):
                x = np.array([x])
            
            # Evaluar función si lo es
            result = expr(x) if callable(expr) else expr
            
            if not isinstance(result, np.ndarray):
                result = np.array([result])
            
            if op == '+':
                folded = np.sum(result)
            elif op == '*':
                folded = np.prod(result)
            elif op == '-':
                folded = result[0]
                for i in range(1, len(result)):
                    folded -= result[i]
            elif op == '%':
                folded = result[0]
                for i in range(1, len(result)):
                    folded //= result[i]
            elif op == '|':
                folded = result[0]
                for i in range(1, len(result)):
                    folded %= result[i]
            elif op == '^':
                folded = result[0]
                for i in range(1, len(result)):
                    folded **= result[i]
            elif op == '>':
                folded = 1 if all(result[i] > result[i+1] for i in range(len(result)-1)) else 0
            elif op == '<':
                folded = 1 if all(result[i] < result[i+1] for i in range(len(result)-1)) else 0
            elif op == '>=':
                folded = 1 if all(result[i] >= result[i+1] for i in range(len(result)-1)) else 0
            elif op == '<=':
                folded = 1 if all(result[i] <= result[i+1] for i in range(len(result)-1)) else 0
            elif op == '=':
                folded = 1 if all(result[i] == result[0] for i in range(len(result))) else 0
            elif op == '<>':
                folded = 1 if len(set(result)) == len(result) else 0
            
            return folded
        
        # Si la expresión es función, devolvemos una función. Si no, ejecutamos.
        if callable(expr):
            return fold_operator
        else:
            return fold_operator(np.array([0]))

    # Binary operations
    def visitBinaryExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        op = ctx.op.text

        def binary_operator(x):
            scalar_input = not isinstance(x, np.ndarray)
            if scalar_input:
                x = np.array([x])

            # Evaluar funciones si lo son
            left_val = left(x) if callable(left) else left
            right_val = right(x) if callable(right) else right

            if not isinstance(left_val, np.ndarray):
                left_val = np.array([left_val])
            if not isinstance(right_val, np.ndarray):
                right_val = np.array([right_val])

            if len(left_val) == 1 and len(right_val) > 1:
                left_val = np.full_like(right_val, left_val[0])
            elif len(right_val) == 1 and len(left_val) > 1:
                right_val = np.full_like(left_val, right_val[0])

            if len(left_val) != len(right_val):
                raise Exception("Length error: arrays must have the same length")

            if op == '+':
                result = left_val + right_val
            elif op == '-':
                result = left_val - right_val
            elif op == '*':
                result = left_val * right_val
            elif op == '%':
                result = left_val // right_val
            elif op == '|':
                result = right_val % left_val
            elif op == '^':
                result = left_val ** right_val
            else:
                raise Exception(f"Unsupported operator: {op}")

            if scalar_input and len(result) == 1:
                return result[0]
            return result

        # Si cualquiera es función, devolvemos una función. Si no, ejecutamos.
        if callable(left) or callable(right):
            return binary_operator
        else:
            return binary_operator(np.array([0]))

        
    def visitFlippedBinaryExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        op = ctx.op.text

        def flipped_binary_operator(x):
            scalar_input = not isinstance(x, np.ndarray)
            if scalar_input:
                x = np.array([x])

            # Evaluar funciones si lo son
            left_val = left(x) if callable(left) else left
            right_val = right(x) if callable(right) else right

            if not isinstance(left_val, np.ndarray):
                left_val = np.array([left_val])
            if not isinstance(right_val, np.ndarray):
                right_val = np.array([right_val])

            if len(left_val) == 1 and len(right_val) > 1:
                left_val = np.full_like(right_val, left_val[0])
            elif len(right_val) == 1 and len(left_val) > 1:
                right_val = np.full_like(left_val, right_val[0])

            if len(left_val) != len(right_val):
                raise Exception("Length error: arrays must have the same length")

            if op == '+':
                result = right_val + left_val
            elif op == '-':
                result = right_val - left_val
            elif op == '*':
                result = right_val * left_val
            elif op == '%':
                result = right_val // left_val
            elif op == '|':
                result = left_val % right_val
            elif op == '^':
                result = right_val ** left_val
            else:
                raise Exception(f"Unsupported operator: {op}")

            if scalar_input and len(result) == 1:
                return result[0]
            return result

        # Si cualquiera es función, devolvemos una función. Si no, ejecutamos.
        if callable(left) or callable(right):
            return flipped_binary_operator
        else:
            return flipped_binary_operator(np.array([0]))
        
    def visitSpecialBinaryExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        op = ctx.op.text

        def special_binary_operator(x):
            scalar_input = not isinstance(x, np.ndarray)
            if scalar_input:
                x = np.array([x])

            # Evaluar funciones si lo son
            left_val = left(x) if callable(left) else left
            right_val = right(x) if callable(right) else right

            if op in [',', '#']:
                if not isinstance(left_val, np.ndarray):
                    left_val = np.array([left_val])
                if not isinstance(right_val, np.ndarray):
                    right_val = np.array([right_val])

            if op == ',':
                result = np.concatenate((left_val, right_val))
            elif op == '#':
                mask_arr = np.array(left_val, dtype=int)
                if not np.all((mask_arr == 0) | (mask_arr == 1)):
                    raise Exception("El primer operando del filtro debe ser una máscara de 0s y 1s")
                result = right_val[mask_arr.astype(bool)]
            elif op == '{':
                try:
                    if isinstance(left_val, np.ndarray):
                        if np.any(np.array(left_val, dtype=int) < 0):
                            raise Exception("Índices negativos no permitidos")
                        result = right_val[np.array(left_val, dtype=int)]
                    else:
                        if left_val < 0:
                            raise Exception("Índice negativo no permitido")
                        result = right_val[left_val]
                except IndexError:
                    raise Exception("Índice fuera de rango")

            if scalar_input and op != '{' and isinstance(result, np.ndarray) and len(result) == 1:
                return result[0]
            return result

        # Si cualquiera es función, devolvemos una función. Si no, ejecutamos.
        if callable(left) or callable(right):
            return special_binary_operator
        else:
            return special_binary_operator(np.array([0]))
            
    def visitRelationalExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        op = ctx.op.text

        def relational_operator(x):
            scalar_input = not isinstance(x, np.ndarray)
            if scalar_input:
                x = np.array([x])

            # Evaluar funciones si lo son
            left_val = left(x) if callable(left) else left
            right_val = right(x) if callable(right) else right

            if not isinstance(left_val, np.ndarray):
                left_val = np.array([left_val])
            if not isinstance(right_val, np.ndarray):
                right_val = np.array([right_val])

            if len(left_val) == 1 and len(right_val) > 1:
                left_val = np.full_like(right_val, left_val[0])
            elif len(right_val) == 1 and len(left_val) > 1:
                right_val = np.full_like(left_val, right_val[0])

            if len(left_val) != len(right_val):
                raise Exception("Length error: arrays must have the same length")

            if op == '>':
                result = np.where(left_val > right_val, 1, 0)
            elif op == '<':
                result = np.where(left_val < right_val, 1, 0)
            elif op == '>=':
                result = np.where(left_val >= right_val, 1, 0)
            elif op == '<=':
                result = np.where(left_val <= right_val, 1, 0)
            elif op == '=':
                result = np.where(left_val == right_val, 1, 0)
            elif op == '<>':
                result = np.where(left_val != right_val, 1, 0)
            else:
                raise Exception(f"Unsupported relational operator: {op}")

            if scalar_input and len(result) == 1:
                return result[0]
            return result

        # Si cualquiera es función, devolvemos una función. Si no, ejecutamos.
        if callable(left) or callable(right):
            return relational_operator
        else:
            return relational_operator(np.array([0]))     

    # Function application
    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.WORD().getText()
        if func_name not in self.variables:
            raise NameError(f"Error: Function '{func_name}' not defined.")
            
        func = self.variables[func_name]
        if not callable(func):
            raise TypeError(f"Error: '{func_name}' is not a function.")
            
        arg = self.visit(ctx.expression())
        
        return func(arg)
    
    def visitComposeExpr(self, ctx):
        # :@
        f = self.visit(ctx.expression(1))  # Right function
        g = self.visit(ctx.expression(0))  # Left function
        
        if not callable(f) or not callable(g):
            raise TypeError("Cannot compose non-function values")
        
        def composed_func(x):
            return g(f(x))
        
        return composed_func

    # Atoms
    def visitListAtom(self, ctx):
        ints = []

        for child in ctx.getChildren():
            text = child.getText()
            if text.startswith('_'):
                ints.append(-int(text[1:]))
            else:
                ints.append(int(text))

        if len(ints) == 1:
            return ints[0]
        return np.array(ints)
    
    def visitVariableAtom(self, ctx):
        var_name = ctx.WORD().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise NameError(f"Error: Variable '{var_name}' no definida.")
      
    def visitIdentityFuncExpr(self, ctx):
        def identity_func(x):
            return x
        return identity_func
    
    def visitSizeFuncExpr(self, ctx):
        def size_func(x):
            if not isinstance(x, np.ndarray):
                return 1
            else:
                return len(x)
        
        return size_func

    def visitSeqFuncExpr(self, ctx):
        def seq_func(x):
            if isinstance(x, np.ndarray):
                if len(x) == 0:
                    return np.array([])
                x = x[0]
            
            if x < 0:
                raise ValueError("i. requiere un argumento no negativo")
            
            return np.arange(x)
        
        return seq_func
    
    def visitModifiedFuncExpr(self, ctx):
        op = ctx.op.text
        
        def modified_func(x):
            scalar_input = not isinstance(x, np.ndarray)
            
            if scalar_input:
                x_array = np.array([x])
            else:
                x_array = x
                
            if op == '+':
                result = x_array + x_array
            elif op == '-':
                result = x_array - x_array
            elif op == '*':
                result = x_array * x_array
            elif op == '%':
                result = x_array // x_array
            elif op == '|':
                result = x_array % x_array
            elif op == '^':
                result = x_array ** x_array
            elif op == '>':
                result = np.where(x_array > x_array, 1, 0)
            elif op == '<':
                result = np.where(x_array < x_array, 1, 0)
            elif op == '>=':
                result = np.where(x_array >= x_array, 1, 0)
            elif op == '<=':
                result = np.where(x_array <= x_array, 1, 0)
            elif op == '=':
                result = np.where(x_array == x_array, 1, 0)
            elif op == '<>':
                result = np.where(x_array != x_array, 1, 0)
                
            if scalar_input:
                return result[0]
            return result
        
        return modified_func

    def visitFoldlFuncExpr(self, ctx):
        op = ctx.op.text
        
        def fold_func(x):
            if not isinstance(x, np.ndarray):
                x = np.array([x])
                
            if op == '+':
                return np.sum(x)
            elif op == '*':
                return np.prod(x)
            elif op == '-':
                result = x[0]
                for i in range(1, len(x)):
                    result -= x[i]
                return result
            elif op == '%':
                result = x[0]
                for i in range(1, len(x)):
                    result //= x[i]
                return result
            elif op == '|':
                result = x[0]
                for i in range(1, len(x)):
                    result %= x[i]
                return result
            elif op == '^':
                result = x[0]
                for i in range(1, len(x)):
                    result **= x[i]
                return result
            elif op == '>':
                return 1 if all(x[i] > x[i+1] for i in range(len(x)-1)) else 0
            elif op == '<':
                return 1 if all(x[i] < x[i+1] for i in range(len(x)-1)) else 0
            elif op == '>=':
                return 1 if all(x[i] >= x[i+1] for i in range(len(x)-1)) else 0
            elif op == '<=':
                return 1 if all(x[i] <= x[i+1] for i in range(len(x)-1)) else 0
            elif op == '=':
                return 1 if all(x[i] == x[0] for i in range(len(x))) else 0
            elif op == '<>':
                return 1 if len(set(x)) == len(x) else 0
        
        return fold_func