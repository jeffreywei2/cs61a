test = {
  'name': 'q0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_compvsinterp in ['True, there is no way to convert an interpreter to a compiler', 'False, compilers and interpreters are the same', 'False, you can turn an interpreter into a compiler via a Futamura projection'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_pyfeatures in ['Memory Management', 'Functions', 'Lazy Evaluation', 'Coroutines'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_regression in ['Triangular', 'Orthogonal', 'Parallel', 'Hyperplexed'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> assert mc_result_neural_networks in ['Finding features', 'Being an inference tool', 'Approximating nonlinear relationships', 'Using high-dimensional space'], 'Selected an invalid option'
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q0 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
