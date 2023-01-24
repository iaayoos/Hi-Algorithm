# 선택정렬
array=[7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j # 매번 새로운 애로 갱신
        array[i],array[min_index]=array[min_index],array[i]
print(array)

# 삽입정렬
array2=[7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array2)):
    for j in range(i,0,-1): # 자기보다 앞에 있는 애들 차례대로
        if array2[j]<array2[j-1]:
            array2[j],array2[j-1]=array2[j-1],array2[j]
        else: # 자기보다 작은 애를 만나면 스탑
            break
print(array2)

# 퀵정렬
array3=[5,7,9,0,3,1,6,2,4,8]
def quick(array,start,end):
    if start>=end: # 원소가 하나면(다 하면) 종료
        return
    pivot=start
    left=start+1
    right=end
    while(left<=right):
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        while(right>start and array[right]>=array[pivot]):
            right-=1
        if(left>right):# 엇갈리면 작은 애랑 피벗이랑 교체. 피벗은 왼쪽에 있었으니
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left],array[right]=array[right],array[left]
    quick(array,start,right-1)
    quick(array,right+1,end)
quick(array3,0,len(array3)-1)
print(array3)

#퀵정렬2
array4=[5,7,9,0,3,1,6,2,4,8]
def quick2(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]
    left_side=[x for x in tail if x<=pivot]
    right_side=[x for x in tail if x>pivot]
    return quick2(left_side)+[pivot]+quick2(right_side)
print(quick2(array4))

#계수정렬(모든 원소가 0 이상이라고 가정)
array5=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count=[0]*(max(array5)+1) #모든 범위 포함 리스트 만들어놓기. 카운트용
for i in range(len(array5)):
    count[array5[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
