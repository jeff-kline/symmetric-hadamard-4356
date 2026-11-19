/* Independent check of a text matrix (4356 lines of '+' and '-'): symmetric, constant
   diagonal, constant row and column sums, and every pair of distinct rows
   orthogonal (Hamming distance n/2), using bit-packed rows.
   cc -O2 -o check4356 code/check4356.c && ./check4356 H4356.txt */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define N 4356
#define WORDS ((N + 63) / 64)
static int8_t H[N][N];
static uint64_t R[N][WORDS];
int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "r");
  if (!f) { perror("open"); return 2; }
  static char line[N + 8];
  for (int i = 0; i < N; i++) {
    if (!fgets(line, sizeof line, f) || strlen(line) != N + 1 || line[N] != '\n') { printf("bad line %d\n", i); return 2; }
    for (int j = 0; j < N; j++) {
      if (line[j] == '+') H[i][j] = 1; else if (line[j] == '-') H[i][j] = -1;
      else { printf("bad character at %d,%d\n", i, j); return 2; }
    }
  }
  if (fgets(line, sizeof line, f)) { puts("extra data"); return 2; }
  fclose(f);
  long diag = H[0][0], rs = 0;
  for (int j = 0; j < N; j++) rs += H[0][j];
  for (int i = 0; i < N; i++) {
    long s = 0, c = 0;
    if (H[i][i] != diag) { printf("diagonal differs at %d\n", i); return 1; }
    for (int j = 0; j < N; j++) {
      int8_t x = H[i][j];
      if (x != 1 && x != -1) { printf("bad entry %d,%d\n", i, j); return 1; }
      if (x != H[j][i]) { printf("not symmetric at %d,%d\n", i, j); return 1; }
      s += x; c += H[j][i];
      if (x < 0) R[i][j / 64] |= 1ULL << (j % 64);
    }
    if (s != rs || c != rs) { printf("row/col sum differs at %d\n", i); return 1; }
  }
  long pairs = 0;
  for (int i = 0; i < N; i++)
    for (int k = i + 1; k < N; k++) {
      int d = 0;
      for (int w = 0; w < WORDS; w++) d += __builtin_popcountll(R[i][w] ^ R[k][w]);
      if (d != N / 2) { printf("rows %d,%d not orthogonal (distance %d)\n", i, k, d); return 1; }
      pairs++;
    }
  printf("PASS: order %d, symmetric, diagonal %ld, row and column sums %ld, %ld row pairs orthogonal\n",
         N, diag, rs, pairs);
  return 0;
}
