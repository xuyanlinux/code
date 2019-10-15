#Author:Timmy
import configparser
config = configparser.ConfigParser()
lis = config.read('userdb.info')
s = config.sections()
print(type(lis))
print(s)

na = config['huhu']['password']
print(na)