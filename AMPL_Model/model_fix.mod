set INTER; # intersections
param entr symbolic in INTER; # entrance to road network
param exit symbolic in INTER, <> entr; # exit from road network
set ROADS within INTER cross INTER;
param time {ROADS} >= 0; # times to travel roads
var Use {(i,j) in ROADS} >= 0; # 1 iff (i,j) in shortest path
minimize Total_Time: sum {(i,j) in ROADS} time[i,j] * Use[i,j];
subject to Start: sum {(entr,j) in ROADS} Use[entr,j] = 1;
subject to noback: sum{(k,entr) in ROADS} Use[k,entr] = 0;
subject to End: sum {(k,exit) in ROADS} Use[k,exit]=1;
subject to noback2: sum {(exit,j) in ROADS} Use[exit,j] = 0;
subject to Balance {k in INTER diff {entr,exit}}:
sum {(i,k) in ROADS} Use[i,k] = sum {(k,j) in ROADS} Use[k,j];
data data.dat;
