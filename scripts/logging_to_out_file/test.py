import logging

# save output in a file called test.out
logging.basicConfig(filename='test.out', encoding='utf-8', level=logging.INFO)

logging.info("does this work")
