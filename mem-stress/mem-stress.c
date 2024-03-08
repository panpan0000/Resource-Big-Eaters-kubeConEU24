
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main (void) {
	int n = 0;
	long sliceSize=1<<25; //32MB
	printf("each size=%d MB\n", sliceSize/1024/1024);
	sleep(2);
	while (1) {
		if (malloc(sliceSize) == NULL) {
			printf("malloc failure after %d MiB\n", n);
			return 0;

		}
		++n;
		printf ("got %d MiB\n",n * (sliceSize/(1<<20)));

		/*if (n > 上限值 ){
		 * 		  sleep(100000);
		 * 		  		  } */

	} //11036480/32

}
