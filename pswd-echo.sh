if [ $(< /proc/sys/kernel/hostname) = WunderStatione ] 
then 
    fl=/mnt/g/Data/ססמאות.csv
else
    if [ $(< /proc/sys/kernel/hostname) = OakenShield ] 
    then
        fl=/mnt/Gate/Data/ססמאות.csv
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
    p="2-3"
fi
cat $fl | grep $q | cut -d , -f $p | tr "," "\t"
#cut -d , -f 1 $fl