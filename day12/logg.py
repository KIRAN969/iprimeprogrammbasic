import logging

logging.basicConfig(filename='demo.log',level=logging.DEBUG)


# x=10
# y=20
# z=x+y
# logging.info(z)

try:
    n1=int(input("enter the number:"))
    n2=int(input("enter the number:"))
    result=n1/n2
    logging.info(result)
except:
    logging.error("an unknown error happened")





# logging.critical("critical error happened")

# logging.error("an unknown error happened")

# logging.warning("expected value is an integer")

# logging.info("normal message")

# logging.debug("for developers")