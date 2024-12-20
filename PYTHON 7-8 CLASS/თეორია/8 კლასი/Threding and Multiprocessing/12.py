# import time

# def do_something():
#   print("Sleeping 1 second...")
#   time.sleep(1)
  
#   return "Done sleeping!"


# # ===============
# if __name__ == '__main__':
#   start = time.time()
#   do_something()
#   do_something()
#   end = time.time()

#   print(f"Finished at {end - start} seconds...")

# # GIL



# import time, threading

# def do_something():
#   print("Sleeping 1 second...")
  
#   time.sleep(1)
  
#   return "Done sleeping!"


# # ===============
# start = time.time()

# t1 = threading.Thread(target=do_something)   # პროცესის შექმნა
# t2 = threading.Thread(target=do_something)   # პროცესის შექმნა

# t1.start()   # შექმნილი პროცესის გაშვება
# t2.start()   # შექმნილი პროცესის გაშვება

# t1.join()
# t2.join()

# end = time.time()

# print(f"\nFinished at {end - start} seconds...")




# import time, threading

# def do_something():
#   print("Sleeping 1 second...")
  
#   time.sleep(1)
  
#   return "Done sleeping!"


# # ===============
# start = time.time()

# threads = []
# for _ in range(10):
#   t = threading.Thread(target=do_something)
#   t.start()
#   threads.append(t)

# for t in threads:
#   t.join()

# end = time.time()

# print(f"\nFinished at {end - start} seconds...")




# import time, threading

# def do_something(seconds):
#   print(f"Sleeping {seconds} second...")
  
#   time.sleep(seconds)
  
#   return f"Done sleeping in {seconds} seconds..."


# # ===============
# start = time.time()

# threads = []
# for _ in range(10):
#   t = threading.Thread(target=do_something, args=(2,))
#   t.start()
#   threads.append(t)

# for t in threads:
#   t.join()

# end = time.time()

# print(f"\nFinished at {end - start} seconds...")




# import time, threading
# from random import randint

# def do_something(seconds):
#   print(f"Sleeping {seconds} second...")
  
#   time.sleep(seconds)
  
#   return f"Done sleeping in {seconds} seconds..."


# # ===============
# start = time.time()

# threads = []
# for _ in range(10):
#   t = threading.Thread(target=do_something, args=(randint(1, 10),))
#   t.start()
#   threads.append(t)

# for t in threads:
#   t.join()

# end = time.time()

# print(f"\nFinished at {end - start} seconds...")




# import time, concurrent.futures

# def do_something(seconds):
#   print(f"Sleeping {seconds} second...")
  
#   time.sleep(seconds)
  
#   return f"Done sleeping in {seconds} seconds..."


# # ===============
# start = time.time()

# # threads = []
# # for _ in range(10):
# #   t = threading.Thread(target=do_something, args=(randint(1, 3),))
# #   t.start()
# #   threads.append(t)

# # for t in threads:
# #   t.join()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#   executor.submit(do_something, 1)

# end = time.time()

# print(f"\nFinished at {end - start} seconds...")





# import time, concurrent.futures

# def do_something(seconds):
#   print(f"Sleeping {seconds} second...")
  
#   time.sleep(seconds)
  
#   return f"Done sleeping in {seconds} seconds..."


# # ===============
# start = time.time()

# # threads = []
# # for _ in range(10):
# #   t = threading.Thread(target=do_something, args=(randint(1, 3),))
# #   t.start()
# #   threads.append(t)

# # for t in threads:
# #   t.join()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#   f1 = executor.submit(do_something, 1)
#   print(f1.result())


# end = time.time()

# print(f"\nFinished at {end - start} seconds...")





import time, concurrent.futures

def do_something(seconds):
  print(f"Sleeping {seconds} second...")
  
  time.sleep(seconds)
  
  return f"Done sleeping in {seconds} seconds..."


# ===============
start = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:  
  results = [executor.submit(do_something, 1) for _ in range(10)]

  # results = []
  # for _ in range(10):
  #   results.append(executor.submit(do_something, 1))

end = time.time()

print(f"\nFinished at {end - start} seconds...")
