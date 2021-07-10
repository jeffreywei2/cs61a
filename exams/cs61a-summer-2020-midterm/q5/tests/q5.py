test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hacker = tape([1,2], 2)
          
          >>> hacker(1)
          
          >>> hacker(2)
          'You are in!'
          
          >>> hacker = tape([1,2], 1)
          
          >>> hacker(1)
          
          >>> hacker(3) # used up attempts to gain access
          
          >>> hacker(2) # correct attempt to gain access, but already locked
          'The trapdoor has been activated!'
          
          >>> hacker = tape([1,2], 2)
          
          >>> hacker(1)
          
          >>> hacker(3) # 1 attempt left to gain access
          
          >>> hacker(2) # correct attempt to gain access
          'You are in!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> hacker = tape([1], 4)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          'The trapdoor has been activated!'
          
          >>> hacker = tape([1], 4)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(1)
          'The trapdoor has been activated!'
          
          >>> hacker = tape([1], 4)
          
          >>> hacker(1)
          'You are in!'
          
          >>> hacker = tape([1, 2, 3, 4, 5, 6], 4)
          
          >>> hacker(1)
          
          >>> hacker(2)
          
          >>> hacker(3)
          
          >>> hacker(4)
          
          >>> hacker(5)
          
          >>> hacker(6)
          'You are in!'
          
          >>> hacker = tape([1,2,3,4], 2)
          
          >>> hacker(1)
          
          >>> hacker(2)
          
          >>> hacker(3)
          
          >>> hacker(3)
          
          >>> hacker(4)
          'You are in!'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
