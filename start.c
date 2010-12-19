#include <stdio.h>
#include <stdlib.h>

unsigned long *cache;

#define MAX_CACHE 1000001

unsigned long cache_start(unsigned long n);
unsigned long cache_start(unsigned long n)
{
	unsigned long result = 0;
	if(n < MAX_CACHE && cache[n] != 0)
		return cache[n];
	if(n < MAX_CACHE)
	{
		if((n%2) == 0)
			result = cache_start(n/2);
		else
			result = cache_start(n*3+1);
		cache[n] = result+1;
	}else
	{
		if((n%2) == 0)
			result = cache_start(n/2);
		else
			result = cache_start(3*n+1);
	}
	return result+1;
}

long brute_start(long n)
{
	unsigned long temp =n;
	long count = 1;
	while(temp !=1)
	{
		if((temp %2) == 0)
			temp = temp/2;
		else
			temp = temp*3+1;
		count += 1;
		
	}
	return count;
}

int main()
{
	unsigned long max = 1;
	unsigned long val = 1;
	unsigned long temp;
	unsigned long i;
	cache = (unsigned long *)calloc(sizeof(unsigned long)*MAX_CACHE,
					sizeof(unsigned long));
	cache[1] = 1;
	printf("%d\n",brute_start(13));
	for(i = 1; i <= 1000*1000;i+=1)
	{
		temp = cache_start(i);
		if(temp > val)
		{
			max = i;
			val = temp;
		}
	}
	printf("max: %d,%d\n",max,val);
}
