test = {
  'name': 'q7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> currency(['a', 'b', 'c'], [1, 2, 3])
          ['a', 'b', 'b', 'c', 'c', 'c']
          
          >>> currency(['a', 'b', 'c'], [3])
          ['a', 'a', 'a']
          
          >>> currency(['a', 'b', 'c'], [0, 2, 0])
          ['b', 'b']
          
          >>> currency([], [1,2,3])
          []
          
          >>> currency(['a', 'b', 'c'], [1, -1, 3])
          ['c', 'c', 'c']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q7 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
