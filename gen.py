import subprocess

header = r'''
#include "emscripten.h"
#include <iostream>

'''

fnNames = []
mainFnNames = []
fnDecls = []
noFns = 40000
i = 0
declaration = "int (*foo)(int);\n"
while i < noFns:
    fnNames.append("sidey" + str(i))
    mainFnNames.append("mainey" + str(i))
    fnDecls.append("extern int " + "sidey" + str(i) + "(int input);\n")
    i+=1

for fnDecl in fnDecls:
    declaration += fnDecl

main = "EMSCRIPTEN_KEEPALIVE int main(int argc, char* argv[]) {\n" + "if (argc == 0) { foo=sidey0; }" + "\nelse { foo = sidey0; }\nfoo(argc); return 0;\n}"

clauses = []
i=0
while i < noFns:
    clauses.append("EMSCRIPTEN_KEEPALIVE int " + mainFnNames[i] + "(int input) {\n" + "if (input==0) { foo=" + fnNames[i] + ";}" + "foo(input); return input;}\n")
    i+=1

clauseBody = ''

for clause in clauses:
    clauseBody += clause

code = header + declaration + main + clauseBody
f_cpp = "main.cpp"
with open(f_cpp,'w') as FOUT:
    FOUT.write(code)


sideDeclaration = ""
fns = []

i = 0
while i < noFns:
    fns.append(r'EMSCRIPTEN_KEEPALIVE int ' + fnNames[i] + r'(int input) { printf("' + fnNames[i] + r':%d\n", input); return input;}' + "\n")
    i+=1

fnBody = ""
for fns in fns:
    fnBody += fns

sideCode = header + fnBody

with open("side.cpp",'w') as FOUT:
    FOUT.write(sideCode)