test = {
  'name': 'question_3',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> carat(1234, 1)
          4
          
          >>> carat(32749, 2)
          79
          
          >>> carat(1917, 2)
          97
          
          >>> carat(32749, 18)
          32749
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from question_3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
