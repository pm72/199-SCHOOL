import concurrent.futures, time

def do_something(seconds):
  print(f"Sleeping {seconds} second!")

  time.sleep(seconds)

  return "Done Sleeping..."

# =================
if __name__ == '__main__':
  start = time.time()

  with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = (4, 2, 3, 4, 1, 1, 2, 3, 2, 1)

    results = executor.map(do_something, secs)

    for result in results:
      print(result)

  end = time.time()

  print(f"Time: {end - start} second")
