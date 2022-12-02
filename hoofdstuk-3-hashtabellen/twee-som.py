def twoSum(getallen,doel):
  for i in range(len(getallen)):
    for j in range(i+1,len(getallen)):
      if getallen[i] + getallen[j] == doel:
        return (i,j)
  return None   
  


def twoSumHash(getallen,doel):
  gezien = {}
  for index,item in enumerate(getallen):
    if doel - item in gezien:
      return (gezien[doel-item],index)
    gezien[item] = index
  return None