#!/bin/bash
DNS=$(grep "nameserver" /etc/resolv.conf|head -n 1 |awk '{print $2}')

# Domain Name to be Stress
Target=$DomainName

if [ "$Target" == "" ];then
	echo "NO DomainName Env variable detected to stress against to! Using default."
	Target="kubernetes.default.svc.cluster.local"
fi

dnsstress -r $DNS:53 -inf  $Target


