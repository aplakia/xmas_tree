treeheight=input ("Give the height of the tree")
trunkheight= input ("Give the height of the trunk")
trunkwidth= input ("Give the width of the trunk")
i=0
while i<treeheight:
  print ((" " * (treeheight-i)) + ("*" * (i*2+1)))
  i+=1
j=0
n=round(trunkheight/2,0)
while j<trunkheight:
  print ((" " * (treeheight-trunkheight/2)+("*" * trunkwidth)))
  j=j+1