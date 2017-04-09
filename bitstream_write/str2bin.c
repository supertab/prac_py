//gcc -o libpycall.so -shared -fPIC str2bin.c
#include<stdio.h>
#include<string.h>
int write(char a[], char fn[]){
FILE *fp1;
unsigned char b[2000000]={'\0'};
int j=7, s=1, t=0;
int i=0, k,z;
int len_a=0, bytes=0, last_bits=0;
len_a = strlen(a);
bytes = len_a/8;/*number of byte*/
last_bits = len_a%8; /*number of bit left*/
for(z=0; z<bytes; z++){
    for(; i<8*(z+1); i++){
        for(k=0; k<j; k++) s *=2;
        t = t + (a[i]-'0') * s;
        s=1;
        j--;    
    }
    b[z] = t;
    t=0;
    j=7;
}
/*last byte*/
s=1, t=0, j=last_bits-1;
for(i=0; i<last_bits; i++){
    for(k=0; k<j; k++) s*=2;
    t = t+(a[bytes*8+i]-'0')*s;
    s=1;
    j--;
}
if(last_bits) b[bytes]=t;

bytes = (len_a%8)? bytes+1: bytes;

//printf("%d\n", bytes);
fp1 = fopen(fn,"wb");
fwrite(b, 1, bytes, fp1);
fclose(fp1);
return 0;
}
