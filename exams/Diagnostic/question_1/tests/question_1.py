test = {
  'name': 'question_1',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> skyscraper(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
          True
          
          >>> skyscraper(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
          True
          
          >>> skyscraper(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
          False
          
          >>> skyscraper(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
          True
          
          >>> skyscraper(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
          False
          
          >>> skyscraper(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from question_1 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
