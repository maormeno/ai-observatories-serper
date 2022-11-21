from app.services.make_search import *
from app.services.xlsx_writer import *
import time


start = time.time()
make_search()
xlsx_writer()
end = time.time()
total_time = end - start

print("Total time: ", total_time)
