#! /bin/bash
rm -f /home/moussa/Documents/PROJET/projethtml/trouve_tout/nom_compare.csv 2>/dev/null && t=0 || t=1
 

case $t$z$d in
  000)
    echo "all those files have been deleted............." ;;
  111)
    echo "you have already removed the files" ;;
  *)
    echo "you have already removed some of the files, and now all are removed" ;;
esac

cd /home/moussa/Documents/PROJET/projethtml/trouve_tout/virtualapp
. bin/activate
python /home/moussa/Documents/PROJET/projethtml/trouve_tout/comparer.py

 