# Strexp

Strexp function makes format string vulnerability exploitation easy for 32bit binaries !

strexp( data, offset, istack, div=1)

with **data** an array of bytes to write to stack memory at location **offset**. \
**istack** is the first writable item number on the stack. \
You can select in how many step you want to write a byte (step = 2^**div**)
