(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign num)
  (cond ((> num 0) 1) ((< num 0) -1) (else 0))
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((= y 0) 1)
    ((= y 1) x)
    ((even? y) (square (pow x (/ y 2))))
    ((odd? y) (* x (pow x (- y 1))))
  )
)


(define (unique s)
  (if (null? s)
  nil
  (cons (car s) (filter (lambda (x) (not (eq? x (car s)))) (unique (cdr s)))) 
  )
)


(define (replicate x n)
  (define (helper k r)
    (if (= k n)
        r
        (helper (+ k 1) (cons x r))))
  (helper 0 nil)
)

(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner (accumulate combiner start (- n 1) term)
      (term n))  
  )
)


(define (accumulate-tail combiner start n term)
    (if (= n 0)
      start
      (accumulate-tail combiner (combiner (term n) start) (- n 1) term)
    )
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)

