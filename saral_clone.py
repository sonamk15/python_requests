
  
import requests
    
BASENAME="http://saral.navgurukul.org/api"

def get(url):
    request=requests.get(url)
    response= request.json()
    return response

courses_url= BASENAME+"/courses"
courses_response = get(courses_url)


print ("\n\n\n*******************Welcome to SARAL*******************\n\n\n")
while True:    

    courses_id_list=[]
    def get_courses():
        index=0

        while index<len(courses_response["availableCourses"]):
            course = courses_response["availableCourses"][index]
            course_name = course["name"]
            course_id= course["id"]
            courses_id_list.append(course_id)
            print(str(index)+".",course_name)
            
        
            index+=1
    get_courses()
    def space():
        print("\n\n-------------------------------------------------------------------------------------------------------\n\n")	
    space()
    def choose_course():

        reply = int(input("Choose any cousre which you want to learn.\n Your answer:- "))
        choosen_courses = courses_id_list[reply]
        return choosen_courses
    courses = choose_course()	
    space()


    exercises_url = BASENAME+"/courses/"+str(courses)+"/exercises"
    exercises_response = get(exercises_url)


    slugList=[]

    def get_exercises():
        index=0



        while index<len(exercises_response["data"]):
            exercise=exercises_response["data"][index]
            parentExerciseId=exercise["parentExerciseId"]
            if parentExerciseId == None:
                exercise_name=exercise["name"]
                exercise_slug=exercise["slug"]
                slugList.append(exercise_slug)
                print(str(index)+".",exercise_name)


            elif parentExerciseId != None:
                exercise_name=exercise["name"]
                exercise_slug=exercise["slug"]
                slugList.append(exercise_slug)

                print(str(index)+".",exercise_name)

                index1=0
                while index1<len(exercise["childExercises"]):
                    child_exercise_name=exercise["childExercises"][index1]["name"]
                    child_exercise_slug=exercise["childExercises"][index1]["slug"]
                    slugList.append(child_exercise_slug)

                    print("\t"+str(index1)+".",child_exercise_name)
                    index1+=1

            index+=1
    get_exercises()		
    space()

    slug_url= BASENAME+"/courses/"+str(courses)+"/exercise/getBySlug"

    


    slug_response=get(slug_url,{'slug': slugList[0]})

    print (slug_response['content'])

    def get_content_from_slug():
        index=0
        while True:
            space()
            choose_exercise= str(input("Enter 'n' to go to next exercise or 'p' to go to previous exercise or \nTo exit from current cousre enter any key :- "))
            space()
            if choose_exercise == "n" and index < len(slugList)-1:
                slug_response=get(slug_url,{'slug': slugList[index+1]})
                print (slug_response['content'])
                index+=1


            elif choose_exercise == "p" and index >0:
            
                slug_response= get(slug_url,{'slug': slugList[index-1]})
                print (slug_response['content'])
                index-=1



            elif choose_exercise=="n" and index==len(slugList)-1:
                slug_response= get(slug_url,{'slug': slugList[index]})
                print (slug_response['content'])
                print ("\n\nNO MORE NEXT EXERCISE\n")


            elif choose_exercise=="p" and index== 0:
                slug_response= get(slug_url,{'slug': slugList[index]})
                print (slug_response['content'])
                print ("\n\nNO MORE PREVIOUS EXERCISE\n")


            else:
                print("\n\n---------------------You choose exit from current COURSE.------------------------------------\n\n")
        
                break
    get_content_from_slug()
    exit= input("Enter 'h' to go back to course or enter any key to exit:- ")
    space()
    if exit == "h":
        continue
    else:
        print("\n\n------------------------------------You choose exit.--------------------------------------------\n\n")
        break    
