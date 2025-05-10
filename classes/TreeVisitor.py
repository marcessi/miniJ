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
                # Obtener texto original con preformateado para números negativos
                expr_text = self.preformat_expr_text(line_ctx.expression().getText())
                
                print(f"Procesando expresión: {expr_text}")
                
                result = self.visit(line_ctx.expression())
                if result is not None:
                    self.results.append(result)
                    print("Resultado: ", end="")
                    self.print_result(result)
        
        return self.results

    def preformat_expr_text(self, text):
        """Format expression text with spaces between tokens, handling negative numbers correctly"""
        # Reglas para formatear texto de expresiones preservando números negativos
        formatted = []
        i = 0
        while i < len(text):
            if text[i] == '_' and i+1 < len(text) and text[i+1].isdigit():
                # Es un número negativo
                neg_num = '_'
                i += 1
                while i < len(text) and text[i].isdigit():
                    neg_num += text[i]
                    i += 1
                formatted.append(neg_num)
            elif text[i].isalpha():
                # Es un identificador
                ident = text[i]
                i += 1
                while i < len(text) and (text[i].isalnum() or text[i] == '_'):
                    ident += text[i]
                    i += 1
                formatted.append(ident)
            elif text[i].isdigit():
                # Es un número positivo
                num = text[i]
                i += 1
                while i < len(text) and text[i].isdigit():
                    num += text[i]
                    i += 1
                # Separamos los dígitos para la visualización 
                formatted.append(' '.join(num))
            else:
                # Es un operador u otro carácter
                formatted.append(text[i])
                i += 1
        
        return ' '.join(formatted)
    
    def print_result(self, result):
        if isinstance(result, np.ndarray):
            # Para arrays, imprimimos los elementos con espacios entre ellos
            result_str = ' '.join(str(x) if x >= 0 else f"_{abs(x)}" for x in result)
        else:
            # Para escalares
            if result >= 0:
                result_str = str(result)
            else:
                result_str = f"_{abs(result)}"
        print(result_str)

    def visitAssignmentLabel(self, ctx):
        var_name = ctx.WORD().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return None # Or value, depending on language semantics
    
    #Atomic expressions
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())
    
    def visitNegativeExpr(self, ctx):
        result = self.visit(ctx.atom())
        return -result
    
    def visitParenExpr(self, ctx):
        return self.visit(ctx.expression())

    #Unary operations
    def visitIdentityExpr(self, ctx):
        # Implementación de ] (identidad)
        return self.visit(ctx.expression())

    def visitSizeExpr(self, ctx):
        # Implementación de # unario (tamaño)
        result = self.visit(ctx.expression())
        if isinstance(result, np.ndarray):
            return len(result)
        else:
            return 1

    def visitIotiExpr(self, ctx):
        # Implementación de i. (secuencia de n números)
        n = self.visit(ctx.expression())
        if isinstance(n, np.ndarray):
            n = n[0]
        return np.arange(n)

    def visitModifiedExpr(self, ctx):
        """Implement op: like +: (double), *: (square), etc."""
        # Obtener la expresión a la que se aplica el modificador
        expr = self.visit(ctx.expression())
        op = ctx.op.text
        
        # Caso especial: si la expresión es una función
        if callable(expr) and isinstance(expr, type(lambda: None)):
            # Crear una función compuesta que aplica el modificador al resultado
            def modified_composition(x):
                # Aplicar primero la función interna
                result = expr(x)
                
                # Determinar si es escalar
                scalar_input = not isinstance(result, np.ndarray)
                
                # Convertir a array si es necesario
                if scalar_input:
                    result_array = np.array([result])
                else:
                    result_array = result
                    
                # Aplicar el operador modificado
                if op == '+':
                    modified = result_array + result_array  # Double
                elif op == '-':
                    modified = result_array - result_array  # Always 0
                elif op == '*':
                    modified = result_array * result_array  # Square
                elif op == '%':
                    modified = result_array // result_array  # Always 1 for non-zero values
                elif op == '|':
                    modified = result_array % result_array  # Always 0
                elif op == '^':
                    modified = result_array ** result_array  # Raise to own power
                    
                # Devolver escalar si la entrada era escalar
                if scalar_input and len(modified) == 1:
                    return modified[0]
                return modified
                
            return modified_composition
        
        # Caso normal: la expresión es un valor
        # Asegurarse de que expr es un array
        scalar_input = not isinstance(expr, np.ndarray)
        if scalar_input:
            expr = np.array([expr])
        
        # Aplicar el operador modificado
        if op == '+':
            result = expr + expr  # Double
        elif op == '-':
            result = expr - expr  # Always 0
        elif op == '*':
            result = expr * expr  # Square
        elif op == '%':
            result = expr // expr  # Always 1 for non-zero values
        elif op == '|':
            result = expr % expr  # Always 0
        elif op == '^':
            result = expr ** expr  # Raise to own power
        
        # Devolver escalar si la entrada era escalar
        if scalar_input and len(result) == 1:
            return result[0]
        return result

    def visitFoldlExpr(self, ctx):
        """Implement op/ like +/ (sum), */ (product), etc."""
        expr = self.visit(ctx.expression())
        op = ctx.op.text
        
        # If we're in a context that expects a function (no argument provided)
        if callable(expr) and isinstance(expr, type(lambda: None)):
            # Return a function that applies fold to its argument
            def fold_func(x):
                # Apply the inner function first
                result = expr(x)
                
                # Then apply the fold
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
            
            return fold_func
        
        # Asegurarse de que expr es un array
        if not isinstance(expr, np.ndarray):
            expr = np.array([expr])
        
        # Aplicar la operación de fold
        if op == '+':
            return np.sum(expr)
        elif op == '*':
            return np.prod(expr)
        elif op == '-':
            # Fold con resta: r[0] - r[1] - r[2] - ...
            result = expr[0]
            for i in range(1, len(expr)):
                result -= expr[i]
            return result
        elif op == '%':
            # División entera secuencial
            result = expr[0]
            for i in range(1, len(expr)):
                result //= expr[i]
            return result
        elif op == '|':
            # Módulo secuencial
            result = expr[0]
            for i in range(1, len(expr)):
                result %= expr[i]
            return result
        elif op == '^':
            # Potencia secuencial
            result = expr[0]
            for i in range(1, len(expr)):
                result **= expr[i]
            return result

    #Binary operations
    def visitBinaryExpr(self, ctx):
        # Evaluar de derecha a izquierda - INVERTIR ORDEN DE EVALUACIÓN
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        
        # Evaluar de derecha a izquierda - INVERTIR ORDEN DE EVALUACIÓN
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        
        op = ctx.op.text
        
        # Caso especial: si uno de los operandos es una función (como ])
        # y estamos en un contexto de asignación, crear una función compuesta
        if callable(right):
            # Estamos definiendo una función que aplica un operador con un valor fijo
            # Como en "2 | ]" que crea una función que calcula "2 mod x"
            def function_with_operator(x):
                # Convertir a array si es necesario
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                # Aplicar operador con left como primer operando
                if op == '+':
                    result = left + x
                elif op == '-':
                    result = left - x
                elif op == '*':
                    result = left * x
                elif op == '%':
                    result = left // x
                elif op == '|':
                    result = x % left  # En J, modulo se representa con |
                elif op == '^':
                    result = left ** x
                    
                # Devolver escalar si la entrada era escalar
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
                
            return function_with_operator
        
        # Verificar si estamos tratando con funciones (caso no esperado)
        if callable(left):
            raise TypeError(f"Error: Operación binaria no soportada con función como operando izquierdo")
        
        # Convertir escalares a arrays para consistencia
        if not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray):
            right = np.array([right])
        
        # Caso especial: si uno es escalar (longitud 1) y el otro no
        if len(left) == 1 and len(right) > 1:
            left = np.full_like(right, left[0])
        elif len(right) == 1 and len(left) > 1:
            right = np.full_like(left, right[0])
        
        # Verificar longitudes iguales para operaciones
        if len(left) != len(right):
            raise Exception("Length error: arrays must have the same length")
        
        op = ctx.op.text
        
        # Realizar la operación según el operador
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '%':
            return left // right
        elif op == '|':
            return right % left  # En J, los operandos están al revés
        elif op == '^':
            return left ** right
        
    def visitFlippedBinaryExpr(self, ctx):
        """Implementación del operador con flip (ej: expr1 op~ expr2)"""
        # Evaluar de derecha a izquierda como los demás operadores binarios
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        op = ctx.op.text
        
        # Convertir escalares a arrays para consistencia
        if not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray):
            right = np.array([right])
        
        # Caso especial: si uno es escalar (longitud 1) y el otro no
        if len(left) == 1 and len(right) > 1:
            left = np.full_like(right, left[0])
        elif len(right) == 1 and len(left) > 1:
            right = np.full_like(left, right[0])
        
        # Verificar longitudes iguales para operaciones
        if len(left) != len(right):
            raise Exception("Length error: arrays must have the same length")
        
        # Aplicar el operador con operandos invertidos (right op left en lugar de left op right)
        if op == '+':
            return right + left  # + es conmutativo, no importa el orden
        elif op == '-':
            return right - left  # Orden invertido
        elif op == '*':
            return right * left  # * es conmutativo, no importa el orden
        elif op == '%':
            return right // left  # Orden invertido
        elif op == '|':
            return left % right  # Orden invertido
        elif op == '^':
            return right ** left  # Orden invertido
        
    def visitSpecialBinaryExpr(self, ctx):
        """Implementación de operadores binarios especiales: ',', '{', '#'"""
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.op.text
        
        # Caso especial: si el segundo operando es una función
        if callable(right):
            # Estamos definiendo una función que aplica el operador con left fijo
            def special_binary_function(x):
                # Convertir a array si es necesario
                if not isinstance(x, np.ndarray) and op in [',', '#']:
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                if op == ',':  # Concatenación
                    if not isinstance(left, np.ndarray):
                        left_array = np.array([left])
                    else:
                        left_array = left
                    result = np.concatenate((left_array, x))
                elif op == '#':  # Filtro con máscara
                    # Verificar que left sea una máscara de 0s y 1s
                    if not all(val in [0, 1] for val in left):
                        raise Exception("El primer operando del filtro debe ser una máscara de 0s y 1s")
                    # Aplicar la máscara
                    result = x[np.array(left, dtype=bool)]
                elif op == '{':  # Acceso por índice
                    # Verificar que los índices en left son válidos
                    try:
                        if isinstance(left, np.ndarray):
                            # Asegurarse de que todos los índices están en rango antes de aplicarlos
                            if np.any(np.array(left, dtype=int) < 0):
                                raise Exception("Índices negativos no permitidos")
                            result = x[np.array(left, dtype=int)]
                        else:
                            if left < 0:
                                raise Exception("Índice negativo no permitido")
                            result = x[left]
                    except IndexError:
                        raise Exception("Índice fuera de rango")
                
                # Devolver resultado adecuado según tipo de entrada
                if scalar_input and op != '{' and len(result) == 1:
                    return result[0]
                return result
            
            return special_binary_function
        
        # Convertir escalares a arrays para ciertas operaciones
        if op in [',', '#'] and not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray) and op in [',', '#']:
            right = np.array([right])
        
        # Implementación normal (cuando ambos operandos son valores)
        if op == ',':  # Concatenación
            return np.concatenate((left, right))
        elif op == '#':  # Filtro con máscara
            # Verificar que left sea una máscara de 0s y 1s
            if not all(x in [0, 1] for x in left):
                raise Exception("El primer operando del filtro debe ser una máscara de 0s y 1s")
            # Aplicar la máscara
            return right[np.array(left, dtype=bool)]
        elif op == '{':  # Acceso por índice
            try:
                # Asegurarse de que los índices están en formato adecuado
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
        # Evaluación de derecha a izquierda para operadores relacionales
        right = self.visit(ctx.expression(1))
        left = self.visit(ctx.expression(0))
        
        op = ctx.op.text
    
        # Caso especial: si uno de los operandos es una función (como ])
        if callable(right):
            # Crear una función que aplique la relación con el valor left
            def relational_function(x):
                # Convertir a array si es necesario
                if not isinstance(x, np.ndarray):
                    x = np.array([x])
                    scalar_input = True
                else:
                    scalar_input = False
                    
                # Aplicar el operador relacional entre left y x
                if op == '>':
                    result = np.where(left > x, 1, 0)
                elif op == '<':
                    result = np.where(left < x, 1, 0)
                elif op == '>=':
                    result = np.where(left >= x, 1, 0)
                elif op == '<=':
                    result = np.where(left <= x, 1, 0)
                elif op == '=':
                    result = np.where(left == x, 1, 0)
                elif op == '<>':
                    result = np.where(left != x, 1, 0)
                    
                # Devolver escalar si la entrada era escalar
                if scalar_input and len(result) == 1:
                    return result[0]
                return result
            
            return relational_function

        # Convertir a arrays para operaciones vectorizadas
        if not isinstance(left, np.ndarray):
            left = np.array([left])
        if not isinstance(right, np.ndarray):
            right = np.array([right])
        
        # Caso especial: si uno es escalar y el otro no
        if len(left) == 1 and len(right) > 1:
            left = np.full_like(right, left[0])
        elif len(right) == 1 and len(left) > 1:
            right = np.full_like(left, right[0])
        
        # Verificar longitudes iguales para operaciones
        if len(left) != len(right):
            raise Exception("Length error: arrays must have the same length")
        
        op = ctx.op.text
        
        # Aplicar operador relacional
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
        """Handle function application"""
        func_name = ctx.WORD().getText()
        if func_name not in self.variables:
            raise NameError(f"Error: Function '{func_name}' not defined.")
            
        func = self.variables[func_name]
        if not callable(func):
            raise TypeError(f"Error: '{func_name}' is not a function.")
            
        # Get the argument
        arg = self.visit(ctx.expression())
        
        # Apply the function to the argument
        return func(arg)
    
    def visitComposeExpr(self, ctx):
        """Handle function composition with @:"""
        # Get the two functions to compose
        f = self.visit(ctx.expression(1))  # Right function (applied first)
        g = self.visit(ctx.expression(0))  # Left function (applied second)
        
        # Make sure both are callable
        if not callable(f) or not callable(g):
            raise TypeError("Cannot compose non-function values")
        
        # Create a new function that applies f then g
        def composed_func(x):
            return g(f(x))
        
        return composed_func

    #ATOMS
    def visitListAtom(self, ctx):
        """Handle list of integers, including negative numbers"""
        ints = []
        
        # Process INT tokens (positive numbers)
        for token in ctx.INT():
            ints.append(int(token.getText()))
        
        # Process NEG_INT tokens (negative numbers)
        for token in ctx.NEG_INT():
            # The token includes the '_' prefix, so remove it and negate
            ints.append(-int(token.getText()[1:]))
        
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
        """Handle the identity function ]"""
        # Return a callable that returns its argument
        def identity_func(x):
            return x
        return identity_func
    
    def visitSizeFuncExpr(self, ctx):
        """Handle size function # used alone"""
        def size_func(x):
            # Convert to array if needed
            if not isinstance(x, np.ndarray):
                return 1  # Un escalar tiene tamaño 1
            else:
                return len(x)  # Retorna el tamaño del array
        
        return size_func

    def visitIotiFuncExpr(self, ctx):
        """Handle iota function i. used alone"""
        def ioti_func(x):
            # Convert to scalar if needed
            if isinstance(x, np.ndarray):
                if len(x) == 0:
                    return np.array([])
                x = x[0]  # Tomar el primer elemento si es un array
            
            # Generar secuencia de 0 a x-1
            if x < 0:
                raise ValueError("i. requiere un argumento no negativo")
            
            return np.arange(x)
        
        return ioti_func
    
    def visitModifiedFuncExpr(self, ctx):
        """Handle modified function expressions like +: or *: used alone"""
        op = ctx.op.text
        
        # Create a function that applies the modification to its argument
        def modified_func(x):
            # Determine if input is scalar
            scalar_input = not isinstance(x, np.ndarray)
            
            # Convert to array if needed
            if scalar_input:
                x_array = np.array([x])
            else:
                x_array = x
                
            if op == '+':
                result = x_array + x_array  # Double
            elif op == '-':
                result = x_array - x_array  # Always 0
            elif op == '*':
                result = x_array * x_array  # Square
            elif op == '%':
                result = x_array // x_array  # Always 1 for non-zero values
            elif op == '|':
                result = x_array % x_array  # Always 0
            elif op == '^':
                result = x_array ** x_array  # Raise to own power
                
            # Return scalar if input was scalar
            if scalar_input:
                return result[0]
            return result
        
        return modified_func

    def visitFoldlFuncExpr(self, ctx):
        """Handle fold function expressions like +/ or */ used alone"""
        op = ctx.op.text
        
        # Create a function that applies the fold operation to its argument
        def fold_func(x):
            # Convert to array if needed
            if not isinstance(x, np.ndarray):
                x = np.array([x])
                
            if op == '+':
                return np.sum(x)
            elif op == '*':
                return np.prod(x)
            elif op == '-':
                # Fold with subtraction: x[0] - x[1] - x[2] - ...
                result = x[0]
                for i in range(1, len(x)):
                    result -= x[i]
                return result
            elif op == '%':
                # Division fold
                result = x[0]
                for i in range(1, len(x)):
                    result //= x[i]
                return result
            elif op == '|':
                # Modulo fold
                result = x[0]
                for i in range(1, len(x)):
                    result %= x[i]
                return result
            elif op == '^':
                # Power fold
                result = x[0]
                for i in range(1, len(x)):
                    result **= x[i]
                return result
        
        return fold_func