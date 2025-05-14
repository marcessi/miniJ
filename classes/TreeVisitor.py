import numpy as np
from grammar.gVisitor import gVisitor

class TreeVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self.results = []
        self.variables = {}
        
    def visitProgram(self, ctx):
        print(f"Procesando {len(list(ctx.line()))} líneas")
        for line_ctx in ctx.line():
            if line_ctx.assignment():
                assign_stmt_node = line_ctx.assignment()
                self.visit(assign_stmt_node)
            elif line_ctx.expression():
                expr_text = self.preformat_expr_text(line_ctx.expression().getText())
                
                print(f"Procesando expresión: {expr_text}")
                
                result = self.visit(line_ctx.expression())
                if result is not None:
                    self.results.append(result)
                    print("Resultado: ", end="")
                    self.print_result(result)
        
        return self.results

    def preformat_expr_text(self, text):
        formatted = []
        i = 0
        while i < len(text):
            if text[i] == '_' and i+1 < len(text) and text[i+1].isdigit():
                neg_num = '_'
                i += 1
                while i < len(text) and text[i].isdigit():
                    neg_num += text[i]
                    i += 1
                formatted.append(neg_num)
            elif text[i].isalpha():
                ident = text[i]
                i += 1
                while i < len(text) and (text[i].isalnum() or text[i] == '_'):
                    ident += text[i]
                    i += 1
                formatted.append(ident)
            elif text[i].isdigit():
                num = text[i]
                i += 1
                while i < len(text) and text[i].isdigit():
                    num += text[i]
                    i += 1
                formatted.append(' '.join(num))
            else:
                formatted.append(text[i])
                i += 1
        
        return ' '.join(formatted)
    
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
        
        # expression is a function
        if callable(expr) and isinstance(expr, type(lambda: None)):
            def modified_composition(x):
                result = expr(x)
                
                scalar_input = not isinstance(result, np.ndarray)
                
                if scalar_input:
                    result_array = np.array([result])
                else:
                    result_array = result
                    
                if op == '+':
                    modified = result_array + result_array
                elif op == '-':
                    modified = result_array - result_array
                elif op == '*':
                    modified = result_array * result_array
                elif op == '%':
                    modified = result_array // result_array
                elif op == '|':
                    modified = result_array % result_array
                elif op == '^':
                    modified = result_array ** result_array
                elif op == '>':
                    modified = np.where(result_array > result_array, 1, 0)
                elif op == '<':
                    modified = np.where(result_array < result_array, 1, 0)
                elif op == '>=':
                    modified = np.where(result_array >= result_array, 1, 0)
                elif op == '<=':
                    modified = np.where(result_array <= result_array, 1, 0)
                elif op == '=':
                    modified = np.where(result_array == result_array, 1, 0)
                elif op == '<>':
                    modified = np.where(result_array != result_array, 1, 0)
                    
                if scalar_input and len(modified) == 1:
                    return modified[0]
                return modified
                
            return modified_composition
        
        # normal case
        scalar_input = not isinstance(expr, np.ndarray)
        if scalar_input:
            expr = np.array([expr])
        
        if op == '+':
            result = expr + expr
        elif op == '-':
            result = expr - expr
        elif op == '*':
            result = expr * expr
        elif op == '%':
            result = expr // expr
        elif op == '|':
            result = expr % expr
        elif op == '^':
            result = expr ** expr
        elif op == '>':
            result = np.where(expr > expr, 1, 0)
        elif op == '<':
            result = np.where(expr < expr, 1, 0)
        elif op == '>=':
            result = np.where(expr >= expr, 1, 0)
        elif op == '<=':
            result = np.where(expr <= expr, 1, 0)
        elif op == '=':
            result = np.where(expr == expr, 1, 0)
        elif op == '<>':
            result = np.where(expr != expr, 1, 0)
        
        if scalar_input and len(result) == 1:
            return result[0]
        return result

    def visitFoldlExpr(self, ctx):
        expr = self.visit(ctx.expression())
        op = ctx.op.text
        
        # expression is a function
        if callable(expr) and isinstance(expr, type(lambda: None)):
            def fold_composition(x):
                result = expr(x)
                
                if not isinstance(result, np.ndarray):
                    result = np.array([result])
                    
                if op == '+':
                    return np.sum(result)
                elif op == '*':
                    return np.prod(result)
                elif op == '-':
                    result_val = result[0]
                    for i in range(1, len(result)):
                        result_val -= result[i]
                    return result_val
                elif op == '%':
                    result_val = result[0]
                    for i in range(1, len(result)):
                        result_val //= result[i]
                    return result_val
                elif op == '|':
                    result_val = result[0]
                    for i in range(1, len(result)):
                        result_val %= result[i]
                    return result_val
                elif op == '^':
                    result_val = result[0]
                    for i in range(1, len(result)):
                        result_val **= result[i]
                    return result_val
                elif op == '>':
                    return 1 if all(result[i] > result[i+1] for i in range(len(result)-1)) else 0
                elif op == '<':
                    return 1 if all(result[i] < result[i+1] for i in range(len(result)-1)) else 0
                elif op == '>=':
                    return 1 if all(result[i] >= result[i+1] for i in range(len(result)-1)) else 0
                elif op == '<=':
                    return 1 if all(result[i] <= result[i+1] for i in range(len(result)-1)) else 0
                elif op == '=':
                    return 1 if all(result[i] == result[0] for i in range(len(result))) else 0
                elif op == '<>':
                    return 1 if len(set(result)) == len(result) else 0
            
            return fold_composition
        
        # normal case
        if not isinstance(expr, np.ndarray):
            expr = np.array([expr])
        
        if op == '+':
            return np.sum(expr)
        elif op == '*':
            return np.prod(expr)
        elif op == '-':
            result = expr[0]
            for i in range(1, len(expr)):
                result -= expr[i]
            return result
        elif op == '%':
            result = expr[0]
            for i in range(1, len(expr)):
                result //= expr[i]
            return result
        elif op == '|':
            result = expr[0]
            for i in range(1, len(expr)):
                result %= expr[i]
            return result
        elif op == '^':
            result = expr[0]
            for i in range(1, len(expr)):
                result **= expr[i]
            return result
        elif op == '>':
            return 1 if all(expr[i] > expr[i+1] for i in range(len(expr)-1)) else 0
        elif op == '<':
            return 1 if all(expr[i] < expr[i+1] for i in range(len(expr)-1)) else 0
        elif op == '>=':
            return 1 if all(expr[i] >= expr[i+1] for i in range(len(expr)-1)) else 0
        elif op == '<=':
            return 1 if all(expr[i] <= expr[i+1] for i in range(len(expr)-1)) else 0
        elif op == '=':
            return 1 if all(expr[i] == expr[0] for i in range(len(expr))) else 0
        elif op == '<>':
            return 1 if len(set(expr)) == len(expr) else 0

    #Binary operations
    def visitBinaryExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        
        op = ctx.op.text

        # both parameters are functions
        if callable(left) and callable(right):
            def function_with_both_functions(x):
                left_result = left(x)
                right_result = right(x)
                
                if not isinstance(left_result, np.ndarray):
                    left_result = np.array([left_result])
                if not isinstance(right_result, np.ndarray):
                    right_result = np.array([right_result])
                
                if len(left_result) == 1 and len(right_result) > 1:
                    left_result = np.full_like(right_result, left_result[0])
                elif len(right_result) == 1 and len(left_result) > 1:
                    right_result = np.full_like(left_result, right_result[0])
                
                if len(left_result) != len(right_result):
                    raise Exception("Length error: arrays must have the same length")
                    
                scalar_input = not isinstance(x, np.ndarray)
                    
                if op == '+':
                    result = left_result + right_result
                elif op == '-':
                    result = left_result - right_result
                elif op == '*':
                    result = left_result * right_result
                elif op == '%':
                    result = left_result // right_result
                elif op == '|':
                    result = right_result % left_result
                elif op == '^':
                    result = left_result ** right_result
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                
            return function_with_both_functions
        
        # first parameter is a function
        if callable(left):
            def function_with_left_function(x):
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                left_result = left(x)
                
                if not isinstance(left_result, np.ndarray):
                    left_result = np.array([left_result])
                    
                if len(left_result) == 1 and len(x) > 1:
                    left_result = np.full_like(x, left_result[0])
                    
                if op == '+':
                    result = left_result + right
                elif op == '-':
                    result = left_result - right
                elif op == '*':
                    result = left_result * right
                elif op == '%':
                    result = left_result // right
                elif op == '|':
                    result = right % left_result
                elif op == '^':
                    result = left_result ** right
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                    
            return function_with_left_function
    
        # second parameter is a function
        if callable(right):
            def function_with_right_function(x):
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                right_result = right(x)
                
                if not isinstance(right_result, np.ndarray):
                    right_result = np.array([right_result])
                    
                if len(right_result) == 1 and len(x) > 1:
                    right_result = np.full_like(x, right_result[0])
                    
                if op == '+':
                    result = left + right_result
                elif op == '-':
                    result = left - right_result
                elif op == '*':
                    result = left * right_result
                elif op == '%':
                    result = left // right_result
                elif op == '|':
                    result = right_result % left
                elif op == '^':
                    result = left ** right_result
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                    
            return function_with_right_function

        
        # normal case
        if not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray):
            right = np.array([right])
        
        if len(left) == 1 and len(right) > 1:
            left = np.full_like(right, left[0])
        elif len(right) == 1 and len(left) > 1:
            right = np.full_like(left, right[0])
        
        if len(left) != len(right):
            raise Exception("Length error: arrays must have the same length")
        
        op = ctx.op.text
        
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '%':
            return left // right
        elif op == '|':
            return right % left
        elif op == '^':
            return left ** right
        
    def visitFlippedBinaryExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))

        op = ctx.op.text
        
        # both parameters are functions
        if callable(left) and callable(right):
            def function_with_both_functions(x):
                left_result = left(x)
                right_result = right(x)
                
                if not isinstance(left_result, np.ndarray):
                    left_result = np.array([left_result])
                if not isinstance(right_result, np.ndarray):
                    right_result = np.array([right_result])
                
                if len(left_result) == 1 and len(right_result) > 1:
                    left_result = np.full_like(right_result, left_result[0])
                elif len(right_result) == 1 and len(left_result) > 1:
                    right_result = np.full_like(left_result, right_result[0])
                
                if len(left_result) != len(right_result):
                    raise Exception("Length error: arrays must have the same length")
                    
                scalar_input = not isinstance(x, np.ndarray)
                    
                if op == '+':
                    result = right_result + left_result
                elif op == '-':
                    result = right_result - left_result
                elif op == '*':
                    result = right_result * left_result
                elif op == '%':
                    result = right_result // left_result
                elif op == '|':
                    result = left_result % right_result
                elif op == '^':
                    result = right_result ** left_result
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                
            return function_with_both_functions

        # first parameter is a function
        if callable(left):
            def function_with_left_function(x):
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                left_result = left(x)
                
                if not isinstance(left_result, np.ndarray):
                    left_result = np.array([left_result])
                    
                if len(left_result) == 1 and len(x) > 1:
                    left_result = np.full_like(x, left_result[0])
                    
                if op == '+':
                    result = right + left_result
                elif op == '-':
                    result = right - left_result
                elif op == '*':
                    result = right * left_result
                elif op == '%':
                    result = right // left_result
                elif op == '|':
                    result = left_result % right
                elif op == '^':
                    result = right ** left_result
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                    
            return function_with_left_function

        # second parameter is a function
        if callable(right):
            def function_with_right_function(x):
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                right_result = right(x)
                
                if not isinstance(right_result, np.ndarray):
                    right_result = np.array([right_result])
                    
                if len(right_result) == 1 and len(x) > 1:
                    right_result = np.full_like(x, right_result[0])
                    
                if op == '+':
                    result = right_result + left
                elif op == '-':
                    result = right_result - left
                elif op == '*':
                    result = right_result * left
                elif op == '%':
                    result = right_result // left
                elif op == '|':
                    result = left % right_result
                elif op == '^':
                    result = right_result ** left
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                    
            return function_with_right_function
        
        
        # normal case
        if not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray):
            right = np.array([right])
        
        if len(left) == 1 and len(right) > 1:
            left = np.full_like(right, left[0])
        elif len(right) == 1 and len(left) > 1:
            right = np.full_like(left, right[0])
        
        if len(left) != len(right):
            raise Exception("Length error: arrays must have the same length")
        
        op = ctx.op.text
        
        if op == '+':
            return right + left
        elif op == '-':
            return right - left
        elif op == '*':
            return right * left
        elif op == '%':
            return right // left
        elif op == '|':
            return left % right
        elif op == '^':
            return right ** left
        
    def visitSpecialBinaryExpr(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        op = ctx.op.text
        
        # both parameters are functions
        if callable(left) and callable(right):
            def function_with_both_functions(x):
                left_result = left(x)
                right_result = right(x)
                
                if not isinstance(left_result, np.ndarray) and op in [',', '#']:
                    left_result = np.array([left_result])
                if not isinstance(right_result, np.ndarray) and op in [',', '#']:
                    right_result = np.array([right_result])
                    
                scalar_input = not isinstance(x, np.ndarray)
                    
                if op == ',':
                    result = np.concatenate((left_result, right_result))
                elif op == '#':
                    if not all(val in [0, 1] for val in left_result):
                        raise Exception("El primer operando del filtro debe ser una máscara de 0s y 1s")
                    result = right_result[np.array(left_result, dtype=bool)]
                elif op == '{':
                    try:
                        if isinstance(left_result, np.ndarray):
                            if np.any(np.array(left_result, dtype=int) < 0):
                                raise Exception("Índices negativos no permitidos")
                            result = right_result[np.array(left_result, dtype=int)]
                        else:
                            if left_result < 0:
                                raise Exception("Índice negativo no permitido")
                            result = right_result[left_result]
                    except IndexError:
                        raise Exception("Índice fuera de rango")
                    
                if scalar_input and op != '{' and len(result) == 1:
                    return result[0]
                return result
                
            return function_with_both_functions

        # first parameter is a function
        if callable(left):
            def special_binary_left_function(x):
                if not isinstance(x, np.ndarray) and op in [',', '#']:
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                left_result = left(x)
                
                if not isinstance(left_result, np.ndarray) and op in [',', '#']:
                    left_result = np.array([left_result])
                    
                if op == ',':
                    if not isinstance(right, np.ndarray):
                        right_array = np.array([right])
                    else:
                        right_array = right
                    result = np.concatenate((left_result, right_array))
                elif op == '#':
                    if not all(val in [0, 1] for val in left_result):
                        # Convertir directamente a booleanos para más flexibilidad
                        mask = np.array(left_result).astype(bool)
                        result = right[mask]
                    else:
                        # Si son 0s y 1s explícitos, usarlos como están
                        result = right[np.array(left_result, dtype=bool)]
                elif op == '{':
                    try:
                        if isinstance(left_result, np.ndarray):
                            if np.any(np.array(left_result, dtype=int) < 0):
                                raise Exception("Índices negativos no permitidos")
                            result = right[np.array(left_result, dtype=int)]
                        else:
                            if left_result < 0:
                                raise Exception("Índice negativo no permitido")
                            result = right[left_result]
                    except IndexError:
                        raise Exception("Índice fuera de rango")
                
                if scalar_input and op != '{' and len(result) == 1:
                    return result[0]
                return result
            
            return special_binary_left_function

        # second parameter is a function
        if callable(right):
            def special_binary_right_function(x):
                if not isinstance(x, np.ndarray) and op in [',', '#']:
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                right_result = right(x)
                
                if not isinstance(right_result, np.ndarray) and op in [',', '#']:
                    right_result = np.array([right_result])
                    
                if op == ',':
                    if not isinstance(left, np.ndarray):
                        left_array = np.array([left])
                    else:
                        left_array = left
                    result = np.concatenate((left_array, right_result))
                elif op == '#':
                    if not all(val in [0, 1] for val in left):
                        # Convertir directamente a booleanos para más flexibilidad
                        mask = np.array(left).astype(bool)
                        result = right_result[mask]
                    else:
                        # Si son 0s y 1s explícitos, usarlos como están
                        result = right_result[np.array(left, dtype=bool)]
                elif op == '{':
                    try:
                        if isinstance(left, np.ndarray):
                            if np.any(np.array(left, dtype=int) < 0):
                                raise Exception("Índices negativos no permitidos")
                            result = right_result[np.array(left, dtype=int)]
                        else:
                            if left < 0:
                                raise Exception("Índice negativo no permitido")
                            result = right_result[left]
                    except IndexError:
                        raise Exception("Índice fuera de rango")
                
                if scalar_input and op != '{' and len(result) == 1:
                    return result[0]
                return result
            
            return special_binary_right_function
        
        # normal case
        if op in [',', '#'] and not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray) and op in [',', '#']:
            right = np.array([right])
        
        if op == ',':
            return np.concatenate((left, right))
        elif op == '#':
            if not all(x in [0, 1] for x in left):
                raise Exception("El primer operando del filtro debe ser una máscara de 0s y 1s")
            return right[np.array(left, dtype=bool)]
        elif op == '{':
            try:
                if isinstance(left, np.ndarray):
                    if np.any(np.array(left, dtype=int) < 0):
                        raise Exception("Índices negativos no permitidos")
                    return right[np.array(left, dtype=int)]
                else:
                    if left < 0:
                        raise Exception("Índice negativo no permitido")
                    return right[left]
            except IndexError:
                raise Exception("Índice fuera de rango")
            
    def visitRelationalExpr(self, ctx):
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        
        op = ctx.op.text
    
        # both parameters are functions
        if callable(left) and callable(right):
            def function_with_both_functions(x):
                left_result = left(x)
                right_result = right(x)
                
                if not isinstance(left_result, np.ndarray):
                    left_result = np.array([left_result])
                if not isinstance(right_result, np.ndarray):
                    right_result = np.array([right_result])
                
                if len(left_result) == 1 and len(right_result) > 1:
                    left_result = np.full_like(right_result, left_result[0])
                elif len(right_result) == 1 and len(left_result) > 1:
                    right_result = np.full_like(left_result, right_result[0])
                
                if len(left_result) != len(right_result):
                    raise Exception("Length error: arrays must have the same length")
                    
                scalar_input = not isinstance(x, np.ndarray)
                    
                if op == '>':
                    result = np.where(left_result > right_result, 1, 0)
                elif op == '<':
                    result = np.where(left_result < right_result, 1, 0)
                elif op == '>=':
                    result = np.where(left_result >= right_result, 1, 0)
                elif op == '<=':
                    result = np.where(left_result <= right_result, 1, 0)
                elif op == '=':
                    result = np.where(left_result == right_result, 1, 0)
                elif op == '<>':
                    result = np.where(left_result != right_result, 1, 0)
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                
            return function_with_both_functions
        
        # first parameter is a function
        if callable(left):
            def relational_left_function(x):
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                left_result = left(x)
                
                if not isinstance(left_result, np.ndarray):
                    left_result = np.array([left_result])
                    
                if len(left_result) == 1 and len(x) > 1:
                    left_result = np.full_like(x, left_result[0])
                    
                if op == '>':
                    result = np.where(left_result > right, 1, 0)
                elif op == '<':
                    result = np.where(left_result < right, 1, 0)
                elif op == '>=':
                    result = np.where(left_result >= right, 1, 0)
                elif op == '<=':
                    result = np.where(left_result <= right, 1, 0)
                elif op == '=':
                    result = np.where(left_result == right, 1, 0)
                elif op == '<>':
                    result = np.where(left_result != right, 1, 0)
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                    
            return relational_left_function

        # second parameter is a function
        if callable(right):
            def relational_right_function(x):
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                right_result = right(x)
                
                if not isinstance(right_result, np.ndarray):
                    right_result = np.array([right_result])
                    
                if len(right_result) == 1 and len(x) > 1:
                    right_result = np.full_like(x, right_result[0])
                    
                if op == '>':
                    result = np.where(left > right_result, 1, 0)
                elif op == '<':
                    result = np.where(left < right_result, 1, 0)
                elif op == '>=':
                    result = np.where(left >= right_result, 1, 0)
                elif op == '<=':
                    result = np.where(left <= right_result, 1, 0)
                elif op == '=':
                    result = np.where(left == right_result, 1, 0)
                elif op == '<>':
                    result = np.where(left != right_result, 1, 0)
                    
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                    
            return relational_right_function

        # normal case
        if not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray):
            right = np.array([right])
        
        if len(left) == 1 and len(right) > 1:
            left = np.full_like(right, left[0])
        elif len(right) == 1 and len(left) > 1:
            right = np.full_like(left, right[0])
        
        if len(left) != len(right):
            raise Exception("Length error: arrays must have the same length")
        
        op = ctx.op.text
        
        if op == '>':
            return np.where(left > right, 1, 0)
        elif op == '<':
            return np.where(left < right, 1, 0)
        elif op == '>=':
            return np.where(left >= right, 1, 0)
        elif op == '<=':
            return np.where(left <= right, 1, 0)
        elif op == '=':
            return np.where(left == right, 1, 0)
        elif op == '<>':
            return np.where(left != right, 1, 0)        

    #Function application
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
        f = self.visit(ctx.expression(1))  # Right function (applied first)
        g = self.visit(ctx.expression(0))  # Left function (applied second)
        
        if not callable(f) or not callable(g):
            raise TypeError("Cannot compose non-function values")
        
        def composed_func(x):
            return g(f(x))
        
        return composed_func

    #ATOMS
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