
import cherrypy

import mysql.connector


class WelcomePage:

    def index(self):
        
        return '''
            <body>
            <form action="store" method="POST">
             <h1 align="center">TECHNICAL PORTPHOLIO </h1>
            <table align = "center" >
            <tr height = "40px"><td>Programming Languages :</td>
            <td><input type="text" name="pro" /></td></tr>
            
            <tr height = "40px"><td>Web Development Languages :</td>
            <td><input type = "text" name = "web"></td></tr>
            <tr height = "40px"><td>Operating Systems :</td>
            <td><input type = "text" name = "opr"></td></tr>
            <tr height = "40px"><td>IDE :</td>
            <td><input type = "text" name = "ide"></td></tr>
            <tr height = "40px"><td>Databases :</td>
            <td><input type = "text" name = "dba">
            <tr height = "40px"><td>Projects :</td>
            <td><input type = "text" name = "projects"></td></tr>
            <tr height = "40px"><td>Project Discription :</td>
            <td><textarea name = "pdesc"></textarea></td></tr>
            <td><input type="submit" ></td></tr></table>
            </form>
            </body>'''
            
    index.exposed = True
    
    def store(self,pro,web,opr,ide,dba,projects,pdesc):
        
        p = "%s" % pro
        w = "%s" % web
        o = "%s" % opr
        i = "%s" % ide
        d = "%s" % dba
        j = "%s" % projects
        e = "%s" % pdesc
        
        if p =='' or w == '' or o == '' or i == '' or d == '' or j == '' or e == '' :
            return '<h2>PLEASE FILL ALL THE FIELD<a href="../"> HERE</a></h2>'
        cnx = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='Techp')
        cursor = cnx.cursor()
        sql = """insert into portfolio (Pro_lan,Web_dev,Os,Ide,Db,Projects,Pro_desc)values("%s","%s","%s","%s","%s","%s","%s" )""" %(p,w,o,i,d,j,e)
        
        cursor.execute(sql)
        cnx.commit()
        cnx.close()
        
        return "<h2> YOU HAVE SUCSESSFULLY SUBMITED YOUR DATA </h2>"
                
    store.exposed = True


import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    
    cherrypy.quickstart(WelcomePage(), config=tutconf)

