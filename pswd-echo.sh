# /bin/bash
if [ $(< /proc/sys/kernel/hostname) = $winhostname ] 
then 
    fl=/mnt/g/$tablepath.csv
else
    if [ $(< /proc/sys/kernel/hostname) = $linhostname ] 
    then
        fl=/mnt/Gate/$tablepath.csv
    fi
fi
q=$1
p="3"
if [[ $1 = '--date' ]]
then
    stat $fl | grep Modify | cut -d ' ' -f 2
    q=$2
fi
if [[ $1 = '-u' ]]
then
    q=$2
    p="2-3"
fi
cat $fl | grep -i $q | cut -d , -f $p | tr "," "\t" 
#cut -d , -f 1 $fl