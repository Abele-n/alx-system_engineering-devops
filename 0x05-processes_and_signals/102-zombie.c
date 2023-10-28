#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - produces an infinite loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - 5 new zombie processes created
 * Return: Always 0
 */
int main(void)
{
	int m;
	pid_t my_zombie;

	while (m < 5)
	{
		my_zombie = fork();
		if (my_zombie > 0)
		{
			printf("Zombie process created, PID: %d\n", my_zombie);
			sleep(1);
			m++;
		}
		else
			exit(0);
	}
	infinite_while();
} return ()EXIT_SUCCESS;
