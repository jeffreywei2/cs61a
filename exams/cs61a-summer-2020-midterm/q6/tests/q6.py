test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> subpizza(2233) # 22 counts
          True
          
          >>> subpizza(2444423) # 4444 counts
          True
          
          >>> subpizza(82223) # 22 counts even if it appears as part of 222
          True
          
          >>> subpizza(234562) # 2...2 does not count if the 2s are not consecutive
          False
          
          >>> subpizza(1) # 1 counts
          True
          
          >>> subpizza(498729879871) # 1 counts
          True
          
          >>> subpizza(149872987987) # 1 counts
          True
          
          >>> subpizza(4445555) # no pizzas in this number
          False
          
          >>> subpizza(20) # no pizzas in this number
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q6 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
