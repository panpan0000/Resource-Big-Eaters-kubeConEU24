This is the demo code to simulate the situation of a few pods as "Resource Big Eaters", for Peter Pan's presentation <Lightning Talk: Locking the Monster: Strategies to Isolate Resource Big Eaters - Peter Pan, DaoCloud>

Actually, containers are not 100% isolated, some resources are shared between pods, so there will be resources contention.
So the code (as simple as possible) here aims to stress the shared resources.

code:

- conntrack-stress
- dns-stress
- pid-stress
- fd-stress
- mem-stress






