test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (library-locator 10)
          (1 0)
          
          scm> (library-locator 10001)
          (1 0 0 0 1)
          
          scm> (library-locator 9090)
          ((9) 0 (9) 0)
          
          scm> (library-locator 123456790)
          (1 2 3 4 5 6 7 (9) 0)
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
