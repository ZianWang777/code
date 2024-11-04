def classification(average_grade):
    if average_grade>=70:
        return "1"
    elif average_grade>=60:
        return "2:1"
    elif average_grade>=50:
        return "2:2"
    elif average_grade>=40:
        return "3"
    else:
        return "F"
file_name=input()
with open(file_name,'r') as infile:
    reader=infile.readlines()[1:]
out_file_name=f"{file_name}_out.csv"
output=[]

for line in reader:
    row=line.split(',')
    id=row[0]
    grades=row[1:]
    sum=0
    number=0
    for i in grades:
        if not i=='' and not i=='\n':
            sum+=int(i)
            number+=1
    average=sum/number
    cl=classification(average)
    output.append(f"{id},{f"{average:.2f}"},{cl}")
with open(out_file_name,'w') as outfile:
    for i in output:
        outfile.write(f"{i}\n")
     
