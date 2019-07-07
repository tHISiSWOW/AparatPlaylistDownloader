import sys
python_location = sys.exec_prefix
def start():
    with open("./service.py","r") as root:
        with open("{0}\\Lib\\site-packages\\selenium\\webdriver\\common\\service.py".format(python_location), "w+") as target:
            target.write(root.read())