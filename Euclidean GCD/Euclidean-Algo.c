//
//  Euclidean-Algo.c
//  An efficient algorithm for finding the greatest common divisor of two integers.
//
//  Created by Ji Hong Guen on 29/10/18.
//  Copyright © 2018 Ji Hong Guen. All rights reserved.
//

#include <stdio.h>

int euclideanGCD(int x, int y);     // Get a value of two value's Greatest Common Divisor.
void swap(int *x, int *y);          // This function exchanges original's value.
int tmp;                            // This will only be used at once.


main()
{

  int x, y;

  printf("Type the First Number : ");
  scanf("%d", &x);

  printf("Type the Second Number : ");
  scanf("%d", &y);

  printf("The GCD : %d\n", euclideanGCD(x, y));

}

int euclideanGCD(int x, int y)
{
  if (x < y) swap(&x, &y);          // For a convenience, if y is bigger, exchange them.
  if (!y) return x;                 // The basis level of this recursion.
  return euclideanGCD(y, x % y);    // Do this recursively.
}

void swap(int *x, int *y)           // This function exchanges original's value.
{
  tmp = *x;
  *x = *y;
  *y = tmp;
}
