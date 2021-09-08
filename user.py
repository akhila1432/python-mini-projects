class User:

    def __init__(self, user_email,name,password,current_job_title):
        self.email    =      user_email
        self.name     =      name
        self.password =      password
        self.current_job_title = current_job_title

    def changepassword(self,new_password):
         self.password = new_password

    def changejobtitle(self,new_job_title):
        self.current_job_title = new_job_title

