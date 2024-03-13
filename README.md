This is the demo code to simulate the situation of a few pods as "Resource Big Eaters".

The code is for KubeCon presentation : https://sched.co/1YeLR

<Lightning Talk: Locking the Monster: Strategies to Isolate Resource Big Eaters - Peter Pan, DaoCloud>


**Background**

Actually, containers are not 100% isolated, some resources are shared between pods, so there will be resources contention.

So the code (as simple as possible) here aims to stress the shared resources to show you some typical cases:

**Code**

- conntrack-stress
- dns-stress
- pid-stress
- fd-stress
- mem-stress






