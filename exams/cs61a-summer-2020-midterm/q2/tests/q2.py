test = {
  'name': 'q2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> competition_a = basketball()
          
          >>> competition_b, x = competition_a(2)
          
          >>> x                                   # 2
          2
          
          >>> competition_c, x = competition_b(8)
          
          >>> x                                   # 2 - 8
          -6
          
          >>> competition_d, x = competition_c(12)
          
          >>> x                                   # 2 - 8 + 12
          6
          
          >>> competition_e, x = competition_d(30)
          
          >>> x                                   # 2 - 8 + 12 - 30
          -24
          
          >>> competition_b_again, x = competition_a(100)
          
          >>> x                                   # 100 [note that we are using competition_a not competition_d here]
          100
          
          >>> footstool(basketball(), [1, 2, 3, 4, 5])
          3
          
          >>> footstool(basketball(), [4000])
          4000
          
          >>> footstool(basketball(), [2, 90])
          -88
          
          >>> footstool(identity_competition, [2, 90])
          90
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': '',
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
