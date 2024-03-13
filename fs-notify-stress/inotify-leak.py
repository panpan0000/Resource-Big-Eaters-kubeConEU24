import inotify.adapters
import os
from pathlib import Path

FILE_COUNT = 20000

def _create_file_and_watch():
  os.system("mkdir -p /tmp/inotify-test")
  for f in range(0,FILE_COUNT):
    Path("/tmp/inotify-test/" + str(f)).touch()
  print("touch %s files" % FILE_COUNT)


  i = inotify.adapters.Inotify()
  c = 0
  for f in range(0,FILE_COUNT):
    try:
      i.add_watch("/tmp/inotify-test/" + str(f))
      c=c+1
    except:
      break
  print( "watch %s files" % c)
  if c < FILE_COUNT:
     print("the max_user_watches in HOST OS is over.")
  for event in i.event_gen(yield_nones=False):
    (_, type_names, path, filename) = event
    print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(path, filename, type_names))


if __name__ == '__main__':
   _create_file_and_watch()

