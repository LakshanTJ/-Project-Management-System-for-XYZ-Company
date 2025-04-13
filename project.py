assigned_workers=0
Onhold_projects=[]
Ongoing_projects=[]
Completed_projects=[]

# print the main menu. Using While to keep repeating the menu.
while True:
    topic="                                                 xyz company"
    sub="                                                       Main Menu"
    print(topic)
    print(sub)
    print()
    print('1.  Add a new project to existing projects.')
    print('2.  Remove a completed project from existing projects.')
    print('3. Add new workers to available workers group.')
    print('4. Update details on ongoing projects.')
    print('5. Project Statistics.')
    print('6. Exit.')
    choice=int(input("                                                                                   your choice:"))
    # printing an error message if the choice is not in the range of 1-6.
    if choice==0:
           print('Enter valid choice between 1-6')
    #doing the following task if the choice=1.
    elif choice==1:
        assigned_workers=0
        Project_code = int(input("Enter a project code-"))
          #checking if the Project code is =0 while the project code is !=0
        if Project_code==0:
            print(" you exit!! Project code can't be '0' ")
        if  Project_code!= 0:
            client_Name=str(input("client Name -"))
            start_Date=str(input("Start date(DD/MM/YYYY) -"))
            expected_end_date=str(input("Expected end date(DD/MM/YYYY) -"))
            No_Workers=int(input("Number of workers -"))
            Project_Status=str(input('project status(ongoing, on hold, completed)-'))
            Project_Data={
                "Project code" : Project_code,
                "Client Name" :  client_Name,
                "Start Date": start_Date,
                "expected end date":expected_end_date,
                " No. workers": No_Workers,
                "project status":Project_Status
                  }          
            check=str(input("Do you want to save project(yes/no)-"))
            if check=='yes':
                if Project_Status=="on hold":
                    Onhold_projects.append(Project_Data)
                elif Project_Status=="ongoing":
                    Ongoing_projects.append(Project_Data)
                    assigned_workers=assigned_workers+ No_Workers
                elif Project_Status=="completed":
                   Actual_end_Date=str(input("Actual end date(DD/MM/YYYY) -"))
                   Project_Data.update({"Actual end date":Actual_end_Date})
                   Completed_projects.append(Project_Data)
                   assigned_workers=assigned_workers+ No_Workers
                   print(Completed_projects)
                else:
                  print("Invalid Project Status. Please adhere to the format in ()")
        if check=='no':
            print('project has been not been entered')
        def Remove_project():
            Project_code = int(input('Enter a project to remove-'))
            Project_Status=str(input('Project status(ongoing, on hold, completed)-'))
            check=str(input("Do you want to remove project(yes/no)-"))
            if check=='yes':
                if Project_Data["Project status"]==Project_Status:
                    if  Project_Status=="completed":
                         Completed_projects.clear(Project_Data)
                         print("you have removed the project")
                    else:
                        print("project should be completed to be removed")
                    
                    
                    
           
   
# function for updating the project.
    def Update_Project():
        assigned_workers=0
        Project_code = int(input("Enter a project code to update-"))
        if Project_code==0:
            print("Project code can't be '0' enter valid code")
        else:
            client_Name=str(input("client Name -"))
            start_Date=str(input("Start date(DD/MM/YYYY) -"))
            expected_end_date=str(input("Expected end date(DD/MM/YYYY) -"))
            No_Workers=int(input("Number of workers -"))
            Project_Status=str(input('Project status(ongoing, on hold, completed)-'))
            if Project_Data["Project code"]== Project_code:
                 updated_Project_Data={
                      "Project code" : Project_code,
                      "Client Name" :  client_Name,
                      "Start Date": start_Date,
                      " No. workers": No_Workers,
                      "expected end date":expected_end_date,
                      "Project status":Project_Status
                    }
                 
                 check=str(input("Do you want to update the project(yes/no)-"))
                 if check=='yes':
                      if Project_Status=="on hold":
                           Onhold_projects.remove(Project_Data)
                           Onhold_projects.append(updated_Project_Data)
                      elif Project_Status=="ongoing":
                           Ongoing_projects.remove(Project_Data)
                           Ongoing_projects.append(updated_Project_Data)
                           assigned_workers=assigned_workers+ No_Workers
                      elif Project_Status=="completed":
                          Completed_projects.remove(Project_Data)
                          Actual_end_Date=str(input("Actual end date(DD/MM/YYYY) -"))
                          updated_Project_Data.update({"Actual end date":Actual_end_Date})
                          Completed_projects.append(updated_Project_Data)
                          assigned_workers=assigned_workers+ No_Workers
                          print(assigned_workers)
                          print(Completed_projects)
                      else:
                         print("Invalid project status.please choose from given status")
                 else:
                    print("your project isn't updated")
    def Add_workers():
        Total_workers=int(input("Enter total number of workers in this company:"))
        Available_workers=Total_workers-assigned_workers
        add_new_workers=int(input("Number workers to add -"))
        check=str(input("Do you want to add (Yes/No)?:"))
        if check=="yes":
                Available_workers=Available_workers+add_new_workers
        else:
            print("you have not added the workers to data")

    def Project_Statistics():
            
         print("Number of ongoing projects -",len(Ongoing_projects))
         print("Number of completed projects -",len(Completed_projects))
         print("Number of on hold projects -",len(Onhold_projects))
         Total_workers=int(input("Enter total number of workers in this company:"))
         Available_workers=Total_workers-assigned_workers
         print("Number of available workers to assign -", Available_workers)
         check=str(input("Do you want to add the project (Yes/No)?:"))
         if check=="yes":
             print("Project has been added successfully")
         else:
            print("Project has not been added")

    if choice==2:
        Remove_project()
    elif choice==3:
        Update_Project()
    elif choice==4:
        Add_workers()
    elif choice==5:
        Project_Statistics()

 


    
    



        


             
           
                                         
         

