outer_code=open('complile_src.py').read()
code = compile(outer_code, 'compile_src.py', 'exec')
exec(code)