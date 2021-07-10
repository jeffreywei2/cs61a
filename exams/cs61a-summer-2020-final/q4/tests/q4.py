test = {
  'name': 'q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (library-locator 12)
          (1 2)
          
          scm> (library-locator 1991)
          (1 (9) (9) 1)
          
          scm> (library-locator 0) ; no digits
          ()
          
          scm> (library-locator 99999999)
          ((9) (9) (9) (9) (9) (9) (9) (9))
          
          scm> (library-locator 1129651)
          (1 1 2 (9) 6 5 1)
          
          scm> (define just-chemistry (cons-stream 'chemistry just-chemistry))
          just-chemistry
          
          scm> (define two (cons-stream 1 (cons-stream 'chemistry two)))
          two
          
          scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'chemistry three))))
          three
          
          scm> (take 10 two)
          (1 chemistry 1 chemistry 1 chemistry 1 chemistry 1 chemistry)
          
          scm> (take 10 three)
          (x y chemistry x y chemistry x y chemistry x)
          
          scm> (take 10 (salad-switch two three))
          (1 x y 1 x y 1 x y 1)
          
          scm> (take 10 (salad-switch two just-chemistry))
          (1 1 1 1 1 1 1 1 1 1)
          
          scm> (take 10 (salad-switch three three))
          (x y x y x y x y x y)
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
