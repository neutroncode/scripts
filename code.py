#!/usr/bin/env python
#encoding:utf-8
# For all your 1337 needs.
import pause

#include <stdio.h>

code = [
"#include <stdio.h>\n",
"int main(int argc, char *argv[])",
"{",
"	int i = 0;",
"	for(i = 1; i < argc; i++){",
"		printf(\"arg %d: %s\\n\", i, argv[i]);\n"
"	}\n",
"	char *server[] = { ",
"		\"178.30.21.298\", \"98.20.1.2\",",
"		\"134.78.123.5\", \"75.75.7.3\" ",
"	};\n",
"	int server_nums = 4;\n",
"	for(i = 0; i < num_states; i++){",
"		printf('Attempting XSS attack on %r');",
"	}\n",
"	return 0;",
"}\n"
]

print("Compiling nodes...\n")

while 1 == 1:
	for x in code:
		print(x)
		pause.seconds(0.02)
