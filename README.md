# Parallel_Life_With_mpi4py
Simple game of life with two threads (MPI)

send() & recv() methods were used.

Plane sharing:

 Planes from different threads overlaps as follows:

   m------------------------>
   m/2+1 ---------->
 n [ x  x  x  x  g ]
 | [ x  x  x  x  g ]
 | [ x  x  x  x  g ] <-thread #0
 | [ x  x  x  x  g ]
 V [ x  x  x  x  g ]
            [ g  x  x  x  x ]
            [ g  x  x  x  x ]
 thread #1->[ g  x  x  x  x ]
            [ g  x  x  x  x ]
            [ g  x  x  x  x ]
            <-----------m/2+1

 where g is 'ghost' column; corresponding x column is copied to g every step.
 As a sum of such planes we obtain n x m plane:

   m------------------------>
 n [ x  x  x  x  x  x  x  x ]
 | [ x  x  x  x  x  x  x  x ]
 | [ x  x  x  x  x  x  x  x ]
 | [ x  x  x  x  x  x  x  x ]
 V [ x  x  x  x  x  x  x  x ]

Only thread #0 holds the sum of planes - shared_plane. It also makes list of earlier states of shared_plane, and makes an animation of it at the end.