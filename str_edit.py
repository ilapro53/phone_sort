def change(into, number, to, error='raise', set='ValueError'):
    tp = type(into)
    into = str(into)
    save = into
    if number<0:
        if tp!=float or error=='force':
            into=into[:number]+str(to)+into[number+1:]
        else:
            if error=='save':
                into = save
                return into
            elif error=='raise':
                raise ValueError('Not supposed to work with float (possibly with a modified value parameter "error")')
            elif error=='set':
                into = set
                return into
            '''
            into_fl=str(int(float(into)-float(int(into))))[2:]
            into_in=str(int(into))
            if -number > len(into_fl):
                number_in=number+len(into_fl)
                into_in=into_in[:number_in]+str(to)+into_in[number_in+1:]
            else:
                into_fl=into_fl[:number_fl]+str(to)+into_fl[number_fl+1:]
            into = str(into_in)+'.'+str(into_fl)
            '''
    elif number>0:
        if tp!=float or error=='force':
            into=into[:number-1]+str(to)+into[number:]
        else:
            if error=='save':
                into = save
                return into
            elif error=='raise':
                raise ValueError('Not supposed to work with float (possibly with a modified value parameter "error")')
            elif error=='set':
                into = set
                return into
    return tp(into)

def help(help='help'):
    if help=='help':
        print('help commands:\n    change')
    elif help=='change':
        print('change(into, number, to, error=\'raise\', set=\'ValueError\')')