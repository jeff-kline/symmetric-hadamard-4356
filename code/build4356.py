"""Build and check a regular symmetric Hadamard matrix of order 4356 = 4*33^2.

Arguments: data/srg65-gritsenko.txt OUT.txt
Writes the matrix as 4356 lines of '+' and '-' characters.

Wallis-Whiteman 1972, Theorem 16 (m = 16): Szekeres difference sets X (skew)
and Y (symmetric) in the cyclic group of order 33 (the squares of F_67), and
the core W of a symmetric conference matrix of order 66 (Seidel matrix of
Gritsenko's SRG(65,32,15,16), arXiv:2102.05432).
Run with one BLAS thread (VECLIB_MAXIMUM_THREADS=1 OMP_NUM_THREADS=1).
"""
import re
import sys
import numpy as np

# --- conference matrix of order 66 from Gritsenko's adjacency matrix ---
tex = open(sys.argv[1]).read()
rows = re.findall(r'^([01]{65})$', tex, re.M)
assert len(rows) == 65, len(rows)
Adj = np.array([[int(c) for c in r] for r in rows], dtype=np.int64)
n = 65
assert (Adj == Adj.T).all() and (np.diag(Adj) == 0).all()
assert (Adj.sum(1) == 32).all()
A2 = Adj @ Adj
off = ~np.eye(n, dtype=bool)
assert (A2[off & (Adj == 1)] == 15).all() and (A2[off & (Adj == 0)] == 16).all()
print("SRG(65,32,15,16) verified")
J65, I65 = np.ones((n, n), dtype=np.int64), np.eye(n, dtype=np.int64)
W = J65 - I65 - 2 * Adj                     # Seidel matrix: -1 adjacent, +1 not, 0 diag
assert (W == W.T).all() and (W.sum(1) == 0).all()
assert (W @ W == 65 * I65 - J65).all()
C = np.zeros((66, 66), dtype=np.int64)
C[0, 1:] = C[1:, 0] = 1
C[1:, 1:] = W
assert (C @ C == 65 * np.eye(66, dtype=np.int64)).all()
print("symmetric conference matrix of order 66 verified: C^2 = 65 I")

# --- Szekeres difference sets in the squares of F_67 (cyclic of order 33) ---
p, m = 67, 16
g = next(x for x in range(2, p) if all(pow(x, (p - 1) // r, p) != 1 for r in (2, 3, 11)))
h = g * g % p                                # generator of the squares
Q = [pow(h, k, p) for k in range(2 * m + 1)]   # exponent k <-> group element h^k
log = {x: k for k, x in enumerate(Q)}
sq = set(Q)
X = sorted(log[x] for x in Q if (x - 1) % p in sq)   # skew
Y = sorted(log[y] for y in Q if (y + 1) % p in sq)   # symmetric
N = 2 * m + 1
assert len(X) == m and len(Y) == m
assert all((-k) % N not in X for k in X) and all((-k) % N in Y for k in Y)
diff = np.zeros(N, dtype=np.int64)
for S in (X, Y):
    for a in S:
        for b in S:
            if a != b:
                diff[(a - b) % N] += 1
assert diff[0] == 0 and (diff[1:] == m - 1).all()
print("Szekeres difference sets of size 16 in Z_33 verified (X skew, Y symmetric)")

def type1(S):
    """Type 1 (1,-1) incidence matrix: M[i,j] = +1 iff j - i in S."""
    M = -np.ones((N, N), dtype=np.int64)
    for i in range(N):
        for s in S:
            M[i, (i + s) % N] = 1
    return M

B = type1(X)
A = -type1(Y)
I33, J33 = np.eye(N, dtype=np.int64), np.ones((N, N), dtype=np.int64)
assert (B.T + B == -2 * I33).all() and (A.T == A).all() and (A @ B == B @ A).all()
assert (A @ J33 == J33).all() and (B @ J33 == -J33).all()
assert (A @ A.T + B @ B.T == 4 * (m + 1) * I33 - 2 * J33).all()
print("Lemma relations for A, B verified")

# --- Theorem 16 block matrix ---
K = np.kron
e = np.ones((1, N), dtype=np.int64)
f = np.ones((1, n), dtype=np.int64)
blocks = [
    [np.ones((1, 1), dtype=np.int64), f, K(e, f), -K(e, f)],
    [f.T, J65, K(e, W - I65), K(e, W + I65)],
    [K(e.T, f.T), K(e.T, W - I65), K(A, W) + K(J33, I65),
     -K(B + I33, W) + K(I33, J65) + K(I33 - J33, I65)],
    [-K(e.T, f.T), K(e.T, W + I65), -K((B + I33).T, W) + K(I33, J65) + K(I33 - J33, I65),
     -K(A.T, W) + K(J33, I65)],
]
H = np.block(blocks)
order = H.shape[0]
assert order == 4356 and set(np.unique(H)) == {-1, 1}
assert (H == H.T).all(), "not symmetric"
assert len(set(np.diag(H))) == 1, "diagonal not constant"
rs = H.sum(1)
assert len(set(rs)) == 1 and len(set(H.sum(0))) == 1
Hf = H.astype(np.float32)
G = Hf @ Hf.T                               # exact: integer entries below 2^24
assert (G == order * np.eye(order, dtype=np.float32)).all(), "H H^T != 4356 I"
print(f"H: order {order}, symmetric, diagonal {H[0,0]}, row sum {rs[0]}, H H^T = {order} I")
with open(sys.argv[2], "w") as out:
    for row in H:
        out.write("".join("+" if x > 0 else "-" for x in row) + "\n")
