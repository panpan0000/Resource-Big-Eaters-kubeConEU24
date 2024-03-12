This is the demo code to simulate the situation of a few pods as "Resource Big Eaters",
for KubeCon presentation :
<Lightning Talk: Locking the Monster: Strategies to Isolate Resource Big Eaters - Peter Pan, DaoCloud>
https://kccnceu2024.sched.com/event/4bc5b2fd8cbbdc6a51f38d4f17513017?iframe=no

Actually, containers are not 100% isolated, some resources are shared between pods, so there will be resources contention.

So the code (as simple as possible) here aims to stress the shared resources as some examples.

code:

- conntrack-stress
- dns-stress
- pid-stress
- fd-stress
- mem-stress






