import requests
import json


data1=requests.get("http://saral.navgurukul.org/api/courses")
output=data1.json()
print(output)

def json_data(jsondata):
    with open("jsondata.json","w") as file:
        json.dump(jsondata,file,indent=4)
json_data(output)
def selection_option(select,slud_id,slug,data2):
    while True:
        index=slud_id
        choice=input("Enter you are option 'up,next,back,exit:")
        if choice=="up":
            index-=1
            course1=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[index]))
            info=course1.json()
            print("content",info["content"])
            print(index)
        if choice=="next":
            index+=1
            course1=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[index-1]))
            info1=course1.json()
            print("content",info1["content"])
            print(index)
        if choice=="back":
            coun=1
            for dic in data2["data"]:
                print(coun,dic["name"])
                coun+=1
                for child in dic["childExercises"]:
                    print("     ",coun,child["name"])
                    coun+=1
        else:
            break

def Available_id_name(filename):
    count=1
    listOfCourseIds=[]
    print("SNO","  Courses Names","ID")
    for values in filename["availableCourses"]:
        print(count+1,"",values["name"]," ",values["id"])
        count+=1
        listOfCourseIds.append(values["id"])
        print(listOfCourseIds)
    for dic in filename["availableCourses"]:
        course_id=int(input("enter you are cource Id:"))
        select=filename["availableCourses"][course_id-1]["id"]
        # print(select)
        courses=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
        data2=courses.json()
        print(data2)
        slug=[]
        count1=1
        for dic_data in data2["data"]:
            print(count1,dic_data["name"])
            slug.append(dic_data["slug"])
            count1+=1
            count2=1
            for child in dic_data["childExercises"]:
                print("     ",count2,child["name"])
                slug.append(child["slug"])
                count2+=1
        
        slug_id=int(input("Enter you are content_slug:"))
        content_inf=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[slug_id-1]))
        data3=content_inf.json()
        print(data3["content"])
        selection_option(select,slug_id,slug,data2)


Available_id_name(output)

# def selection_option(select,slud_id,slug,data2):
#     while True:
#         index1=slug_id
#         options=input("Enter you are option 'up,next,back,exit:")
#         if op