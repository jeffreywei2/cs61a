test = {
  'name': 'q7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> compact([1,1,1], [3])
          True
          
          >>> compact([1,1,1], [2])
          False
          
          >>> compact([1,1,1], [1])
          True
          
          >>> compact([1,2,3], [1,5])
          True
          
          >>> compact([1,2,3], [2])
          True
          
          >>> compact([], [1,2,3])
          False
          
          >>> compact([1,2,3], [])
          False
          
          >>> compact([], [])
          True
          
          >>> compact([1,4,2,8,3,9,4], [31])
          True
          
          >>> compact([1,4,2,8,3,9,4], [3,5,5])
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q7 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> compact([1, 2, 3, 4, 5, 9], [0])
          True
          
          >>> compact([5], [0])
          False
          
          >>> compact([0], [0])
          True
          
          >>> compact([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q7 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
