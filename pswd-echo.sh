if [ $(< /proc/sys/kernel/hostname) = $winhostname ] 
then 
    g=$winmountchar
else
    if [ $(< /proc/sys/kernel/hostname) = $linhostname ] 
    then
        g=$linmountname
    fi
fi
fl=/mnt/$g/$tablepath.csv
q=$1
p="3"
if [[ $1 = '--help' ]]
then
    echo "-u --help --date --loc"
    q=$2
fi
if [[ $1 = '--date' ]]
then
    stat $fl | grep Modify | cut -d ' ' -f 2
    q=$2
fi
if [[ $1 = '--loc' ]]
then
    echo $g/$tablepath.csv
    q=$2
fi
if [[ $1 = '-u' ]]
then
    q=$2
    p="2-3"
fi
if [ -e $1 ]
then
    echo 'please give me a name of a service you want the password for'    
else
    cat $fl | grep -i $q | cut -d , -f $p | tr "," "\t"
fi
#cut -d , -f 1 $fl