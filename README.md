# Parallel_Life_With_mpi4py
Simple game of life with two threads (MPI)

send() & recv() methods were used.

Plane sharing: see multrheadpsace.py

Only thread #0 holds the sum of planes - shared_plane. It also makes list of earlier states of shared_plane, and makes an animation of it at the end.