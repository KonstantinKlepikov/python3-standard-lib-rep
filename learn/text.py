import string, re

def main():
    
    s = "The longest string to Test a 'different' Method and solutions"
    
    print('>>> Module string - oldstyle solutions')
    print('> string.capwords')
    print(s)
    print(string.capwords(s))
    
    print('> string.Template')
    
    val = {'foo': 'base'}
    t = string.Template("""
    Variable    : $foo
    Escape      : $$
    Var in text : ${foo}
    """)
    print('Template:', t.substitute(val))
    
    # vars translate to str as it is, no variables, no formating
    # but we have solutions fo missed values
    
    t = string.Template('$foo is correct, but $missing is missing')
    try:
        print('substitude(): ', t.substitute(val))
    except KeyError as err:
        print('ERROR', str(err))
    print('safe_substitude(): ', t.safe_substitute(val))
    
    # we can redefine patterns of Template
    class MyTemplate(string.Template):
        delimiter = '{{'
        pattern = r'''
        \{\{(?:
        (?P<escaped>\{\{)|
        (?P<named>[ a-z][ a-z0-9]*)\}\}|
        (?P<braced>[ a-z][ a-z0-9]*)\}\}|
        (?P<invalid>)
        )
        '''
    t = MyTemplate('''
    {{{{
    {{foo}}
    ''')
    
    print('Matches:' , t.pattern.findall(t.template))
    print('Substituted:', t.safe_substitute(foo='replacement'))
    
    print('> class Formatter')
    
    # Represents the sane as format() method of class str
    # It can be used for creation subclasses
    
    from string import Formatter
    
    class MyFormst(Formatter):
        pass
    
    print('>>> textwrap')
    
    # For formsating to output
    
    t = '''
    На пылающей палубе мальчик стоял,
    У ног его дикий огонь танцевал.
    Стоял он красиво и гордо, будто тигрёнок,
    Из плоти и крови храбрец, а снаружи ребёнок...
    '''    
        
    import textwrap
    
    # format by fill for given width
    print(textwrap.fill(t, width=50))
    
    # remove indentations - is removed only joint indentatons
    print(t) 
    print(textwrap.dedent(t))
    
    # fill and dedent
    dedented = textwrap.dedent(t).strip()
    print(textwrap.fill(dedented, width=50))


if __name__ == '__main__':
    
    main()