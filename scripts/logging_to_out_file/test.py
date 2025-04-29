import logging

# save output in a file called test.out
logging.basicConfig(filename="test.out", encoding="utf-8", level=logging.INFO)

s = 0
logging.info("does this work {}".format(s))
