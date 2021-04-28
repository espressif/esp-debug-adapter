#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

extern int print_hamlet(void);

static void start_new_thread(long num);

static void *print_hamlet_thread(void *arg)
{
    long num = (long)arg;
    int lines = print_hamlet();
    printf("\n[Printed lines of the play: %d]\n", lines );
    printf("[Bye!] from thread %ld\n", num);
    if (num < 5)
        start_new_thread(num + 1);
}

static void start_new_thread(long num)
{
    pthread_t thread_id;
    
    sleep(1);
    int ret = pthread_create(&thread_id, NULL, print_hamlet_thread, (void *)num);
    if (ret != 0) {
        printf("Failed to create thread %ld\n", num);
    } else {
        printf("Created thread %ld, id 0x%lx\n", num, thread_id);
    }
}

int main()
{
    start_new_thread(0);
    while(1);
    return 0;
}