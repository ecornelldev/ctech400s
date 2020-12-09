# Exercise Title: H5P Advanced Indexing
---
## Key Technical Outcome
list(range) and slicing strings

## Exercise Context


## Exercise Instructions

Choose the correct result:

list(range(7))

[1,2,3,4,5,6,7]<br>
[0,1,2,3,4,5,6,7]<br>
[0,1,2,3,4,5,6] <b># correct </b><br>
[1,2,3,4,5,6,7,8] <br>

list(range(0,5))

[1,2,3,4,5] <br>
[0,1,2,3,4,5]<br>
[1,2,3,4] <br>
[0,1,2,3,4] <b># correct </b><br>

list(range(2,10,3))

[2,3,4,5,6,7,8,9]<br>
[2,5,8] <b># correct </b> <br>
[2,3,4,5,6,7,8,9,10]<br>
[3,5,7,9]<br>

Choose the correct result:

s = 'Good Morning Everyone!'

s[5:9]

' Morn' <br>
'Morn' <b># correct </b><br>
'Morni' <br>
' Mor' <br>


s[15:]

'e' <br>
'eryone!' <b># correct</b><br>
'Good Morning Ev'<br>
'veryone!<br>

s[3:8:2]

'd Mor' <br>
'od Mor'<br>
'dMr'<b># correct </b><br>
'o o' <br>

s[::5]

'G n re' <br>
'Good ' <br>
'GMnee'<b># correct </b><br>
'Morning Everyone!' <br>

s[-6]

'r' <b># correct </b><br>
'o'<br>
'e'<br>
'!eid' <br>
