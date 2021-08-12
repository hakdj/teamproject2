class Users:
    def __init__(self, user_id, pwd, name,email,phone,regdate):
        self.user_id = user_id;
        self.pwd = pwd;
        self.name = name;
        self.email = email;
        self.phone = phone;
        self.regdate = regdate;
    def __str__(self):
        return self.user_id+' '+self.pwd+' '+self.name+' '+self.email+' '\
               +self.phone+' '+self.regdate;

class Udata:
    def __init__(self, data_id, id, schooltype, major, graduy, age, intern, toeic, tosp, train, jobseek, cert ):
        self.data_id = data_id;
        self.id = id;
        self.schooltype = schooltype;
        self.major = major;
        self.graduy = graduy;
        self.age = age;
        self.intern = intern;
        self.toeic = toeic;
        self.tosp = tosp;
        self.train = train;
        self.jobseek = jobseek;
        self.cert = cert;
    def __str__(self):
        return str(self.data_id) + ' ' + self.id +' '+ str(self.schooltype)+\
               ' '+ str(self.major) + ' '+ str(self.graduy) +' '+str(self.age)+\
               ' '+str(self.intern)+' '+str(self.toeic)+' '+str(self.tosp)+\
               ' '+str(self.train)+' '+str(self.jobseek)+' '+str(self.cert);

class Res:
    def __init__(self, result_id,id,result,resdate):
        self.result_id = result_id;
        self.id = id;
        self.result = result;
        self.resdate = resdate;

    def __str__(self):
        return str(self.result_id)+' '+self.id+' '+self.result+' '\
            +str(self.resdate);







