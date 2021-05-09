import itertools
import subprocess

def getUserInput():
    for i in itertools.count():
        try:
            yield i, input('in [%d]:'%i)
        except KeyboardInterrupt:
            pass
        except EOFError:
            break

def execFunction(userInput):
    try:
        compile(userInput,'<stdin>','eval')
    except SyntaxError:
        return exec
    return eval

def execUserInput(i,userInput,userGlobals):
    userGlobals=userGlobals.copy()
    try:
        retval=execFunction(userInput)(userInput,userGlobals)
    except Exception as e:
        print('%s:%s'%(e.__class__.__name__,e))
    else:
        if retval is not None:
            print('Out[%d]:%s'%(i,retval))
    return userGlobals

def selectedUserGlobals(userGlobals):
    return(
        (key,userGlobals[key])
        for key in sorted(userGlobals)
        if not key.startswith('__') or not key.endswith('__')
    )

def saveUserGlobals(userGlobals,path='userGlobal.txt'):
    with open(path,'w') as fd:
        for key, val in selectedUserGlobals(userGlobals):
            fd.write('%s = %s (%s)\n' % (key,val,val.__class__.__name__))

def main():
    userGlobals={}
    saveUserGlobals(userGlobals)
    for i, userInput in getUserInput():
        userGlobals = execUserInput(i,userInput,userGlobals)
        saveUserGlobals(userGlobals)


if __name__=='__main__':
    main()

with open("output.txt","w") as f:
    p1 = subprocess.run(["ls","-la"], stdout = f, text = True)
with open("userGlobal.txt", "r")
    p2=subprocess.Popen("bc", stdin=subprocess.PIPE).communicate(b"3+4\n")
print(p2.stdin)

