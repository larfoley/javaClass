import subprocess
import os.path

className = raw_input("Enter the name of the class signiture: ")

if not os.path.exists(className):

    os.makedirs(className)

    f = open(className + "/" + className + ".java", "w+")

    f.write("/* \n*" + className + ".java" + "\n*/")
    f.write("""\n
public class """ + className + """ {

    public static void main(String[] args) {
    }

}
    """)

    subprocess.Popen('javac ' + './' + className + '/' + className + '.java', shell=True)
