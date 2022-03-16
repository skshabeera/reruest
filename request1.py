import requests
import json
url="http://saral.navgurukul.org/api/courses"
html_data=requests.get(url)
data=html_data.json()
with open("q.json","w")as file:
    json.dump(data,file,indent=4)
def navigation(s,slug_id,slug,data1):
    i=0
    while True:
        j=slug_id
        choice=input("enter the choice up,next,back,exist")
        if choice=="up":
            j-=1
            course1=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[j]))
            info=course1.json()
            print("content",info["content"])
            print(j)
        elif choice=="next":
            j+=1
            course1=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[j-1]))
            info1=course1.json()
            print("content",info1["content"])
            print(j)
        elif choice=="back":
            coun=1
            for i in data1["data"]:
                print(coun,i["name"])
                coun+=1
                for child in i["childExercises"]:
                    print("    ",coun,child["name"])
                    coun+=1
        else:
            break
print("SI.NO","","Name","","ID")
c=1
for i in data["availableCourses"]:
        print(c,"",i["name"],"",i["id"])
        c+=1
for dic in data["availableCourses"]:
    course_id=int(input("enter any course number"))
    s=data["availableCourses"][course_id-1]["id"]
    course=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercises")
    data1=course.json()
    # print(data1)
    slug=[]
    c1=1
    for i in data1["data"]:
        print(c1,i["name"])
        slug.append(i["slug"])
        c1+=1
        c2=1
        for child in i["childExercises"]:
            print("    ",c2,child["name"])
            slug.append(child["slug"])
            c2+=1
    # print(slug)
    slug_id=int(input("enter content of slug"))
    content_info=requests.get("http://saral.navgurukul.org/api/courses/"+str(s)+"/exercise/getBySlug?slug="+str(slug[slug_id-1]))
    data2=content_info.json()
    print(data2["content"])
    navigation(s,slug_id,slug,data1)






