#!/usr/local/bin/python2.7
from collections import defaultdict
from sets import Set

import unittest


DICT = defaultdict(list)

def makeFriend(name1, name2):
  if (name2 in DICT[name1]) or (name1 in DICT[name2]):
    return "already friends"
  else:
    DICT[name1].append(name2)
    DICT[name2].append(name1)


def unmakeFriend(name1, name2):
  if (name2 not in DICT[name1]) and (name1 not in DICT[name2]):
    return "not valid friends"
  else:
    DICT[name1].remove(name2)
    DICT[name2].remove(name1)


def getDirectFriends(name1):
  if name1 not in  DICT.keys():
    return "not a valid name"
  else:
    return DICT[name1]


def find_path(start, end, path=[]):
  path = path + [start]
  if start == end:
    return path
  if not DICT.has_key(start):
    return None
  for node in DICT[start]:
    if node not in path:
      newpath = find_path(node, end, path)
      if newpath: 
        return newpath
  return None



def getIndirectFriends(name1):
  if name1 not in  DICT.keys():
    return "not a valid name"
    return None
  
  set1 = Set()
  
  for item in DICT.keys():
    if item not in DICT[name1]:
      if find_path(name1, item) and item != name1:
        set1.add(item)
        
  return set1


class TestSequenceFunctions(unittest.TestCase):
    def test_makeFriend(self):
      name1='1'
      name2='2'
      makeFriend(name1, name2)
      self.assertTrue(makeFriend(name1, name2), "already friends")
      self.assertTrue(name1 in getDirectFriends(name2)) 
      self.assertTrue(name2 in getDirectFriends(name1)) 

    def test_unmakeFriend(self):
      name1='1'
      name2='2'
      unmakeFriend(name1, name2)
      self.assertTrue(unmakeFriend(name1, name2), "not valid friends")
      makeFriend(name1, name2)
      unmakeFriend(name1, name2)
      self.assertTrue(name1 not in getDirectFriends(name2)) 
      self.assertTrue(name2 not in getDirectFriends(name1)) 


    def test_getDirectFriends(self):

      self.assertTrue(getDirectFriends('5') ,"not a valid name") 
      makeFriend('1','2')
      makeFriend('1','3')
      makeFriend('1','4')
      
      name1='1'
      name2='2'
      self.assertTrue(name1 in getDirectFriends(name2)) 
      self.assertTrue(name2 in getDirectFriends(name1)) 
      self.assertTrue(name1 not in getDirectFriends(name1)) 
      
    def test_getIndirectFriends(self):
      name1='1'
      name2='2'
      
      self.assertTrue(getDirectFriends('5') ,"not a valid name") 
      makeFriend('1','2')
      makeFriend('2','3')
      makeFriend('1','3')
      makeFriend('3','4')
      makeFriend('2','4')
      

      name1='1'
      name2='2'
      self.assertTrue(name1 not in getIndirectFriends(name1)) 
      for friend in getDirectFriends(name1):
        self.assertTrue(friend not in getIndirectFriends(name1)) 
      for friend in getIndirectFriends(name1):
        self.assertTrue(getIndirectFriends(name1).count(friend) <=1)



if __name__ == '__main__':
    unittest.main()
