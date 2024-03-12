clone code and build tool for dns-stress
#go get github.com/DataDog/dnsstress

# Build image
docker build -t dns-stress .

# Stress CoreDNS
kubectl apply -f  dns-stress.yaml


# Show a victim
kubectl apply -f victim.yaml


# the Victim will suffer from connection timed out; no servers could be reached


# show core-dns pod status
kubectl -n kube-system get po |grep dns




# if stress is not enough, scale the replicas
#kubectl scale deploy dns-stress --replicas=1
