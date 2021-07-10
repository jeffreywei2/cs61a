test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM parta;
          bike f
          bike c
          bike d
          """,
          'hidden': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': 'sqlite> .read q1.sql',
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
